class ProductService:

    def __init__(self, repo):
        self.repo = repo

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