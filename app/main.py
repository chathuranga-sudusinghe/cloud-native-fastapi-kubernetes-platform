from fastapi import FastAPI

app = FastAPI(
    title="Cloud-Native FastAPI Platform",
    version="1.0.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "service": "cloud-native-fastapi-kubernetes-platform",
        "status": "running",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
    }