from typing import Dict, List
from pydantic import BaseModel

class RefInDB(BaseModel):
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


database_refs= Dict[str, RefInDB]

database_refs = {
    "Hotel1": RefInDB(**{"nombre":"Hotel1",
                            "ubicacion":"Colombia",
                            "estrellas":"tres",
                            "totalHabitaciones":30,
                            "sencilla":15,
                            "precioMinSenc":70000,
                            "doble":10,
                            "precioMinDob":100000,
                            "triple":3,
                            "precioMinTrip":130000,
                            "suite":2,   
                            "precioMinSuite":200000,
                            "Tasa":[{"Enero":0.95},
                            {"Febrero":0.78},
                            {"Marzo":0.8},
                            {"Abril":0.6},
                            {"Mayo":0.45},
                            {"Junio":0.55},
                            {"Julio":0.75},
                            {"Agosto":0.65},
                            {"Septiembre":0.4},
                            {"Octubre":0.55},
                            {"Noviembre":0.5},
                            {"Diciembre":0.99}]    }),        
                                            
    "Hotel2": RefInDB(**{"nombre":"Hotel2",
                            "ubicacion":"Colombia",
                            "estrellas":"dos",
                            "totalHabitaciones":12,
                            "sencilla":4,
                            "precioMinSenc":45000,
                            "doble":4,
                            "precioMinDob":75000,
                            "triple":4,
                            "precioMinTrip":110000,
                            "suite":0,   
                            "precioMinSuite":0,
                            "Tasa":[{"Enero":0.88},
                            {"Febrero":0.8},
                            {"Marzo":0.75},
                            {"Abril":0.5},
                            {"Mayo":0.5},
                            {"Junio":0.48},
                            {"Julio":0.7},
                            {"Agosto":0.6},
                            {"Septiembre":0.3},
                            {"Octubre":0.38},
                            {"Noviembre":0.48},
                            {"Diciembre":0.88}] }),
    "Hotel3": RefInDB(**{"nombre":"Hotel3",
                            "ubicacion":"Colombia",
                            "estrellas":"cinco",
                            "totalHabitaciones":40,
                            "sencilla":15,
                            "precioMinSenc":150000,
                            "doble":15,
                            "precioMinDob":250000,
                            "triple":5,
                            "precioMinTrip":320000,
                            "suite":5,   
                            "precioMinSuite":450000,
                            "Tasa":[{"Enero":0.88},
                            {"Febrero":0.8},
                            {"Marzo":0.75},
                            {"Abril":0.5},
                            {"Mayo":0.5},
                            {"Junio":0.48},
                            {"Julio":0.7},
                            {"Agosto":0.6},
                            {"Septiembre":0.3},
                            {"Octubre":0.38},
                            {"Noviembre":0.48},
                            {"Diciembre":0.88}]          
                                            }),
}

def get_referencia(nombre: str): # Busqueda
    if nombre in database_refs.keys():
        return database_refs[nombre]
    else:
        return None

def get_temporada(nombre: str, mes: str):
    ref_in_db=get_referencia(nombre)
    