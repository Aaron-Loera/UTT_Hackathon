# backend/main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chat import get_retrieval_chain

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

retrieval_chain = get_retrieval_chain()

class QueryRequest(BaseModel):
    input: str

@app.post("/query")
async def query_chain(req: QueryRequest):
    result = retrieval_chain.invoke({"input": req.input})
    return {"answer": result["answer"]}
