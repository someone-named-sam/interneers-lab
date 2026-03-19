class CategoryService:

    def __init__(self, repo):
        self.repo = repo

    def create_category(self, data):
        return self.repo.create(data)

    def list_categories(self):
        return self.repo.list()

    def get_category(self, category_id):
        return self.repo.get(category_id)

    def delete_category(self, category_id):
        return self.repo.delete(category_id)