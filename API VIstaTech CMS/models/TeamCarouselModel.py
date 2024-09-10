from core.configs import settings

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from core.configs import settings

class TeamCarouselModel(settings.DBBaseModel):
    __tablename__ = 'team_carousel'
    id = Column(Integer, primary_key=True, autoincrement=True)
    card_carousel_titulo = Column(String(100), nullable=True)
    card_carousel_subtitulo = Column(String(100), nullable=True)
    card_carousel_nome = Column(String(100), nullable=True)
    card_carousel_cargo = Column(String(100), nullable=True)
    card_carousel_descricao = Column(Text, nullable=True)
    card_carousel_link1 = Column(String(255), nullable=True)
    card_carousel_link2 = Column(String(255), nullable=True)
    card_carousel_link3 = Column(String(255), nullable=True)
    nav_main_content_id = Column(Integer, ForeignKey('nav_main_content.id'))

    # Relacionamento com o modelo NavMainContent
    nav_main_content = relationship("NavMainContentModel", back_populates="team_carousels")
    