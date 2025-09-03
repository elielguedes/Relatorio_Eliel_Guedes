from fastapi import FastAPI
from app.database import Base, engine
from app.routers import empresas, estabelecimentos, socios
from app.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(empresas.router, prefix="/empresas", tags=["empresas"])
app.include_router(estabelecimentos.router, prefix="/estabelecimentos", tags=["estabelecimentos"])
app.include_router(socios.router, prefix="/socios", tags=["socios"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])