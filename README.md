# Prospect-Canadian-Water-Companies
A study on data

## Problem:

It is desired to prospect companies that have solutions in **water treatment**, mainly related to: **solutions on waste and water, Improve water quality and water efficiency use, water contamination, water for human consumption, water resources** .

         a) EXERCISE 1 - Apply an ML algorithm (or a set of them) capable of selecting the main companies indicated to develop the solution according to their alignment with the topic (Justify the choice of the algorithm).

         b) EXERCISE 2 - Carry out an exploratory analysis of the results by adding the other variables contained in the dataset. What insights can you gain from this data? What are the main cities (development hubs) for this solution?


## Files list:

+ /Docs/Pablo Vigneaux - First_Desafio_ciencia_de_dados_SR.pdf                - Answered questionnaire
+ /00-DataFIleAdjusts.ipynb                                                   - Jupyter Notebook Where data is reformatted and corrected for use in the solution.
+ /01-EDA Transformacoes e Inferencia.ipynb                                   - Jupyter Notebook Where the initial EDA, data inference, and some tests are implemented.
+ /02-Exercicio-01-Modelo.ipynb                                               - Jupyter Notebook Where exercise 01 was implemented, creating a model using text data.
+ /03-Exercicio-02-EDA.zip                                                    - Jupyter Notebook Where exercise 02 was implemented. The final file exceeds 30 MB because this it was compressed.
+ /API.py                                                                     - FastAPI API for model consumption
+ /Dta/Planilha em First_Desafio_ciencia_de_dados_SR (1) 1 (1) (2).xlsm       - Spreadsheet with data in initial format.
+ /Data/lda_visualization.html                                                - LDA Model interactive visualization.
+ /Data/best_logistic_regression_model.pkl                                    - Logistic Regression Model.
+ /Data/tfidf_matrix_restrita.pkl                                             - TF-IDF Matrix used.

## Criação do Ambiente:

conda create -n firstenv python=3.10 nb_conda pylint pip
conda activate firstenv

conda install -c anaconda pandas
conda install -c conda-forge fastparquet
conda install -c anaconda numpy
conda install -c anaconda scipy
conda install -c anaconda scikit-learn
pip install openpyxl
conda install -c conda-forge spacy
python -m spacy download en_core_web_trf
pip install gensim
conda install -c conda-forge matplotlib
conda install -c anaconda seaborn
conda install -c conda-forge plotly
conda install -c plotly plotly_express
conda install -c conda-forge wordcloud

pip install gensim pyLDAvis
pip install imbalanced-learn
pip install fastapi uvicorn
pip install joblib
pip install folium


## API use:

+ Server execution: uvicorn APP:appCanadaWater --reload
+ API access: http://127.0.0.1:8000
+ Swagger access: http://127.0.0.1:8000/docs

+ To test:
 curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "description": "Sua descrição aqui"
 }'
