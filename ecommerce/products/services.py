from fastapi import HTTPException, status
from . import models
from . import schema
from sqlalchemy.orm import Session
from typing import List

async def create_category(category: schema.Category, database: Session) -> models.Category:
    new_category = models.Category(name=category.name)
    database.add(new_category)
    database.commit()
    database.refresh(new_category)
    return new_category

async def get_all_categories(database) -> List[models.Category]:
    categories = database.query(models.Category).all()
    return categories

async def get_category_by_id(category_id: int, database: Session) -> models.Category:
    category = database.query(models.Category).get(category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    
    
async def delete_category_by_id(category_id: int, database: Session) -> None :
    database.query(models.Category).filter(models.Category.id == category_id).delete()
    database.commit()
    
    
async def create_new_product(request, database) -> models.Product:
    new_product = models.Product(name=request.name, quantity=request.quantity,
                                 description=request.description, price=request.price,
                                 category_id=request.category_id)
    database.add(new_product)
    database.commit()
    database.refresh(new_product)
    return new_product


async def get_all_products(database) -> List[models.Product]:
    products = database.query(models.Product).all()
    return products