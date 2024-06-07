class Article:
    def __init__(self, author_id, magazine_id, title):
        self._author_id = author_id
        self._magazine_id = magazine_id
        self._title = title
        # Code to insert into the database articles table

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value

    def author(self):
        # Code to retrieve author of the article using SQL JOINS
        pass

    def magazine(self):
        # Code to retrieve magazine of the article using SQL JOINS
        pass
