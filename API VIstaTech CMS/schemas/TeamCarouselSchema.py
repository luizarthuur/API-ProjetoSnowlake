from typing import Optional

from pydantic import BaseModel as SCBaseModel

class TeamCarouselSchema(SCBaseModel):
    id: Optional[int]
    card_carousel_titulo: str
    card_carousel_subtitulo: str
    card_carousel_nome: str
    card_carousel_cargo: str
    card_carousel_descricao: str
    card_carousel_link1: str
    card_carousel_link2: str
    card_carousel_link3: str
    nav_main_content_id: Optional[int] 



    class Config:
        orm_mode = True