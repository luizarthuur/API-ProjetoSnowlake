from core.configs import settings

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from core.configs import settings


class ContentSectionModel(settings.DBBaseModel):
    __tablename__ = 'content_section'
    id = Column(Integer, primary_key=True, autoincrement=True)
    content_section_titulo = Column(String(200), nullable=False)
    content_section_conteudo = Column(Text, nullable=True)
