# Prospect-Canadian-Water-Companies
A study on data

## Problem:

It is desired to prospect companies that have solutions in **water treatment**, mainly related to: **solutions on waste and water, Improve water quality and water efficiency use, water contamination, water for human consumption, water resources** .

         a) EXERCISE 1 - Apply an ML algorithm (or a set of them) capable of selecting the main companies indicated to develop the solution according to their alignment with the topic (Justify the choice of the algorithm).

         b) EXERCISE 2 - Carry out an exploratory analysis of the results by adding the other variables contained in the dataset. What insights can you gain from this data? What are the main cities (development hubs) for this solution?


## Files list:

+ 00-DataFIleAdjusts.ipynb                                         - Jupyter Notebook Where data is reformatted and corrected for use in the solution.
+ 01-EDA e Exercicios.ipynb                                        - Jupyter Notebook Where the initial EDA, data inference, algorithm testing for classification, and EDA with all provided and inferred data are implemented.
+ API.py                                                           - FastAPI API for model consumption
+ Planilha em First_Desafio_ciencia_de_dados_SR (1) 1 (1) (2).xlsm - Spreadsheet with data in initial format.
+ lda_visualization.html                                           - LDA Model interactive visualization.
+ best_logistic_regression_model.pkl                               - Logistic Regression Model.
+ tfidf_matrix_restrita.pkl                                        - TF-IDF Matrix used.

## API use:

Server execution: uvicorn APP:appCanadaWater --reload
 API access: http://127.0.0.1:8000
 Swagger access: http://127.0.0.1:8000/docs

 To test:
 curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "description": "Sua descrição aqui"
 }'
