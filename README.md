# 🧠 Octavus - Assistente Virtual com IA, Voz e Histórico

Octavus é um assistente virtual pessoal desenvolvido em Python, que utiliza técnicas de reconhecimento de voz, machine learning e banco de dados para interagir de forma inteligente e prática com o usuário.  

Com ele, você pode controlar seu computador por comandos de voz, enviar mensagens via WhatsApp, e acompanhar um histórico detalhado das interações, tudo de forma automatizada e eficiente.

---

## 🚀 Funcionalidades Principais

- 🎙️ **Reconhecimento de voz** com `speech_recognition` para captar comandos do usuário em tempo real.  
- 🗣️ **Resposta por voz** usando `pyttsx3`, que oferece feedbacks naturais e interativos.  
- 🤖 **Classificação de intenções** por meio de machine learning (scikit-learn), permitindo entender e responder corretamente diferentes tipos de comandos.  
- 💬 **Respostas dinâmicas** baseadas na intenção reconhecida, tornando a interação fluida e contextual.  
- 🖥️ **Execução de comandos locais**, como abrir programas, sites e arquivos no computador.  
- 📱 **Envio de mensagens via WhatsApp** usando a biblioteca `pywhatkit`, para comunicação rápida e prática.  
- 🧾 **Armazenamento das mensagens e comandos** em banco de dados SQLite, garantindo histórico para auditoria e análise posterior.  

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11  
- `speech_recognition` — captura e interpretação de áudio.  
- `pyttsx3` — síntese de voz offline para respostas faladas.  
- `scikit-learn` — machine learning para classificação de intenções.  
- `pywhatkit` — automação do envio de mensagens via WhatsApp.  
- `sqlite3` — banco de dados leve para armazenar histórico de interações.  
- Bibliotecas auxiliares: `pandas`, `numpy`, `joblib`, `os`, `time`.  

---

## 💻 Como usar

1. Clone o repositório:  
```bash
git clone https://github.com/VictorAraujopy/Octavus.git


🎯 Próximos passos (em desenvolvimento)
Aprimorar o reconhecimento de voz para maior precisão em ambientes ruidosos.

Implementar novas funcionalidades como controle de dispositivos IoT e integração com APIs externas.

Criar interface gráfica para facilitar o uso por usuários não técnicos.

