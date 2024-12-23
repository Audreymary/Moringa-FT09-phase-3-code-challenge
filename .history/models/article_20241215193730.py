from database.connection import Connection
from models.author import Author  # Import Author class
from models.magazine import Magazine  # Import Magazine class

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        if not isinstance(id, int):
            raise ValueError("ID must be an integer.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        if not isinstance(content, str):
            raise ValueError("Content must be a string.")
        if not isinstance(author_id, int):
            raise ValueError("Author ID must be an integer.")
        if not isinstance(magazine_id, int):
            raise ValueError("Magazine ID must be an integer.")
        
        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Cannot change title after initialization.")

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        raise AttributeError("Cannot change content after initialization.")

    @property
    def author(self):
        query = "SELECT * FROM authors WHERE id = ?;"
        result = Connection.get_db_connection().execute(query, (self._author_id,)).fetchone()
        return Author(result[0], result[1]) if result else None

    @property
    def magazine(self):
        query = "SELECT * FROM magazines WHERE id = ?;"
        result = Connection.get_db_connection().execute(query, (self._magazine_id,)).fetchone()
        return Magazine(result[0], result[1]) if result else None