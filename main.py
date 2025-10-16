from fastapi import FastAPI    #framework
from pydantic import BaseModel   #authentication when api call
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id:int
    name:str
    origin:str

teas: List[Tea] = []

@app.get("/")
def read_root():
    return {"message" : "Welcome to tea house"}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_teas(tea : Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id : int, updated_tea : Tea):
    for index , tea in enumerate(teas):
        if tea.id ==tea_id:
            teas[index] = updated_tea
            return update_tea
    return {"error" : "tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id :int):
    for index ,tea in enumerate(teas):
        if tea.id == tea_id:
            deleted_tea=teas.pop(index)
            return deleted_tea  
    return  {"error" : "tea not found"}


