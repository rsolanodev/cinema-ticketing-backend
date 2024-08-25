import uuid
from dataclasses import dataclass

from app.core.domain.constants.unset import UnsetType


@dataclass
class PosterImage:
    filename: str | None
    content: bytes
    content_type: str | None


@dataclass
class Category:
    id: uuid.UUID
    name: str

    @classmethod
    def create(cls, name: str) -> "Category":
        return cls(id=uuid.uuid4(), name=name)


@dataclass
class Movie:
    id: uuid.UUID
    title: str
    description: str | None
    poster_image: str | None

    @classmethod
    def create(
        cls, title: str, description: str | None, poster_image: str | None
    ) -> "Movie":
        return cls(
            id=uuid.uuid4(),
            title=title,
            description=description,
            poster_image=poster_image,
        )

    def update(
        self,
        title: str | UnsetType,
        description: str | None | UnsetType,
        poster_image: str | None | UnsetType,
    ) -> None:
        if not isinstance(title, UnsetType):
            self.title = title

        if not isinstance(description, UnsetType):
            self.description = description

        if not isinstance(poster_image, UnsetType):
            self.poster_image = poster_image
