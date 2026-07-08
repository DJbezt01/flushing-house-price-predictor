# Flushing Queens House Price Predictor
A machine learning API that predicts residential property sale prices in Flushing, Queens NYC using real data from NYC Open Data.

## Tech Stack
- Python, pandas, scikit-learn
- FastAPI, Uvicorn
- NYC Open Data API

## How to Run
1. Install dependencies: `pip install fastapi uvicorn scikit-learn pandas joblib numpy`
2. Start the API: `uvicorn main:app --reload --port 8080`
3. Open `http://localhost:8080/docs`

## Example Request
POST `/predict`
```json
{
  "gross_square_feet": 1200,
  "land_square_feet": 2500,
  "year_built": 1955,
  "residential_units": 1
}
```
