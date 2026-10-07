from fastapi import FastAPI

app = FastAPI(title="DeployGuard")


@app.get("/")
def home():
    return {
        "project": "DeployGuard",
        "message": "Deployment Risk & Rollback Assistant",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }