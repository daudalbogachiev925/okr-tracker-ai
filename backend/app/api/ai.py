from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.llm import generate_key_results

router = APIRouter()

class OKRRequest(BaseModel):
    objective: str

@router.post("/generate-kr")
def generate(req: OKRRequest):
    if not req.objective.strip():
        raise HTTPException(400, "Objective required")
    try:
        return {"key_results": generate_key_results(req.objective)}
    except Exception as e:
        raise HTTPException(500, str(e))
