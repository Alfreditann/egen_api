from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
 
app = FastAPI(title="HP quote")
 
sitater = {
    1: "Yare yare daze.",
    2: "I, Giorno Giovanna, have a dream.",
    3: "You thought it was someone else, but it was me, Dio!",
    4: "Your next line is: 'What?!'",
    5: "MUDA MUDA MUDA!",
    6: "ORA ORA ORA!",
    7: "This must be the work of an enemy Stand!",
    8: "Good grief...",
    9: "WRYYYY!",
    10: "The Joestar bloodline will not fall so easily."
}
 
class GetQuote(BaseModel):
    quote: str
 
@app.get("/sitat",response_model=GetQuote)
def sitat():
    id = random.randint(1,len(sitater))
    return {"quote":sitater[id]}