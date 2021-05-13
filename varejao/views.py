from fastapi import APIRouter, Depends
from varejao.schemas import Contacts
from varejao.controller import create_contacts, get_contacts
from auth.views import verify_token
from db import get_db

router = APIRouter(
    prefix="/varejao/contacts",
    dependencies=[Depends(verify_token)],
    tags=["varejao"],
)

session = get_db('varejao')

@router.post("/", status_code=201)
async def create(contacts: Contacts, token: dict = Depends(verify_token)):
    contacts = create_contacts(db=session, contacts=contacts, user=token)
    return {'detail': 'Contatos criados com sucesso!'}

@router.get("/", status_code=201)
async def get():
    contacts = get_contacts(db=session)
    return contacts