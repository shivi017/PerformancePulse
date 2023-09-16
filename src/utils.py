import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        print("Current Working Directory:", os.getcwd())
        print("Files in Directory:", os.listdir(os.getcwd()))

    except Exception as e:
        raise CustomException(str(e), sys.exc_info())
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(str(e), sys.exc_info())
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            
            # Load the object from the file
            loaded_object = pickle.load(file_obj)
        return loaded_object
    except FileNotFoundError as e:
        raise CustomException(f"File not found: {file_path}", sys.exc_info())
    except Exception as e:
        raise CustomException(f"Error loading object from file: {str(e)}", sys.exc_info())