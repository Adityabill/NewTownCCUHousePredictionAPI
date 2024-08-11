import joblib
import numpy as np
housePriceModel = joblib.load('housePricePredict.joblib')

def housePricePredict(bhk : int, total_sq_ft : float):

    return housePriceModel.predict(np.array([[bhk, total_sq_ft]]))



a = int(input("Enter BHK:"))
b = float(input("Enter total SQ. Ft of the house:"))

price = housePricePredict(a, b)
print(price[0][0])

