import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
import yaml

def load_params(filepath : str) -> float:
    try:
        with open(filepath,'r') as file:
            params = yaml.safe_load(file)
        return params["data_collection"]["test_size"]
    except Exception as e:
        raise Exception(f"Error loading params from {filepath}")
    
#data = pd.read_csv('./water_potability.csv')
def load_data(filepath : str) -> pd.DataFrame:
    try:
        return pd.read_csv("./water_potability.csv")
    except Exception as e:
        raise Exception(f"Error loading the CSV file from {filepath} : {e}")

#train_data, test_data =train_test_split(data, test_size=0.2, random_state=42)
def split_data(data : pd.DataFrame, test_size : float ) -> tuple[pd.DataFrame,pd.DataFrame] :
    try: 
        return train_test_split(data, test_size=test_size, random_state=42)
    except Exception as e:
        raise Exception(f"Error Occured in Train Test Split : {e}")

#data_path = os.path.join('data','raw')

#os.makedirs('data/raw', exist_ok=True)
#train_data.to_csv(os.path.join(data_path,"train.csv"), index=False)
#test_data.to_csv(os.path.join(data_path,"test.csv"), index=False)

def main():
    data_filepath = "./water_potability.csv"
    params_filepath = "params.yaml"
    raw_data_path = os.path.join('data','raw')

    try:
        data = load_data(data_filepath)
        test_size = load_params(params_filepath)
        train_data,test_data = split_data(data, test_size)

        os.mkdirs(raw_data_path)

        save_data(train_data,os.path.join(raw_data_path,"train.csv"))
        save_data(test_data,os.path.join(raw_data_path,
                                        ))
    except:
        pass