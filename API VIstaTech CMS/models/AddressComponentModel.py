from core.configs import settings

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from core.configs import settings

class AddressComponentModel(settings.DBBaseModel):
    __tablename__ = 'address_component'
    id = Column(Integer, primary_key=True, autoincrement=True)
    address_component_titulo = Column(Text, nullable=False)
    address_component_endereco_conteudo = Column(Text, nullable=True)
    address_component_telefone_conteudo = Column(String(50), nullable=True)
    address_component_email_conteudo = Column(String(150), nullable=True)
