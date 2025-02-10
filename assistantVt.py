# Bibliotecas padrão do Python
import os
import asyncio
import webbrowser
from datetime import datetime
from random import randint
from time import sleep

# Bibliotecas de terceiros
import flet as ft
import pyttsx3
import speech_recognition as sr
from ollama import AsyncClient

# Módulos locais/personalizados
from clasificacion import classify_text


class VirtualAssistant(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page: ft.Page                  =  page
        self.text_speak                     =  pyttsx3.init()
        self.speech_queue: list[str]        =  []

        # settings of VirtualAssistant
        self.wave                       =  self.create_wave_speak()
        self.expand                     =  True
        self.alignment                  =  ft.MainAxisAlignment
        self.status_window              =  True
        self.status_animate_waves       =  False

        self.bar_speak = ft.Row(
                expand          =  True, 
                controls        =  self.wave, 
                alignment       =  ft.MainAxisAlignment.CENTER)
        
        self.display_speak = ft.Container(
            content             =  self.bar_speak,
            expand              =  True,
            height              =  200
        )

        self.controls.append(self.display_speak)

    def create_wave_speak(self, waveTotal: int = 10) -> list[ft.Container]:
        waves = [ 
            ft.Container(
                height          =  10, 
                width           =  20, 
                bgcolor         =  '#00A6FF', 
                border_radius   =  16,
                animate         =  ft.animation.Animation(400, 'ease_in_out')
                ) for _ in range(waveTotal)
            ]
        
        return waves

    def animate_waves(self) -> None:
        while self.status_animate_waves:
            for wave in self.wave:
                wave.height = randint(10, 100)
            
            self.page.update()

            sleep(0.4)

        for wave in self.wave:
            wave.height = 10

        self.page.update()
        sleep(1)
    
    def speak(self, text) -> None:
        self.status_animate_waves = True
        self.page.run_thread(self.animate_waves)

        self.text_speak.setProperty('rate', 180)
        voices = self.text_speak.getProperty('voices')
        self.text_speak.setProperty('voice', voices[0].id)

        self.text_speak.say(text)
        self.text_speak.runAndWait()
        
        
        self.status_animate_waves = False

    async def chat(self, question: str) -> None:
        message = {
            'role': 'user', 
            'content': f'faça uma pesquisa sobre {question}'}

        word_accumulator = ''
        async for part in await AsyncClient().chat(
            model           =  'llama3.1', 
            stream          =  True,
            messages        =  [message]):
            content         =  part['message']['content']
            word_accumulator += content
            if word_accumulator.endswith('.') or word_accumulator.endswith(','):
                self.speak(word_accumulator.replace('*', ''))
                self.speech_queue.append(word_accumulator)
                word_accumulator = ''

    def speak_time(self) -> None:
        time_now = datetime.now().strftime('%H:%M')
        self.speak(f"Agora são: {time_now}")

    def speak_date(self) -> None:
        year    =  int(datetime.now().year)
        month   =  int(datetime.now().month)
        day     =  int(datetime.now().day)

        self.speak(f"A data atual é: ")
        self.speak(f'{day}')
        self.speak(f'do {month}')
        self.speak(f'de {year}')

    def speak_greeting(self) -> None:
        hour = datetime.now().hour

        if 6 <= hour < 12:
            self.speak("Bom Dia mestre!")
        elif hour < 18:
            self.speak("Boa tarde mestre!")
        else:
            self.speak("Boa Noite mestre!")

        self.speak('Maria a sua disposição! em que posso ajuda-lo!')

    def microphone(self) -> str:
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            command = r.recognize_google(audio, language='pt-br')
            return command
        
        except Exception as e:
            #self.speak('Não consegui entender! tem como repetir, por favor')
            return 'None'
    
    def open_you_tube(self):
        _webbrowser = webbrowser.open_new_tab('https://www.youtube.com/')

        if _webbrowser:
            self.speak('YouTube foi aberto!')
        else:
            self.speak('Não consegui abrir o YouTube!')

    def open_vs_code(self):
        os.system('code')

    def open_chrome(self):
        os.system('"C:/Program Files/Google/Chrome/Application/chrome.exe"')

    def main(self):
        self.speak_greeting()

        while self.status_window:
            command = self.microphone().lower()
            if classify_text(command) == 'pergunta':
                if 'como você está' in command:
                    self.speak("Estou bem! Obrigado por perguntar.")
                    self.speak("o que posso fazer para ajudá-lo. mestre")

                elif 'hora' in command:
                    self.speak_time()

                elif 'data' in command:
                    self.speak_date()
                else:
                    asyncio.run(self.chat(command))

            else:
                if 'abrir youtube' in command:
                    self.open_you_tube()

                elif 'abrir chrome' in command:
                    self.open_chrome()
                
                elif 'abrir vscode' in command or 'abrir vs code' in command:
                    self.open_vs_code()

                elif 'desligar' in command or 'sair' in command:
                    self.speak('adeus mestre!.')
                    self.status_window = False
                    self.page.window.close()
                    break

                else:
                    if command != "none":
                        self.speak('comando não encontrado!, tente novamente.')
                