from sqlalchemy.orm import Session
import bcrypt

import models, schemas


def get_user(db: Session, user_id: int):
    if user_id == None:
        return {"message": "User not found"}
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.User(name=user.name, email=user.email, hashed_password=hashed_password.decode('utf-8'))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: schemas.User):
    db_user = db.query(models.User).filter(models.User.id == user.id).first()
    db_user.name = user.name
    db_user.email = user.email
    db_user.hashed_password = user.hashed_password
    db.commit()
    db.refresh(db_user)
    return db_user
def delete_user(db: Session, user_id: int):
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    return {"message": "User deleted"} and db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(name=product.name, category=product.category)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# CRUD Panier utilisateur

def get_panier_by_user(db: Session, user_id: int):
    return db.query(models.Panier).filter(models.Panier.user_id == user_id).all()


def create_user_panier(db: Session, panier: schemas.PanierCreate, user_id: int):
    db_panier = models.Panier(**panier.dict(), user_id=panier.user_id)
    db.add(db_panier)
    db.commit()
    db.refresh(db_panier)
    return db_panier
def get_panier(db: Session, panier_id: int):
    return db.query(models.Panier).filter(models.Panier.id == panier_id).first()


def get_paniers(db: Session, skip: int = 0, limit: int = 100):
    try:
        paniers = db.query(models.Panier).offset(skip).limit(limit).all()
        return paniers
    except Exception as e:
        print("An error occurred while fetching paniers:", e)
        return []
    #return db.query(models.Panier).offset(skip).limit(limit).all()


def get_panier_by_name(db: Session, name: str):
    return db.query(models.Panier).filter(models.Panier.name == name).first()


def create_panier(db: Session, panier: schemas.PanierCreate):
    db_panier = models.Panier(**panier.dict())
    db.add(db_panier)
    db.commit()
    db.refresh(db_panier)
    return db_panier


def update_panier(db: Session, panier: schemas.Panier):
    db_panier = db.query(models.Panier).filter(models.Panier.id == panier.id).first()
    db_panier.user_id = panier.user_id
    db_panier.product_id = panier.product_id
    db_panier.quantity = panier.quantity
    db_panier.name = panier.name
    db_panier.total = panier.total
    db_panier.payed = panier.payed
    db.commit()
    db.refresh(db_panier)
    return db_panier


def delete_panier(db: Session, panier_id: int):
    db.query(models.Panier).filter(models.Panier.id == panier_id).delete()
    db.commit()
    return {"message": "Panier deleted"} and db.query(models.Panier).filter(models.Panier.id == panier_id).first()


def get_commande(db: Session, commande_id: int):
    return db.query(models.Commande).filter(models.Commande.id == commande_id).first()


def get_commandes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Commande).offset(skip).limit(limit).all()


def create_commande(db: Session, commande: schemas.CommandeCreate):
    db_commande = models.Commande(**commande.dict())
    db.add(db_commande)
    db.commit()
    db.refresh(db_commande)
    return db_commande


def update_commande(db: Session, commande: schemas.Commande):
    db_commande = db.query(models.Commande).filter(models.Commande.id == commande.id).first()
    db_commande.user_id = commande.user_id
    db_commande.product_id = commande.product_id
    db_commande.prix_product = commande.prix_product
    db_commande.quantity = commande.quantity
    db_commande.total = commande.total
    db_commande.date = commande.date
    db.commit()
    db.refresh(db_commande)
    return db_commande


def delete_commande(db: Session, commande_id: int):
    db.query(models.Commande).filter(models.Commande.id == commande_id).delete()
    db.commit()
    return {"message": "Commande deleted"} and db.query(models.Commande).filter(models.Commande.id == commande_id).first()


def get_codepromo(db: Session, codepromo_id: int):
    return db.query(models.CodePromo).filter(models.CodePromo.id == codepromo_id).first()


def get_codepromos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CodePromo).offset(skip).limit(limit).all()


def create_codepromo(db: Session, codepromo: schemas.CodePromoCreate):
    db_codepromo = models.CodePromo(**codepromo.dict())
    db.add(db_codepromo)
    db.commit()
    db.refresh(db_codepromo)
    return db_codepromo


def update_codepromo(db: Session, codepromo: schemas.CodePromo):
    db_codepromo = db.query(models.CodePromo).filter(models.CodePromo.id == codepromo.id).first()
    db_codepromo.code = codepromo.code
    db.commit()
    db.refresh(db_codepromo)
    return db_codepromo


def delete_codepromo(db: Session, codepromo_id: int):
    db.query(models.CodePromo).filter(models.CodePromo.id == codepromo_id).delete()
    db.commit()
    return {"message": "Codepromo deleted"} and db.query(models.CodePromo).filter(models.CodePromo.id == codepromo_id).first()


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update_category(db: Session, category: schemas.Category):
    db_category = db.query(models.Category).filter(models.Category.id == category.id).first()
    db_category.name = category.name
    db.commit()
    db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int):
    db.query(models.Category).filter(models.Category.id == category_id).delete()
    db.commit()
    return {"message": "Category deleted"} and db.query(models.Category).filter(models.Category.id == category_id).first()



def create_panier_for_user(db: Session, user_id: int, panier: schemas.PanierCreate):
    db_panier = models.Panier(
        name=panier.name,
        total=panier.total,
        payed=panier.payed,
        user_id=user_id,
        product_id=panier.product_id,
        quantity=panier.quantity
    )
    db.add(db_panier)
    db.commit()
    db.refresh(db_panier)
    return db_panier