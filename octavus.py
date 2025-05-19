import speech_recognition as sr
from google.cloud import texttospeech
import os
from pydub import AudioSegment
from pydub.playback import play
import uuid
import subprocess
import time
from joblib import load
import numpy as np
import pywhatkit as kit  
from database import tabela, registrar
import re
from respostas_OC import obter_resposta


tabela()
contatos = {
    "namorada": "+55 11 98945-9610", 
    "tati": "+55 11 96303-9889",
    "gps": "+55 11 99453-2056",
     
}


# Carrega modelos e encoders
modelo_intencoes = load("modelo_octavus.pkl")      # classificador de intenções

# Configura caminho do ffmpeg
os.environ["PATH"] += os.pathsep + r"C:\Users\vicit\Desktop\ffmpeg-7.1.1-essentials_build\bin"
AudioSegment.converter = r"C:/Users/vicit/Desktop/ffmpeg-7.1.1-essentials_build/bin/ffmpeg.exe"
AudioSegment.ffprobe = r"C:/Users/vicit/Desktop/ffmpeg-7.1.1-essentials_build/bin/ffprobe.exe"

# Configuração da chave da API Google
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\vicit\Desktop\projeto octavus\key.json"

print("octavus iniciando...")

reconhedor = sr.Recognizer()

# Função para ocavusfalar
def oc_fala(texto):
    print(f"OC:{texto}")
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=texto)
    voice = texttospeech.VoiceSelectionParams(language_code='pt-BR', ssml_gender=texttospeech.SsmlVoiceGender.MALE)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)
    nome_arquivo = f"saida_{uuid.uuid4().hex}.mp3"
    with open(nome_arquivo, "wb") as out:
        out.write(response.audio_content)
    time.sleep(1)
    audio = AudioSegment.from_mp3(nome_arquivo)
    play(audio)
    os.remove(nome_arquivo)

# Função para ouvir comando
def ouvir_comando():
    with sr.Microphone() as fonte:
        reconhedor.adjust_for_ambient_noise(fonte, duration=0.5)
        reconhedor.pause_threshold = 1.2
        print("ouvindo...")
        audio = reconhedor.listen(fonte)
    try:
        comando = reconhedor.recognize_google(audio, language='pt-BR')
        comando = comando.lower()
        print(f"você disse:{comando}")
        if len(comando.strip()) < 2:
            return ""
        return comando
    except sr.UnknownValueError:
        return ''
    except sr.RequestError:
        oc_fala('erro ao se conectar com o serviço de reconhecimento')
        return ''

# Função para identificar intenção usando o modelo de intenções
def identificar_intencao(comando):
    if not comando:
        return "desconhecido"
    
    # Previsão retorna a string da intenção diretamente
    return modelo_intencoes.predict([comando])[0]



    

def processar_comando_mensagem(comando):
    padrao = r"envi(?:ar|a) mensagem (?:para|pra) (\w+)(?: (?:dizendo|falando))? (.+)"

    match = re.search(padrao, comando.lower())
    
    if match:
        nome = match.group(1)  
        mensagem = match.group(2)  
        
        if nome in contatos:
            numero = contatos[nome]
            hora = time.localtime().tm_hour
            minuto = time.localtime().tm_min + 1
            if minuto >= 60:
                minuto = 0
                hora = (hora + 1) % 24
            try:
                kit.sendwhatmsg_instantly(
    numero,           # número no formato "+55XXXXXXXXXXX"
    mensagem,         # texto da mensagem
    wait_time=10,     # segundos para aguardar o carregamento da página antes de digitar
    tab_close=True,   # fecha a aba após o envio
    close_time=3      # segundos para aguardar antes de fechar a aba
)
                registrar(nome, numero, mensagem)
                return f"Mensagem enviada para {nome} com sucesso!"
            except Exception as e:
                return f"Ocorreu um erro ao enviar: {str(e)}"
        else:
            return f"Contato {nome} não encontrado."
    else:
        return "Formato inválido. Diga: enviar mensagem para [nome] dizendo [mensagem]."
        

# Função principal modificada
def iniciar_oc():
    oc_fala('Sou o Octavus, projeto pessoal do Victor. Como posso ajudar?')
    while True:
        comando = ouvir_comando()
        intencao = identificar_intencao(comando)
        
        if intencao != 'desconhecido':
            # Gera resposta usando o novo método
            resposta = obter_resposta(intencao)
            oc_fala(resposta)
            
            # Executa ações
            if intencao == "encerrar_conversa":
                break
            elif intencao == 'fechar_spotify':
                subprocess.run(['taskkill', '/im', 'Spotify.exe', '/f'], shell=True)
            elif intencao == 'abrir_spotify':
                subprocess.Popen(r"C:\Users\vicit\AppData\Local\Microsoft\WindowsApps\Spotify.exe", shell=True)
            elif intencao == 'fechar_red':
                subprocess.run(['taskkill', '/im', 'RDR2.exe', '/f'], shell=True)
            elif intencao == 'abrir_red':
                subprocess.Popen(r"D:\Red Dead Redemption 2\RDR2.exe", shell=True)

            elif intencao == 'enviar_mensagem':
                 resposta = processar_comando_mensagem(comando)
                 oc_fala(resposta)
        else:
            print('comando desconhecido')

if __name__ == "__main__":
    iniciar_oc()

