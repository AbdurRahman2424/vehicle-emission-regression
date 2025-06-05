# 🚗 CO₂ Emission Predictor

This project applies **Multiple Linear Regression** to predict CO₂ emissions from vehicles using a dataset of fuel consumption and engine specifications.

## 📂 Dataset

* File used: `VehicleFuelCO2.csv`
* Includes features like Engine Size, Number of Cylinders, Fuel Consumption, and CO₂ Emissions.

## 🛠️ Project Overview

* Built multiple linear regression models using **two features at a time**.
* Assessed model performance using:

  * **MAE** (Mean Absolute Error)
  * **MSE** (Mean Squared Error)
  * **R² Score** (Coefficient of Determination)
* Compared results with a **three-feature model** developed earlier in class.

## 📊 Best 2-Feature Model

**Features:** Cylinders + Fuel Consumption

* **MAE:** 16.50
* **MSE:** 515.45
* **R² Score:** 0.89

## 📉 3-Feature Model (from Lecture)

**Features:** Engine Size + Cylinders + Fuel Consumption

* **MAE:** 14.50
* **MSE:** 408.38
* **R² Score:** 0.89

## ✅ Conclusion

While both models show the same **R² score**, the three-feature model slightly outperforms the two-feature model in terms of **MAE** and **MSE**, indicating more accurate predictions.

---
