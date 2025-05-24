# 🧠 Octavus - Assistente Virtual com IA, Voz e Armazenamento de Interações

Octavus é um assistente virtual pessoal criado em Python que usa reconhecimento de voz, machine learning e comandos SQL para interagir com o usuário e executar tarefas no computador. Ele é capaz de abrir e fechar programas, responder perguntas com voz, enviar mensagens via WhatsApp e **registrar todas as mensagens enviadas em um banco de dados SQL (SQLite)** para fins de histórico ou auditoria.

---

## 🚀 Funcionalidades

- 🎙️ Reconhecimento de voz com `speech_recognition`
- 🗣️ Respostas por voz com `pyttsx3`
- 🤖 Classificação de intenções com `scikit-learn`
- 💬 Respostas baseadas em intenção
- 🖥️ Execução de comandos locais (abrir programas, sites, etc.)
- 📱 Envio de mensagens via WhatsApp com `pywhatkit`
- 🧾 **Registro das mensagens enviadas usando banco de dados SQLite**

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11
- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [scikit-learn](https://scikit-learn.org/)
- [pywhatkit](https://pypi.org/project/pywhatkit/)
- [sqlite3](https://docs.python.org/3/library/sqlite3.html)
- pandas, numpy, joblib, os, time

