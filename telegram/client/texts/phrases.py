from client.base import BaseAPI, Urls


class PhraseAPI(BaseAPI):
    def __init__(self):
        super(PhraseAPI, self).__init__()
        self._URL += Urls.phrases


phrase_api = PhraseAPI()
