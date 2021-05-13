from pydantic import BaseModel, validator
from typing import Optional, List
import re


class Contact(BaseModel):
    id: Optional[str]
    name: str
    cellphone: str

    @validator('cellphone')
    def validate_phone_number(cls, v):
        if len(v) > 11:
            raise ValueError('Número inválido, formato válido DDD + 9 + Digitos')
        regex_match = re.search(
            r"([0-9]{2})([0-9]{1})([0-9]{4})([0-9]{4})", 
            v
        )
        print(regex_match)
        if not regex_match:
            raise ValueError('Número inválido, formato válido DDD + 9 + Digitos')
        return v


class Contacts(BaseModel):
    contacts: Optional[List[Contact]] = None