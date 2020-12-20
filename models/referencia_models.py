from pydantic import BaseModel
from typing import Dict, List

class RefIn(BaseModel):
    nombre:str

class RefOut(BaseModel):
    nombre:str
    ubicacion:str
    estrellas:str
    totalHabitaciones:int
    sencilla:int
    precioMinSenc:int
    doble:int
    precioMinDob:int
    triple:int
    precioMinTrip:int
    suite:int
    precioMinSuite:int
    Tasa:List[Dict[str, float]]
