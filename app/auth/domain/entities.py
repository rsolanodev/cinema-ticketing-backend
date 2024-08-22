from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import StrEnum
from uuid import UUID
from zoneinfo import ZoneInfo

import jwt


class TokenType(StrEnum):
    BEARER = "bearer"


@dataclass
class Token:
    access_token: str
    token_type: TokenType
    expires_in: int

    @classmethod
    def create(
        cls,
        user_id: UUID,
        secret_key: str,
        expire_minutes: int,
        token_type: TokenType = TokenType.BEARER,
    ) -> "Token":
        expire_date = datetime.now(tz=ZoneInfo("UTC")) + timedelta(
            minutes=expire_minutes
        )
        access_token = jwt.encode(
            payload={"exp": expire_date, "sub": str(user_id)},
            key=secret_key,
            algorithm="HS256",
        )
        return Token(
            access_token=access_token,
            token_type=token_type,
            expires_in=expire_minutes,
        )
