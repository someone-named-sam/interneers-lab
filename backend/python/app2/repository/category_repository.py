from pymongo import MongoClient
from app2.domain.category import ProductCategory

class MongoCategoryRepository:

    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["product_db"]
        self.collection = self.db["categories"]

    def create(self, data):
        result = self.collection.insert_one(data)
        data["id"] = str(result.inserted_id)
        return ProductCategory(**data)

    def list(self):
        return [
            ProductCategory(**{**doc, "id": str(doc["_id"])})
            for doc in self.collection.find()
        ]

    def get(self, category_id):
        doc = self.collection.find_one({"_id": category_id})
        if doc:
            doc["id"] = str(doc["_id"])
            return ProductCategory(**doc)
        return None

    def delete(self, category_id):
        return self.collection.delete_one({"_id": category_id}).deleted_count > 0