from datetime import date
from typing import Protocol
from uuid import UUID

from app.movies.domain.entities import Movie


class MovieRepository(Protocol):
    def save(self, movie: Movie) -> None: ...

    def get(self, id: UUID) -> Movie | None: ...

    def delete(self, id: UUID) -> None: ...

    def add_genre(self, movie_id: UUID, genre_id: UUID) -> None: ...

    def remove_genre(self, movie_id: UUID, genre_id: UUID) -> None: ...

    def get_available_movies_for_date(self, available_date: date) -> list[Movie]: ...

    def get_movie_for_date(
        self, movie_id: UUID, showtime_date: date
    ) -> Movie | None: ...
