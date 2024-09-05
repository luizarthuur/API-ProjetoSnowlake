from typing import Optional

from pydantic import BaseModel as SCBaseModel

class InfoMainContentSchema(SCBaseModel):
    id: Optional[int]
    info_main_titulo_principal: str
    info_main_conteudo_principal: str


    class Config:
        orm_mode = True