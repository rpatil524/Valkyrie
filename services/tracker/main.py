from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    """
    Health check to ensure that the tracker service is running.

    Usage:
    curl -X GET http://<endpoint>/health

    Returns:
    {
        "status": "ok"
    }

    Returns:
    - 200 OK if the server is running
    - 500 Internal Server Error if the server is not running
    """
    return {"status": "ok"}
