from src.base.services import BaseService
from src.languages import models, schemas


class PhraseService(BaseService):
    model = models.Phrase
    get_schema = schemas.GetPhrase
    get_detail = schemas.GetPhrase
    update_schema = schemas.UpdatePhrase


phrase_s = PhraseService()
