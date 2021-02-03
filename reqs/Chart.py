from reqs.IEntity import IEntity
from reqs.IHttpClient import IHttpClient
from reqs.IRemovable import IRemovable


class Chart(IEntity, IRemovable):
    def __init__(self, http_client: IHttpClient, args: dict, root_url: str):
        self.name = args['name']
        self.created = args['created']
        self.__http_client = http_client
        self.__all_args = args
        self.__url = root_url
