from fastapi import FastAPI, Request, Header, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class CallbackData(BaseModel):
    task_id: str
    status: int
    tagged_as: Optional[str] = None
    validation_message: Optional[str] = None

@app.post("/api/v1/testcallback")
async def test_callback(
    data: CallbackData,
    authorization: str = Header(...)
):
    expected_token = "4f8a9d7fbd34c89ea234fa27fbd1c03baf7a7dc6e12f85c3c770a49c3d5e4ccf"
    if not authorization.startswith("Bearer ") or authorization.split(" ")[1] != expected_token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {
        "message": "Callback received successfully",
        "received_data": data
    }
