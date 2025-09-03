from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.auth import SECRET_KEY, ALGORITHM
from sqlalchemy.orm import Session
from app.schemas import EmpresaCreate, Empresa
from app.database import SessionLocal
from app.services.empresa_service import (
    create_empresa_service,
    get_empresas_service,
    get_empresa_service,
    delete_empresa_service
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Empresa)
def create_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    return create_empresa_service(db, empresa)

@router.get("/", response_model=list[Empresa])
def read_empresas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_empresas_service(db, skip, limit)

@router.get("/{empresa_id}", response_model=Empresa)
def read_empresa(empresa_id: int, db: Session = Depends(get_db)):
    empresa = get_empresa_service(db, empresa_id)
    if empresa is None:
        raise HTTPException(status_code=404, detail="Empresa not found")
    return empresa

@router.delete("/{empresa_id}")
def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/auth/login")), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não autorizado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not isinstance(username, str) or username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    from app.models.models import Usuario
    user = db.query(Usuario).filter(Usuario.username == username).first()
    if user is None:
        raise credentials_exception
    return user

@router.delete("/{empresa_id}")
def delete_empresa(empresa_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Apenas admin pode deletar empresa.")
    ok = delete_empresa_service(db, empresa_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Empresa not found")
    return {"ok": True}
