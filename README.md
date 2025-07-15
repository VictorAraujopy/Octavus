Octavus - Assistente Virtual com Machine Learning
Este projeto é um assistente virtual em português, que utiliza reconhecimento de voz, síntese de fala e machine learning para entender e responder comandos, além de executar ações no computador e enviar mensagens via WhatsApp.

Visão geral do funcionamento
O Octavus é uma assistente pessoal que:

Escuta comandos de voz pelo microfone.

Reconhece a fala usando a API do Google ou Google Speech Recognition.

Identifica a intenção do comando usando um modelo de machine learning treinado.

Gera uma resposta apropriada usando um modelo de respostas baseado na intenção.

Executa ações específicas no computador conforme o comando (ex: abrir apps, enviar mensagens).

Responde por voz com áudio sintetizado pela Google Text-to-Speech.

Registra mensagens enviadas num banco de dados SQLite local.

Estrutura do código principal (octavus.py)
Importações e configurações
Usa speech_recognition para captar voz.

Google Cloud Text-to-Speech para sintetizar áudio.

pydub para tocar arquivos MP3 gerados.

Modelos de ML carregados com joblib (modelo_octavus.pkl e resp_noa.pkl).

Banco SQLite acessado via módulo database.py.

Configuração do caminho do ffmpeg e variável de ambiente para o JSON da API.

Contatos
Dicionário com nomes e números para envio automático de mensagens via WhatsApp.

python
Copier
Modifier
contatos = {
    "namorada": "+55 11 98945-9610", 
    "tati": "+55 11 96303-9889",
    "gps": "+55 11 99453-2056",
}
Funções principais
oc_fala(texto)
Recebe uma string de texto.

Converte texto em fala usando Google Text-to-Speech.

Salva o áudio em MP3 temporário.

Reproduz o áudio com pydub.

Remove o arquivo temporário.

ouvir_comando()
Escuta o microfone com ajuste de ruído ambiente.

Converte áudio em texto (reconhecimento de fala).

Retorna o texto convertido ou string vazia em caso de erro.

identificar_intencao(comando)
Recebe texto do comando.

Usa modelo de ML para prever a intenção da frase.

Retorna a intenção como string (ex: "abrir_spotify", "enviar_mensagem").

obter_resposta(intencao)
Recebe a intenção prevista.

Usa outro modelo para gerar respostas possíveis.

Seleciona uma resposta com base em probabilidades, para variar as respostas.

Retorna uma resposta em texto.

processar_comando_mensagem(comando)
Detecta se o comando é para enviar mensagem via WhatsApp.

Extrai destinatário e mensagem usando regex.

Envia a mensagem com pywhatkit.

Registra a mensagem no banco de dados.

Retorna confirmação ou mensagem de erro.

Loop principal (iniciar_oc())
Dá uma mensagem inicial de boas-vindas.

Entra em loop infinito:

Escuta o comando do usuário.

Identifica a intenção.

Se for conhecida:

Gera uma resposta.

Executa a ação correspondente (abrir app, fechar app, enviar mensagem).

Responde por voz.

Se for desconhecida, ignora.

Finaliza se o comando for para encerrar a conversa.

Outros arquivos
database.py
Cria e conecta a um banco SQLite local octavus.db.

Cria tabela para armazenar mensagens enviadas.

Função para registrar destinatário, número, mensagem e data/hora do envio.

treinamento_intencao.py
Treina modelo de machine learning para classificação das intenções.

Usa pipeline com CountVectorizer + MultinomialNB.

Separa dados em treino e teste (80/20).

Salva modelo treinado em modelo_octavus.pkl.

respostas_training.py
Treina modelo para gerar respostas baseadas na intenção.

Usa pipeline com TfidfVectorizer + MultinomialNB.

Usa LabelEncoder para codificar respostas.

Salva pipeline e encoder em resp_noa.pkl.

Fluxo completo da assistente
Usuário fala pelo microfone.

Texto é extraído via reconhecimento de voz.

Texto é passado para modelo de intenções.

Intenção identificada é passada para modelo de respostas.

Resposta gerada é falada para o usuário.

Se intenção envolver ação (ex: abrir app, enviar mensagem), a ação é executada.

Se enviar mensagem, registra no banco SQLite.

