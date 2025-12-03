from fastapi import FastAPI

app = FastAPI(title="Predict API")

@app.get("/health")
async def health():
   
    return {"status": "ok"}

@app.get("/predict")
async def predict():
    
    return {"score": 0.75}

