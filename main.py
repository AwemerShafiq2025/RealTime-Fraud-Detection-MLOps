from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
from prometheus_fastapi_instrumentator import Instrumentator # <-- Nayi Library Import ki

# Initialize FastAPI App
app = FastAPI(
    title="Real-Time Fraud Detection API",
    description="API for detecting fraudulent financial transactions using MLOps.",
    version="1.0.0"
)

# --- NAYA STEP: Prometheus Metrics Expose karna ---
Instrumentator().instrument(app).expose(app)
# --------------------------------------------------

# Load the trained Model and Scaler
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    print("✅ Model and Scaler loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model/scaler: {e}")

# Define the input data format using Pydantic
class TransactionData(BaseModel):
    # Expecting 30 features
    features: list[float]

@app.get("/")
def root():
    return {"message": "Welcome to the Real-Time Fraud Detection API. Go to /docs to test the API."}

@app.post("/predict")
def predict_fraud(data: TransactionData):
    try:
        # Validate feature count
        if len(data.features) != 30:
            raise HTTPException(status_code=400, detail="Expected 30 features.")
        
        # Convert input list to numpy array and reshape for a single prediction
        input_data = np.array(data.features).reshape(1, -1)
        
        # Scale the data using the loaded scaler
        scaled_data = scaler.transform(input_data)
        
        # Make Prediction
        prediction = model.predict(scaled_data)
        
        # Determine the result (0 = Legitimate, 1 = Fraud)
        result = "Fraudulent" if prediction[0] == 1 else "Legitimate"
        
        return {
            "prediction": int(prediction[0]),
            "status": result,
            "message": f"This transaction is {result}."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))