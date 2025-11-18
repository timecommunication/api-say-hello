from fastapi import FastAPI
from pydantic import BaseModel


class ReqData(BaseModel):
    name: str
    description: str | None = None



app = FastAPI()


@app.post("/say_hello_to_sap")
async def say_hello_to_sap(req_data: ReqData):
    return {'message': f'你好, {req_data.name}, 你的描述是 {req_data.description}'}