from pydantic import BaseModel
from typing import List, Optional

from pydantic.types import datetime as DateTime

class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    paniers: List["Panier"] = []
    commande: List["Commande"] = []
    class Config:
        orm_mode = True


class UserWithPaniers(User):
    paniers: List["Panier"] = []



class ProductBase(BaseModel):
    name: str
    price: int
    description: str | None = None
    image: str
    stock: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    category_id: int

    category: Optional[str]

    class Config:
        orm_mode = True


class PanierBase(BaseModel):
    name: str
    total: int
    payed: bool


class PanierCreate(PanierBase):
    quantity: int
    product_id: int | None = None


class Panier(PanierBase):
    id: int
    user_id: int
    product_id: int | None = None
    quantity: int

    class Config:
        orm_mode = True
    
    product: Optional[Product]
    


class CommandeBase(BaseModel):
    prix_product: int
    quantity: int
    total: int
    date: DateTime


class CommandeCreate(CommandeBase):
    pass


class Commande(CommandeBase):
    id: int
    user_id: int
    product_id: int

    class Config:
        orm_mode = True

    user: Optional[User]
    product: Optional[Product]


class CodePromoBase(BaseModel):
    code: str
    name: str
    discount: int


class CodePromoCreate(CodePromoBase):
    date_start: DateTime
    date_end: DateTime


class CodePromo(CodePromoBase):
    id: int
    date_start: DateTime
    date_end: DateTime

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    products: List[Product] = []

    class Config:
        orm_mode = True

    category: Optional[str]