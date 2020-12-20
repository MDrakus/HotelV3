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

class TocProm(BaseModel):
    nombre:RefInDB
    Enero:float
    Febrero:float
    Marzo:float
    Abril:float
    Mayo:float
    Junio:float
    Julio:float
    Agosto:float
    Septiembre:float
    Octubre:float
    Noviembre:float
    Diciembre:float


database_refs= Dict[str, TocProm]

database_refs = {
    "HotelReferencia1":TocProm(**{"Hotel1": RefInDB(**{"nombre":"Hotel1",
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
                            "precioMinSuite":200000,}),
                            "Enero":0.95,
                            "Febrero":0.78,
                            "Marzo":0.8,
                            "Abril":0.6,
                            "Mayo":0.45,
                            "Junio":0.55,
                            "Julio":0.75,
                            "Agosto":0.75,
                            "Septiembre":0.4,
                            "Octubre":0.5,
                            "Noviembre":0.5,
                            "Diciembre":0.99,           
                                            }),
    "HotelReferencia2":TocProm(**{"Hotel2": RefInDB(**{"nombre":"Hotel2",
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
                            "precioMinSuite":0,}),
                            "Enero":0.75,
                            "Febrero":0.68,
                            "Marzo":0.6,
                            "Abril":0.6,
                            "Mayo":0.5,
                            "Junio":0.48,
                            "Julio":0.65,
                            "Agosto":0.7,
                            "Septiembre":0.45,
                            "Octubre":0.45,
                            "Noviembre":0.55,
                            "Diciembre":0.85,            
                                            }),
    "HotelReferencia3":TocProm(**{"HotelReferencia3": RefInDB(**{"nombre":"HotelReferencia3",
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
                            "precioMinSuite":450000,}),
                            "Enero":0.88,
                            "Febrero":0.8,
                            "Marzo":0.75,
                            "Abril":0.5,
                            "Mayo":0.5,
                            "Junio":0.48,
                            "Julio":0.7,
                            "Agosto":0.6,
                            "Septiembre":0.3,
                            "Octubre":0.38,
                            "Noviembre":0.48,
                            "Diciembre":0.88,           
                                            }),
}

def get_referencia(nombre: str): # Busqueda
    if nombre in database_refs.keys():
        return database_refs[nombre]
    else:
        return None

def create_hotel(hotel_in_db: RefInDB): # crear  
    database_refs[hotel_in_db.nombre] = hotel_in_db
    return database_refs[hotel_in_db.nombre]

def delete_hotel(nombre: str): # borrar
    if nombre in database_refs.keys():
        del database_refs[nombre]
        return None
    else:
        return None

def update_hotel(hotel_in_db: RefInDB):# actualizar
    if hotel_in_db.nombre in database_refs.keys():
        database_refs[hotel_in_db.nombre] = hotel_in_db
        return None
    else:
        return None