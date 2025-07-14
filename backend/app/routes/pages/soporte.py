from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.routes.auth.auth import get_current_user

from app.schemas.producto import PromocionOut, PromocionCreate
from app.models import User, MensajeContacto, FAQ
from app.schemas.users import MensajeContactoCreate, MensajeContactoOut, FAQOut

from typing import List

router = APIRouter(
    prefix="/soporte",
    tags=["Soporte y validaciones"]
)

# ----------------- ENDPOINT DE CONTACTO ---------------------
@router.post("/contacto", response_model=MensajeContactoOut)
def enviar_mensaje_contacto(
    data: MensajeContactoCreate,
    db: Session = Depends(get_db),
    usuario: User = Depends(get_current_user)
):
    mensaje = MensajeContacto(
        usuario_id = usuario.id,
        asunto = data.asunto,
        mensaje = data.mensaje
    )
    db.add(mensaje)
    db.commit()
    db.refresh(mensaje)

    return mensaje

# -------------- ENDPOINT DE PREGUNTAS FRECUENTES -----------
@router.get("/faqs", response_model=List[FAQOut])
def faqs(
    db: Session = Depends(get_db)
):
    return db.query(FAQ).order_by(FAQ.id.asc()).all()