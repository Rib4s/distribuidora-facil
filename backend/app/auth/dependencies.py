from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database.dependencies import get_db
from app.models.usuario import Usuario
from app.utils.security import verify_token


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    email = verify_token(token)

    usuario = db.execute(
        select(Usuario).where(
            Usuario.email == email
        )
    ).scalar_one_or_none()

    return usuario