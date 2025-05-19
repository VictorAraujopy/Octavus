import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
import joblib

# Carrega os dados de respostas
dados_respostas = pd.read_csv(r"C:\Users\vicit\Desktop\projeto octavus\respostas.csv")

# Pré-processamento
dados_respostas['resposta'] = dados_respostas['resposta'].str.lower().str.strip()

# Cria um encoder para as respostas
encoder_resposta = LabelEncoder()
y_encoded = encoder_resposta.fit_transform(dados_respostas['resposta'])

# Pipeline aprimorado
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1, 2))),  # Captura combinações de palavras (intenção)
    ('clf', MultinomialNB(alpha=0.5))                # treina o modelo
])

# Treina com todas as frases de cada intenção
X = dados_respostas['intencao']  # Usamos a intenção como entrada
y = y_encoded

pipeline.fit(X.astype(str), y)

# Salva o pipeline e o encoder
joblib.dump((pipeline, encoder_resposta), "resp_noa.pkl")
print("Modelo de respostas treinado!")