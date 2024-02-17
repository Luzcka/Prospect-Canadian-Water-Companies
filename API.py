# Para executar o servidor: uvicorn APP:appCanadaWater --reload
# Para acessar a API: http://127.0.0.1:8000
# Para acessar o Swagger: http://127.0.0.1:8000/docs

# Para testar:
#curl -X 'POST' \
#  'http://127.0.0.1:8000/predict/' \
#  -H 'accept: application/json' \
#  -H 'Content-Type: application/json' \
#  -d '{
#  "description": "Sua descrição aqui"
#}'


from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer



ROOT_DIR = Path().absolute()
SOURCE_SUBDIR = 'Data'


# Classe para o corpo da solicitação
class Item(BaseModel):
    description: str

# Carregar o modelo treinado e o vetorizador
model = joblib.load(ROOT_DIR / SOURCE_SUBDIR / "best_logistic_regression_model.pkl")
vectorizer = joblib.load(ROOT_DIR / SOURCE_SUBDIR / "tfidf_matrix_restrita.pkl")


appCanadaWater = FastAPI()

@appCanadaWater.post("/predict/")
def predict(item: Item):
    # Vetorizar a descrição recebida
    description_vect = vectorizer.transform([item.description])
    
    # Fazer a previsão usando o modelo carregado
    prediction = model.predict(description_vect)
    
    # Mapear a previsão numérica para o rótulo correspondente
    label_map = {0: "Menos relevante", 1: "Não relevante", 2: "Relevante"}
    predicted_label = label_map[prediction[0]]

    return {"prediction": predicted_label}