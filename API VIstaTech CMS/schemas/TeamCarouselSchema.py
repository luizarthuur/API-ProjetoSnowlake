from typing import Optional

from pydantic import BaseModel as SCBaseModel

class TeamCarouselSchema(SCBaseModel):
    id: Optional[int]
    card_carousel_titulo: Optional[str]
    card_carousel_subtitulo: Optional[str]
    card_carousel_nome: Optional[str]
    card_carousel_cargo: Optional[str]
    card_carousel_descricao: Optional[str]
    card_carousel_link1: Optional[str]
    card_carousel_link2: Optional[str]
    card_carousel_link3: Optional[str]
    nav_main_content_id: Optional[int] 



    class Config:
        orm_mode = True