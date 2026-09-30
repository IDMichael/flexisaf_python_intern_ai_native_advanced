from fastapi import FastAPI

app = FastAPI(
    title="Agent-Ready Backend Service",
    description="A minimal backend used to demonstrate the AI-native engineering lifecycle.",
    version="1.0.0",
)

@app.get("/")
def root():
    """Return a simple API health message."""
    return {"message": "AI-Native Week 1 API is running."}

@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the service health status."""
    return {"status": "healthy"}
