from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas, crud
from database import  SessionLocal, engine


app = FastAPI()


models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/user/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    if users is None:
        raise HTTPException(status_code=404, detail="Users not found")
    return users


@app.post("/user/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.put("/user/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.User, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db=db, user=user)


@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, user_id=user_id)



@app.get("/product/{product_id}")
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@app.get("/products/", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    if products is None:
        raise HTTPException(status_code=404, detail="Products not found")
    return products


@app.post("/product/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_name(db, name=product.name)
    if db_product:
        raise HTTPException(status_code=400, detail="Product already registered")
    return crud.create_product(db=db, product=product)


@app.put("/product/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.Product, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.update_product(db=db, product=product)


@app.delete("/product/{product_id}")


def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.delete_product(db=db, product_id=product_id)


@app.get("/panier/{panier_id}")
def read_panier(panier_id: int, db: Session = Depends(get_db)):
    db_panier = crud.get_panier(db, panier_id=panier_id)
    if db_panier is None:
        raise HTTPException(status_code=404, detail="Panier not found")
    return db_panier


@app.get("/paniers/", response_model=list[schemas.Panier])
def read_paniers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    paniers = crud.get_paniers(db, skip=skip, limit=limit)
    if paniers is None:
        raise HTTPException(status_code=404, detail="Paniers not found")
    return paniers


@app.post("/panier/", response_model=schemas.PanierCreate)
def create_panier(panier: schemas.PanierCreate, db: Session = Depends(get_db)):
    db_panier = crud.get_panier_by_name(db, name=panier.name)
    if db_panier:
        raise HTTPException(status_code=400, detail="Panier already registered")
    return crud.create_panier(db=db, panier=panier)


@app.put("/panier/{panier_id}", response_model=schemas.Panier)
def update_panier(panier_id: int, panier: schemas.Panier, db: Session = Depends(get_db)):
    db_panier = crud.get_panier(db, panier_id=panier_id)
    if db_panier is None:
        raise HTTPException(status_code=404, detail="Panier not found")
    return crud.update_panier(db=db, panier=panier)


@app.delete("/panier/{panier_id}")
def delete_panier(panier_id: int, db: Session = Depends(get_db)):
    db_panier = crud.get_panier(db, panier_id=panier_id)
    if db_panier is None:
        raise HTTPException(status_code=404, detail="Panier not found")
    return crud.delete_panier(db=db, panier_id=panier_id)


#panier pour chaque utilisteur


@app.post("/user/{user_id}/panier", response_model=schemas.Panier)
def create_user_panier(user_id: int, panier: schemas.PanierCreate, db: Session = Depends(get_db)):
    return crud.create_panier_for_user(db=db, user_id=user_id, panier=panier)


@app.get("/user/{user_id}/panier")
def read_user_panier(user_id: int, db: Session = Depends(get_db)):
    db_panier = crud.get_panier_by_user(db, user_id=user_id)
    if db_panier is None:
        raise HTTPException(status_code=404, detail="Panier not found")
    return db_panier


@app.post("/user/{user_id}/panier", response_model=schemas.Panier)
def create_user_panier(user_id: int, panier: schemas.PanierCreate, db: Session = Depends(get_db)):
    return crud.create_panier_for_user(db=db, user_id=user_id, panier=panier)


@app.get("/commandes/", response_model=list[schemas.Commande])
#commande pour chaque utilisateur


@app.get("/user/{user_id}/commande")
def read_user_commande(user_id: int, db: Session = Depends(get_db)):
    db_commande = crud.get_commande_by_user(db, user_id=user_id)
    if db_commande is None:
        raise HTTPException(status_code=404, detail="Commande not found")
    return db_commande


@app.get("/commande/{commande_id}")
def read_commande(commande_id: int, db: Session = Depends(get_db)):
    db_commande = crud.get_commande(db, commande_id=commande_id)
    if db_commande is None:
        raise HTTPException(status_code=404, detail="Commande not found")
    return db_commande

