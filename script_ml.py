from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
from azure.ai.ml import MLClient
try:
    credential = DefaultAzureCredential()
    credential.get_token("https://management.azure.com/.default")
except Exception as e:
    print(f"Error using DefaultAzureCredential: {e}")
    credential = InteractiveBrowserCredential()
ml_client = MLClient(
    credential=credential,
    subscription_id="<enter-your-subscription-id>",
    resource_group_name="dio-lab-rg",
    workspace_name="lab-desafio-ws"
)


%%writefile src/vendas_training.py
%%writefile src/vendas_training.py
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import roc_auc_score, roc_curve
from azureml.core import Dataset, Workspace
print("Loading data...")
sorvetes = pd.read_csv("historico.csv")
x, y = sorvetes[['Temperatura']].values, sorvetes[['Vendas']].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
reg = 0.01
print("Training a logistic model with regulariztion rate of ", reg)
model = LinearRegression(C=1/reg, solver='liblinear').fit(x_train, y_train)
y_hat = model.predict(x_test)
acc = np.average(y_hat == y_test)
print("Accuracy: ", acc)
y_score = model.predict(x_test)
auc = roc_auc_score(y_test, y_score[:,1])
print("AUC: ", auc)


from azure.ai.ml import command
job = command(
    code="./src/vendas_training.py",
    command="python vendas_training.py",
    environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu",
    compute="compute-ml-cluster",
    display_name="vendas-training-job",
    experiment_name="vendas-training-experiment"
)
returned_job = ml_client.create_or_update(job)
aml_url = returned_job.studio_url
print(f"Job created with ID: {returned_job.id} Monitoring your job at: {aml_url}")