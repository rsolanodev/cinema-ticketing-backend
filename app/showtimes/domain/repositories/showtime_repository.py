import uuid
from datetime import datetime
from typing import Protocol

from app.showtimes.domain.entities import Showtime


class ShowtimeRepository(Protocol):
    def exists(self, movie_id: uuid.UUID, show_datetime: datetime) -> bool: ...
    def create(self, showtime: Showtime) -> None: ...
    def delete(self, showtime_id: uuid.UUID) -> None: ...
