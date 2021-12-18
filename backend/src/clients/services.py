from src.base.services import BaseService
from . import models, schemas


class ClientsService(BaseService):
    model = models.Client
    get_schema = schemas.GetClient
    get_detail = schemas.GetClient
    create_schema = schemas.CreateClient
    update_schema = schemas.CreateClient


clients_s = ClientsService()
