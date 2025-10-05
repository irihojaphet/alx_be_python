# library_management.py

from __future__ import annotations
from typing import List


class Book:
    """
    A simple book with public title/author and a private availability flag.
    """

    def __init__(self, title: str, author: str) -> None:
        self.title = title                   # public
        self.author = author                 # public
        self._is_checked_out: bool = False   # "private" by convention

    def check_out(self) -> bool:
        """
        Mark the book as checked out if available.
        Returns True if the state changed, False if it was already checked out.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self) -> bool:
        """
        Mark the book as returned if it was checked out.
        Returns True if the state changed, False otherwise.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    @property
    def is_checked_out(self) -> bool:
        """Read-only view of checkout state."""
        return self._is_checked_out

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book instances.
    """

    def __init__(self) -> None:
        self._books: List[Book] = []  # private list of books

    def add_book(self, book: Book) -> None:
        """Add a Book to the collection."""
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added.")
        self._books.append(book)

    def check_out_book(self, title: str) -> bool:
        """
        Find the first available book with the given title (case-insensitive)
        and check it out. Returns True if successful, False otherwise.
        """
        target = title.strip().lower()
        for b in self._books:
            if b.title.lower() == target and not b.is_checked_out:
                return b.check_out()
        return False

    def return_book(self, title: str) -> bool:
        """
        Find the first checked-out book with the given title (case-insensitive)
        and return it. Returns True if successful, False otherwise.
        """
        target = title.strip().lower()
        for b in self._books:
            if b.title.lower() == target and b.is_checked_out:
                return b.return_book()
        return False

    def list_available_books(self) -> None:
        """
        Print all available books in the format:
        <title> by <author>
        """
        for b in self._books:
            if not b.is_checked_out:
                print(str(b))
