from reqs.IEntity import IEntity
from reqs.IHttpClient import IHttpClient
from reqs.IRemovable import IRemovable
from reqs.ISearching import ISearching
from reqs.Tag import Tag


class Repository(IEntity, IRemovable, ISearching):
    def __init__(self, http_client: IHttpClient, args: dict, root_url: str):
        self.project_id = args['project_id']
        self.name = args['name']
        self.__http_client = http_client
        self.__all_args = args
        self.__url = root_url

    @property
    def root_url(self):
        return self.__url

    @property
    def url(self):
        return self.__url + '/repositories/'

    @property
    def content(self):
        return self.__all_args

    def removable(self):
        return True

    def search_entity_in_content(self, target):
        all_tags = self.get_tags()
        for tag in all_tags:
            if tag.name == target:
                return tag

    def get_tags(self):
        # Собираем URL для получения всех репозиториев в проекте
        content = self.__http_client.get_content(self.url + str(self.name) + '/tags')
        tags = []
        for c in content.json():
            tags.append(Tag(self.__http_client, c, content.url))
        return tags

    def get_image_tag_by_name(self, tag_name: str):
        return self.search_entity_in_content(tag_name)
