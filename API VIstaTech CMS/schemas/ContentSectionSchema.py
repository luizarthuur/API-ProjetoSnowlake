from typing import Optional

from pydantic import BaseModel as SCBaseModel

class ContentSectionSchema(SCBaseModel):
    id: Optional[int]
    content_section_titulo: str
    content_section_conteudo: str



    class Config:
        orm_mode = True