# Octavus - Assistente Virtual com Machine Learning 🇧🇷🧠💬

O **Octavus** é um assistente virtual em português que entende sua voz, responde com fala sintetizada e realiza ações no seu computador, tudo isso utilizando **Machine Learning**, **Reconhecimento de Fala**, **Text-to-Speech** e integração com **WhatsApp**. É como ter uma IA pessoal rodando localmente!

> ⚠️ **Aviso:** As funcionalidades de envio de mensagens via WhatsApp e registro no banco de dados SQLite estão temporariamente desativadas.

---

## 🚀 Visão Geral

O Octavus:

- Escuta comandos de voz pelo microfone.
- Usa **Google Speech Recognition** para transcrever o áudio.
- Utiliza um modelo de ML para identificar a intenção do comando.
- Gera uma resposta com base na intenção detectada.
- Executa ações como abrir apps ou responder com fala.
- Usa a **Google Cloud Text-to-Speech** para sintetizar a resposta.
- (Opcional) Envia mensagens via WhatsApp e salva no banco (atualmente desativado).

---

## 🧠 Estrutura e Funcionamento

### Arquivo principal: `octavus.py`

- Reconhecimento de fala com `speech_recognition`
- Fala sintetizada com `google.cloud.texttospeech`
- Reprodução de áudio com `pydub`
- Modelos de ML carregados com `joblib`
- Integração com banco de dados (`database.py`)
- Configuração de `ffmpeg` e chave JSON do Google


## 📌 Requisitos

- Python 3.8+
- `speech_recognition`, `pydub`, `google-cloud-texttospeech`, `joblib`, `pywhatkit`, etc.
- **FFmpeg** (necessário para reprodução de áudio com `pydub`)

---

## ⚙️ Como instalar o FFmpeg

O FFmpeg é uma ferramenta essencial para manipulação e reprodução de áudio. Você precisa baixar e configurar ele para que o Octavus funcione corretamente.

1. Baixe o FFmpeg no site oficial: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

2. Escolha a versão para o seu sistema operacional (Windows, Linux, Mac).

3. Extraia o conteúdo para uma pasta no seu computador (ex: `C:\ffmpeg` no Windows).

4. Adicione o caminho da pasta `bin` do FFmpeg à variável de ambiente PATH do seu sistema:

   - No Windows:  
     Vá em **Painel de Controle > Sistema > Configurações Avançadas > Variáveis de Ambiente**  
     Edite a variável `PATH` e adicione algo como:  
     `C:\ffmpeg\bin`

   - No Linux/Mac:  
     Adicione a linha abaixo no seu `.bashrc` ou `.zshrc`:  
     ```bash
     export PATH=$PATH:/caminho/para/ffmpeg/bin
     ```

5. Reinicie o terminal/PC para as alterações entrarem em vigor.
