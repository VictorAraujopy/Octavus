import random

# Dicionário de respostas por intenção
respostas = {
    "abrir_spotify": [
        "abrindo spotify",
        "ok musica a caminho",
        "bora ouvir um som",
        "entendido vou iniciar o spotify",
        "spotify em processo de execução",
        "vou tocar sua playlist agora",
        "abrindo seu som favorito",
        "ligando o spotify pra você",
        "preparando sua musica",
        "ja estou abrindo o spotify"
    ],
    "fechar_spotify": [
        "fechando player de música",
        "saindo do spotify",
        "interrompendo sua música",
        "parando spotify",
        "ok encerrando o spotify",
        "encerrando player agora",
        "desligando o som",
        "sua musica foi interrompida",
        "spotify finalizado"
    ],
    "abrir_red": [
        "jogo de faroeste a caminho",
        "começando a diversão",
        "red dead redemption dois iniciando",
        "executando red dead",
        "abrindo red dead",
        "red dead em execução",
        "vou iniciar o jogo de faroeste",
        "preparando red dead pra você",
        "jogo red dead começando",
        "ligando o jogo de velho oeste"
    ],
    "fechar_red": [
        "saindo do jogo",
        "gameplay encerrada",
        "acabando com a diversão agora",
        "ok fechando red dead redemption dois",
        "fechando o red dead",
        "red dead encerrado",
        "jogo finalizado",
        "encerrando red dead",
        "desligando o jogo",
        "finalizando gameplay de faroeste"
    ],
    "enviar_mensagem": [
        "mensagem a caminho",
        "enviando mensagem",
        "ok irei enviar",
        "abrindo WhatsApp",
        "preparando envio",
        "vou mandar a mensagem agora",
        "escrevendo sua mensagem",
        "entendido vou enviar",
        "mensagem pronta para envio",
        "mandando agora"
    ],
    "encerrar_conversa": [
        "encerrando atividades",
        "até logo",
        "tchau até mais",
        "desligando",
        "finalizando bate papo",
        "te vejo mais tarde",
        "conversa encerrada",
        "estou indo nessa",
        "foi bom falar com você",
        "estou saindo agora"
    ]
}

def obter_resposta(intencao):
    
    return random.choice(respostas.get(intencao, ["Desculpe, não entendi o que você quer."]))
