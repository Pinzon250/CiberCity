from pydantic import BaseModel

class CategoriaOut(BaseModel):
    id: int
    nombre: str
    slug: str

    model_config = {
        "from_attributes": True
    }
