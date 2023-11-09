from sqlalchemy.orm import Session

import models
import schemas

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def delete_item(db: Session, item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return item
    return None

def get_supplement_companies_with_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SupplementCompany).options(joinedload(models.SupplementCompany.items)).offset(skip).limit(limit).all()