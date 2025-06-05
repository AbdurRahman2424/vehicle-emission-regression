import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def train_and_evaluate(features, label, test_size=0.2, random_state=2):
    trn_X, tst_X, trn_y, tst_y = train_test_split(features, label, test_size=test_size, random_state=random_state)

    regr = LinearRegression()
    regr.fit(trn_X, trn_y)
    y_hat = regr.predict(tst_X)

    return {
        "intercept": regr.intercept_,
        "coefficients": regr.coef_,
        "mae": mean_absolute_error(tst_y, y_hat),
        "mse": mean_squared_error(tst_y, y_hat),
        "r2": r2_score(tst_y, y_hat)
    }
