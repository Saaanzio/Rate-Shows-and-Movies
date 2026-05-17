from .show_repository import ShowRepository
class ShowService:
    def __init__(self):
        self.show_repository = ShowRepository()

    def save_review(self, name: str, review: str | None, rating: int) -> None:
        self.show_repository.save_review(name, review, rating)
        return

    def get_all_reviews(self) -> list[dict]:
        return self.show_repository.get_all_reviews()

    def get_review_by_id(self, review_id: int) -> dict | None:
        return self.show_repository.get_show_by_id(review_id)

    def update_review(self, review_id: int, name: str, description: str, rating: int) -> None:
        return self.show_repository.update_show(review_id, name, description, rating)

    def delete_review(self, review_id: int) -> None:
        return self.show_repository.delete_show(review_id)