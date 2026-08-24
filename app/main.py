from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="DevOps Health API",
    description="A production-style API demonstrating DevOps practices.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "service": "devops-health-api",
        "status": "running",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "devops-health-api"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0",
        "environment": "production"
    }
