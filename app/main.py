from fastapi import FastAPI
from datetime import datetime
import time

app = FastAPI(title="DeployGuard")

START_TIME = time.time()


@app.get("/")
def home():
    return {
        "project": "DeployGuard",
        "message": "Deployment Risk & Rollback Assistant",
        "status": "running"
    }


@app.get("/health")
def health():
    uptime = round(time.time() - START_TIME, 2)

    return {
        "status": "healthy",
        "uptime_seconds": uptime,
        "timestamp": datetime.utcnow().isoformat()
    }