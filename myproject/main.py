from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import os
import crud
import schemas
import models
from database import SessionLocal, engine

print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/supplement_companies/", response_model=list[schemas.SupplementCompany])
def read_supplement_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    supplement_companies = crud.get_supplement_companies_with_items(db, skip=skip, limit=limit)
    return supplement_companies


@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.delete_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item