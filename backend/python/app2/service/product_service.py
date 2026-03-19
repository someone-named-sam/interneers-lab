from fastapi import HTTPException
class ProductService:

    def __init__(self, repo, category_repo):
        self.repo = repo
        self.category_repo = category_repo

    def create_product(self, data):
        return self.repo.create(data)

    def get_product(self, product_id):
        return self.repo.get(product_id)

    def list_products(self):
        return self.repo.list()

    def update_product(self, product_id, data):
        return self.repo.update(product_id, data)

    def delete_product(self, product_id):
        return self.repo.delete(product_id)
    
    def get_products_by_category(self, category_id):
        return [p for p in self.repo.list() if p.category_id == category_id]
    
    

    def assign_category(self, product_id, category_id):
        category = self.category_repo.get(category_id)

        if not category:
            raise HTTPException(status_code=400, detail="Category does not exist")

        return self.repo.update(product_id, {"category_id": category_id})