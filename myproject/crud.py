from sqlalchemy.orm import Session, joinedload

import models
import schemas
import auth


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def delete_item(db: Session, item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return item
    return None


def get_supplement_companies_with_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SupplementCompany).options(joinedload(models.SupplementCompany.items)).offset(skip).limit(limit).all()


def create_supplement_company(db: Session, company: schemas.SupplementCompanyCreate):
    hashed_password = auth.get_password_hash(company.password)
    db_company = models.SupplementCompany(name=company.name, email=company.email, hashed_password=hashed_password)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def update_item(db: Session, item_id: int, updated_item: schemas.ItemUpdate):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()

    if db_item:
        for key, value in updated_item.dict(exclude_unset=True).items():
            setattr(db_item, key, value)

        db.commit()
        db.refresh(db_item)

    return db_item

