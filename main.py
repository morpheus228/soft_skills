import pickle
from fastapi import Depends, FastAPI, Request, HTTPException, Response
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import joblib
import uvicorn

from schemas import RequestBody


app = FastAPI()


encoders = {}
for label in ["lesson", "color", "relax", "happy", "angry", "bad_people", "can_not_forgive", "music", "weak_skill", "sphere", "result"]:
    with open(f'encoders/{label}_encoder.pickle', 'rb') as f:
        encoders[label] = pickle.load(f)


model = joblib.load('model.pkl')


def predict(data: dict) -> str:
    df = pd.DataFrame([data])

    for column in df.columns:
        df[column] = encoders[column].transform(df[column])
    
    print(df)
    
    prediction = np.round(model.predict(df)).astype(int)
    predicted_lesson = encoders['lesson'].inverse_transform(prediction)[0]
    return predicted_lesson


@app.post('/predict')
def predict_handler(body: RequestBody):
    prediction = predict(body.dict())
    return {'result': prediction}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, port=80)
