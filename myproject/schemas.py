from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    password: str


class SupplementCompanyCreate(BaseModel):
    name: str
    email: str


class SupplementCompany(SupplementCompanyCreate):
    id: int

    class Config:
        orm_mode = True


class ItemCreate(BaseModel):
    name: str
    description: str
    company_id: int


class Item(ItemCreate):
    id: int

    class Config:
        orm_mode = True


class ItemUpdate(BaseModel):
    name: str = None
    description: str = None
    company_id: int = None
