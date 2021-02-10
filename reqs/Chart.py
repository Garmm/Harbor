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

    @property
    def root_url(self):
        return self.__url

    @property
    def url(self):
        return self.__url + '/' + self.name

    @property
    def content(self):
        return self.__all_args

    def removable(self):
        return True

    def remove(self):
        if self.__size > 0:
            self.__http_client.delete_content(self, self.url)

    def get_helm_chart_by_name(self, chart_name: str):
        return self.search_entity_in_content(chart_name)
