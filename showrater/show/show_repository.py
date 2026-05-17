from database.db import get_connection, execute, fetch_all, fetch_one

class ShowRepository:

    SAVE_QUERY = "INSERT INTO reviews (name, description, rating) VALUES (?,?,?)"

    GET_ALL_QUERY = "SELECT * FROM reviews"

    GET_BY_ID = "SELECT * FROM reviews WHERE id = ?"

    UPDATE_BY_ID = "UPDATE reviews SET name = ?, description = ?, rating = ? WHERE ID = ?"

    DELETE_BY_ID = "DELETE FROM reviews WHERE ID = ?"


    def save_review(self, name: str, review: str, rating: int) -> None:
        execute(self.SAVE_QUERY, (name, review, rating))

    def get_all_reviews(self) -> list[dict]:
        return fetch_all(self.GET_ALL_QUERY)

    def get_show_by_id(self, review_id: int) -> dict:
        return fetch_one(self.GET_BY_ID, (review_id,))

    def update_show(self, review_id: int, name: str, description: str, rating: int) -> None:
        execute(self.UPDATE_BY_ID, (name, description, rating, review_id))

    def delete_show(self, review_id: int) -> None:
        execute(self.DELETE_BY_ID, (review_id,))

