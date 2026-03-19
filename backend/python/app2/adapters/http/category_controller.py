from fastapi import APIRouter, HTTPException
from app2.domain.category import ProductCategory
from app2.repository.category_repository import MongoCategoryRepository
from app2.service.category_service import CategoryService

from app2.repository.mongo_product_repository import MongoProductRepository
from app2.service.product_service import ProductService

router = APIRouter()

# Category setup
category_repo = MongoCategoryRepository()
category_service = CategoryService(category_repo)

# Product setup (needed for nested API)
product_repo = MongoProductRepository()
product_service = ProductService(product_repo, category_repo)

@router.post("/categories", response_model=ProductCategory)
def create_category(category: ProductCategory):
    return category_service.create_category(category.dict(exclude={"id"}))

@router.get("/categories", response_model=list[ProductCategory])
def list_categories():
    return category_service.list_categories()

@router.get("/categories/{category_id}", response_model=ProductCategory)
def get_category(category_id: str):
    cat = category_service.get_category(category_id)
    if not cat:
        raise HTTPException(404, "Category not found")
    return cat

@router.delete("/categories/{category_id}")
def delete_category(category_id: str):
    if not category_service.delete_category(category_id):
        raise HTTPException(404, "Category not found")
    return {"message": "Deleted"}

@router.get("/categories/{category_id}/products")
def get_products_by_category(category_id: str):
    return product_service.get_products_by_category(category_id)