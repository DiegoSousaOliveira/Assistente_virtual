## Assistente Virtual Inteligente 🤖
Essa assistente é capaz de exexuta comandos e responder a perguntas. Eu utilizeu um llm da meta chamado Llama 3.1 que é responsavel por responder as perguntas.

## 🛠️ Tecnologias Utilizadas
 • Flet: Criação de uma interface gráfica amigável para interação.
 • Pyttsx3: Conversão de texto em fala.
 • Speech Recognition: Reconhecimento de voz do usuário.
 • Ollama: Para integrar o modelo Llama 3.1 (4B) da Meta, que responde às 
 perguntas.
 • Pandas: Manipulação e análise de dados.
 • Sklearn: Desenvolvimento e treinamento do modelo de classificação.

## 🧠 Como Funciona?
 1. Treinei um modelo de aprendizado de máquina para classificar frases 
 como "perguntas" ou "comandos".
 • Dados de treinamento: 400 perguntas e 400 comandos em um arquivo 
 CSV.
 2. Quando o usuário fala, o sistema reconhece a entrada e classifica o tipo 
 de frase.
 3. Para perguntas, utilizo o Llama 3.1 (4B) para fornecer respostas.
 4. Para comandos, a assistente executa a ação diretamente.

## Requisitos:
 - Ter o python instalado
 - Ter o Ollama instalado
 - Ter o modelo llama 3.1 instalado

## Etapas para a execução:
 - Baixe o projeto em um arquivo em seu computador.
 - Entre nesse proejto pelo terminal.
 - Crie um ambiente virtual para baixa as dependencias.
 - Ative o ambiente virtual.
 - digite ``pip install requirements.txt`` no termial do projeto.
 - executo o arquivo main.py assim: ``python main.py``
