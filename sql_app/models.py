from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    paniers = relationship("Panier", back_populates="user")
    commande = relationship("Commande", back_populates="user")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    name = Column(String)
    category = relationship("Category")
    price = Column(Integer)
    description = Column(String)
    image = Column(String)
    stock = Column(Integer)


class Panier(Base):
    __tablename__ = "paniers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    name = Column(String)
    total = Column(Integer)
    payed = Column(Boolean, default=False)

    user = relationship("User")
    product = relationship("Product")


class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(String)
    token_type = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")


class Commande(Base):
    __tablename__ = "commandes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    prix_product = Column(Integer)
    quantity = Column(Integer)
    total = Column(Integer)
    date = Column(DateTime)
    user = relationship("User")
    product = relationship("Product")
    

class CodePromo(Base):
    __tablename__ = "codes_promo"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String)
    name = Column(String)
    discount = Column(Integer)
    date_start = Column(DateTime)
    date_end = Column(DateTime)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    products = relationship("Product", back_populates="category")
    category = relationship("Product")
