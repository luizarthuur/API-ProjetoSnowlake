from core.configs import settings

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from core.configs import settings


class InfoMainContentModel(settings.DBBaseModel):
    __tablename__ = 'info_main_content'
    id = Column(Integer, primary_key=True, autoincrement=True)
    info_main_titulo_principal = Column(String(150), nullable=False)
    info_main_conteudo_principal = Column(Text, nullable=True)
