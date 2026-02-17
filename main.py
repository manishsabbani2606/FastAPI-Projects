from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import SessionLocal,engine
import database_models

from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"])

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to Product tracking system"

products = [
    Product(id=1, name="Laptop", description="A high performance laptop", price=999.99, quantity=10),
    Product(id=2, name="Smartphone", description="A latest model smartphone", price=499.99, quantity=20),
    Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=15),
    Product(id=4, name="Smartwatch", description="A smartwatch with various features", price=299.99, quantity=5) 
]


def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()
    
def init_db():
    db = SessionLocal()
    
    count = db.query(database_models.ProductDB).count()
    if count == 0:
        for product in products:
            db.add(database_models.ProductDB(**product.model_dump()))
        db.commit()

init_db()
    
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    
    db_products = db.query(database_models.ProductDB).all()
    
    #need a database connection here to fetch products from database

    return db_products

@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    
    db_products = db.query(database_models.ProductDB).filter(database_models.ProductDB.id == id).first()
    return db_products
    # print(f"Fetching product with id: {id}")
    # for product in products:
    #     if product.id == id:
    #         return product
    # return {"message": "Product not found"}


@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db_product = database_models.ProductDB(**product.model_dump())

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product
#     db_pro
#     # products.append(product)
#     # return product
#     # return {"message": "Product added successfully"}

@app.put("/products/{id}")
def update_product(id:int, updated_product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.ProductDB).filter(database_models.ProductDB.id == id).first()
    if db_product:
        db_product.name = updated_product.name
        db_product.description = updated_product.description
        db_product.price = updated_product.price
        db_product.quantity = updated_product.quantity
        db.commit()
        return "product updated successfully"
    else:
        return {"message": "Product not found"}
    
#     # for i in range(len(products)):
#     #     if products[i].id == id:
#     #         products[i] = updated_product
#     #         return updated_product
#     # return {"message": "Product not found"} 

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.ProductDB).filter(database_models.ProductDB.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted successfully"}
    else:
        return {"message": "Product not found"}
#     # return {"message": "Product not found"}

