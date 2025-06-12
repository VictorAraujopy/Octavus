import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib




dados = pd.read_csv(r"C:\Users\vicit\Desktop\projeto octavus\intencoes.csv")  #le o arquivo csv


x = dados["frase"]
y = dados["intencao"]
#divide os x e o y do ml em frase e intencao no .csv x sendo os dados de entrada e y os dados q o modelo vai tentar prever



x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.2, random_state=42) # divide a fase de treino e de teste da ia em 80\20

modelo = make_pipeline(CountVectorizer(), MultinomialNB())
#transforma as palavras em numeros e o multinomial relaciona palavras em frases diferentes tipo se tiver abrir ou spotify em qlqr frase ele vai executar o comando

modelo.fit(x_treino, y_treino)
#aqui ele treina

y_pred = modelo.predict(x_teste)
#aqui ele testa


print(classification_report(y_teste, y_pred))
#me mostra o desempenho


joblib.dump(modelo, "modelo_octavus.pkl")
print("modelo treinado e salvo" )