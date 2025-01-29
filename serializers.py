from pydantic import BaseModel


class AutomobilisSchema(BaseModel):
    id: int
    gamintojas: str
    modelis: str
    spalva: str
    metai: int

    class Config:
        from_attributes = True
