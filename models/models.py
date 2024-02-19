import pickle
import pandas as pd


with open('venv/models/predictcarprice.pkl', 'rb') as f:
    load_ml_pipeline = pickle.load(f)


def prediction(values):
    df = pd.DataFrame(data=values, 
             columns=['Year','Drivetrain','Transmission','Fuel Type','Max Power','Fuel Tank Capacity'])
    

    pred = load_ml_pipeline.predict(df)
    return pred[0]