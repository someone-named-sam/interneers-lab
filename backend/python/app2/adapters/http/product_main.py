from fastapi import FastAPI, HTTPException, UploadFile
from app2.domain.product import Product
#from app2.repository.product_repository import InMemoryProductRepository
from app2.service.product_service import ProductService

from app2.adapters.http.category_controller import router as category_router
import csv


# Initialize
#repo = InMemoryProductRepository()
from app2.repository.mongo_product_repository import MongoProductRepository
from app2.repository.category_repository import MongoCategoryRepository

repo = MongoProductRepository()
category_repo = MongoCategoryRepository()
service = ProductService(repo, category_repo)

app = FastAPI(title="Product API (In-Memory)")
app.include_router(category_router)

# Create product
@app.post("/products", response_model=Product)
def create_product_api(product: Product):
    return service.create_product(product.dict(exclude={"id"}))


# Fetch a single product
@app.get("/products/{product_id}", response_model=Product)
def get_product_api(product_id: str):
    product = service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# List all products
@app.get("/products", response_model=list[Product])
def list_products_api():
    return service.list_products()


# Update a product
@app.put("/products/{product_id}", response_model=Product)
def update_product_api(product_id: str, product: Product):
    updated = service.update_product(product_id, product.dict(exclude={"id"}))
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


# Delete a product
@app.delete("/products/{product_id}")
def delete_product_api(product_id: str):
    success = service.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

'''
#get the products by the category
@app.get("/categories/{category_id}/products")
def get_products_by_category(category_id: str):
    return service.get_products_by_category(category_id)
    '''

@app.post("/products/bulk")
def bulk_upload(file: UploadFile):
    contents = file.file.read().decode("utf-8").splitlines()
    reader = csv.DictReader(contents)

    created = []
    for row in reader:
        row["price"] = float(row["price"])
        row["quantity"] = int(row["quantity"])
        created.append(service.create_product(row))

    return created