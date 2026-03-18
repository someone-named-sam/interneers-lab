from fastapi import FastAPI, HTTPException
from app2.domain.product import Product
#from app2.repository.product_repository import InMemoryProductRepository
from app2.service.product_service import ProductService

# Initialize
#repo = InMemoryProductRepository()
from app2.repository.mongo_product_repository import MongoProductRepository

repo = MongoProductRepository()
service = ProductService(repo)

app = FastAPI(title="Product API (In-Memory)")

# Create product
@app.post("/products", response_model=Product)
def create_product_api(product: Product):
    return service.create_product(product.dict(exclude={"id"}))


# Fetch a single product
@app.get("/products/{product_id}", response_model=Product)
def get_product_api(product_id: int):
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
def update_product_api(product_id: int, product: Product):
    updated = service.update_product(product_id, product.dict(exclude={"id"}))
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


# Delete a product
@app.delete("/products/{product_id}")
def delete_product_api(product_id: int):
    success = service.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}