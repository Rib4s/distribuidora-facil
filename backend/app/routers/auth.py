from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.dependencies import get_db

from app.models.empresa import Empresa
from app.models.usuario import Usuario

from app.schemas.empresa import (
    EmpresaCreate,
    EmpresaResponse
)

from app.schemas.usuario import (
    UsuarioCreate,
    UsuarioResponse
)

from app.schemas.login import (
    LoginRequest,
    TokenResponse
)

from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token
)

from sqlalchemy import select


router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)


@router.post(
    "/register",
    response_model=EmpresaResponse
)
def register_empresa(
    empresa: EmpresaCreate,
    db: Session = Depends(get_db)
):
    nova_empresa = Empresa(
        nome=empresa.nome,
        email=empresa.email,
        telefone=empresa.telefone
    )

    db.add(nova_empresa)
    db.commit()
    db.refresh(nova_empresa)

    return nova_empresa


@router.post(
    "/register-user",
    response_model=UsuarioResponse
)
def register_user(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=hash_password(usuario.senha),
        empresa_id=usuario.empresa_id
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    usuario = db.execute(
        select(Usuario).where(
            Usuario.email == login_data.email
        )
    ).scalar_one_or_none()

    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="Email ou senha inválidos"
        )

    if not verify_password(
        login_data.senha,
        usuario.senha
    ):
        raise HTTPException(
            status_code=401,
            detail="Email ou senha inválidos"
        )

    access_token = create_access_token(
        {
            "sub": usuario.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }