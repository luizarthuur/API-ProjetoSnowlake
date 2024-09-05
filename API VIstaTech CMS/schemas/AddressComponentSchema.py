from typing import Optional, List

from pydantic import BaseModel as SCBaseModel


from schemas.TeamCarouselSchema import TeamCarouselSchema 

class AddressComponentSchema(SCBaseModel):
    id: Optional[int]
    address_component_titulo: str
    address_component_endereco_conteudo: str
    address_component_telefone_conteudo: str
    address_component_email_conteudo: str



    class Config:
        orm_mode = True