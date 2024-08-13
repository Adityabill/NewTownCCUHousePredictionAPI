from fastapi import FastAPI
import joblib
import numpy as np
import uvicorn

app = FastAPI()

housePriceModel = joblib.load('housePricePredict.joblib')

@app.get("/")
def readRoot():
    return {"Message": "Hello World!"}

@app.get("/{bhk}/{total_sq_ft}")
def predictHousePrice(bhk : int, total_sq_ft: float):
    price = housePriceModel.predict(np.array([[bhk, total_sq_ft]]))
    return {'housePrice' : round(price[0][0])}

if __name__ == '__main__':
    uvicorn.run(app, '127.0.0.1', port=8000)