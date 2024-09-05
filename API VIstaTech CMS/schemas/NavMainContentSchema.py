from typing import Optional, List

from pydantic import BaseModel as SCBaseModel
from schemas.TeamCarouselSchema import TeamCarouselSchema

class NavMainContentSchema(SCBaseModel):
    id: Optional[int]
    nav_main_titulo_principal: str
    nav_main_subtitulo: str
    team_carousels: List[TeamCarouselSchema] = []


    class Config:
        orm_mode = True