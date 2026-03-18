from pymongo import MongoClient
from app2.domain.product import Product

class MongoProductRepository:

    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["product_db"]
        self.collection = self.db["products"]

    def create(self, data: dict) -> Product:
        result = self.collection.insert_one(data)
        data["id"] = str(result.inserted_id)
        return Product(**data)

    def get(self, product_id: str):
        doc = self.collection.find_one({"_id": product_id})
        if doc:
            doc["id"] = str(doc["_id"])
            return Product(**doc)
        return None

    def list(self):
        products = []
        for doc in self.collection.find():
            doc["id"] = str(doc["_id"])
            products.append(Product(**doc))
        return products

    def update(self, product_id: str, data: dict):
        result = self.collection.update_one(
            {"_id": product_id},
            {"$set": data}
        )
        if result.modified_count == 0:
            return None
        return self.get(product_id)

    def delete(self, product_id: str):
        result = self.collection.delete_one({"_id": product_id})
        return result.deleted_count > 0