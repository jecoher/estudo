from pydantic import BaseModel, configDict   

class productoCrear(BaseModel):
    nombre:str
    unidad_medida:str
    categoria: str
    subcategoria: str

class ProductoRespuesta(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:int
    nombre: str
    unidad_medida:str
    categoria: str
    subcategoria: str