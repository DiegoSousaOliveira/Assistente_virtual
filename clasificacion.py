import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Carregar os dados do arquivo CSV
file_path = 'modified_questions.csv'
df = pd.read_csv(file_path)

# Dividir os dados em textos e rótulos
texts = df['text'].values
labels = df['label'].values

# Dividindo os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.3, random_state=42)

# Convertendo o texto para uma representação TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Treinando o modelo de classificação
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Realizando previsões
y_pred = model.predict(X_test_tfidf)


# Matriz de Confusão
conf_matrix = confusion_matrix(y_test, y_pred)

# Função para classificar um novo texto
def classify_text(new_text):
    # Transformando o texto para TF-IDF
    new_text_tfidf = vectorizer.transform([new_text])
    # Classificando o texto
    prediction = model.predict(new_text_tfidf)
    return prediction[0]

if __name__ == '__main__':
    # Avaliando o modelo
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # Teste de classificação de um novo texto
    novo_texto = "O que é um analista de sistema"
    classe_prevista = classify_text(novo_texto)
    print(f"O texto '{novo_texto}' foi classificado como: {classe_prevista}")