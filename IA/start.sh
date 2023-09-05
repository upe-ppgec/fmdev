#! /bin/bash

python -m venv venv
source venv/bin/activate

pip install kaleido matplotlib numpy pandas plotly plotly.express scikit-learn scipy seaborn

python outliers_agrupamento_Visu.py
