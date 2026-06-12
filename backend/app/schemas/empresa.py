from pydantic import BaseModel, EmailStr


class EmpresaCreate(BaseModel):
    nome: str
    email: EmailStr
    telefone: str | None = None


class EmpresaResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    telefone: str | None = None

    class Config:
        from_attributes = True