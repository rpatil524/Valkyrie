from fastapi import FastAPI, File, HTTPException, UploadFile
from tracker.s3 import upload_to_s3

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


@app.post("/upload")
async def upload_agent(
    agent: UploadFile = File(..., description="Agent submodule zip file"),
    contract: UploadFile = File(..., description="AgentContract python file"),
):
    """
    Upload agent and contract to S3.

    Usage:
    curl -X POST http://<endpoint>/upload \
      -F "agent=@agent.zip" \
      -F "contract=@contract.py"

    Returns:
    {
        "status": "success",
        "message": "Agent and contract uploaded successfully"
    }

    Returns:
    - 200 OK if upload succeeds
    - 400 Bad Request if files are invalid
    - 500 Internal Server Error if upload fails
    """
    # TODO: More robust validation.
    # Perhaps run some kind of test script to make sure implementation is correct
    if not agent.filename or not agent.filename.endswith(".zip"):
        raise HTTPException(status_code=400, detail="Agent must be a zip file")

    if not contract.filename or not contract.filename.endswith(".py"):
        raise HTTPException(status_code=400, detail="Contract must be a Python file")

    try:
        # Read file contents
        agent_content = await agent.read()
        contract_content = await contract.read()

        # TODO: better keys so that contracts and agents with same names don't collide
        agent_s3_key = f"agents/{agent.filename}"
        contract_s3_key = f"contracts/{contract.filename}"

        upload_to_s3(agent_content, agent_s3_key)
        upload_to_s3(contract_content, contract_s3_key)

        return {
            "status": "success",
            "message": "Agent and contract uploaded successfully",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")
