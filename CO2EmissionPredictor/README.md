# CO2 Emission Predictor

This project uses a dataset of car fuel consumption and technical specs to predict **CO2 emissions** using **Multiple Linear Regression** in Python.

## 📁 Dataset
- `VehicleFuelCO2.csv`

## 🔍 Project Tasks
- Trained multiple linear regression models using two features at a time
- Evaluated performance with MAE, MSE, and R²
- Compared results to a previous model trained on three features

## 📊 Best Performing 2-Feature Model
**Features:** Cylinders + Fuel Consumption  
- MAE: 16.50  
- MSE: 515.45  
- R²: 0.89

## 📉 3-Feature Model (Lecture Comparison)
**Features:** Engine Size + Cylinders + Fuel Consumption  
- MAE: 14.50  
- MSE: 408.38  
- R²: 0.89

## ✅ Conclusion
The three-feature model performs slightly better, especially in MAE and MSE, while both models have the same R² score.
