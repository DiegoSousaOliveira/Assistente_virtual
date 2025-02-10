import asyncio
import pyttsx3
from ollama import AsyncClient

engine = pyttsx3.init()

speech_queue: list[str] = []

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Função assíncrona de chat
async def chat(question: str):
    message = {
        'role': 'user', 
        'content': f'responda esse pergunta "{question}" de forma resumida e objetiva'}

    word_accumulator = ''
    async for part in await AsyncClient().chat(model='llama3.1', messages=[message], stream=True):
        content = part['message']['content']
        word_accumulator += content
        if word_accumulator.endswith('.') or word_accumulator.endswith(','):
            speak(word_accumulator.replace('*', ''))
            speech_queue.append(word_accumulator)
            word_accumulator = ''

if __name__ == '__main__':
    asyncio.run(chat('O que é python?'))
    