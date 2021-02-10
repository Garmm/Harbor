from reqs.IEntity import IEntity
from reqs.IHttpClient import IHttpClient
from reqs.ISearching import ISearching
from reqs.Repository import Repository
from reqs.Chart import Chart


class Project(IEntity, ISearching):
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
        return self.__url + '/repositories?project_id='

    @property
    def content(self):
        return self.__all_args

    def search_entity_in_content(self, target):
        all_repositories = self.get_repositories()
        for repository in all_repositories:
            if repository.name == target:
                return repository

    def get_repositories(self):
        # Собираем URL для получения всех репозиториев в проекте
        content = self.__http_client.get_content(self.url + str(self.project_id))
        repositories = []
        for c in content.json():
            repositories.append(Repository(self.__http_client, c, self.__url))
        return repositories

    def get_repository_by_name(self, repository_name: str):
        return self.search_entity_in_content(repository_name)

    def get_charts(self):
        content = self.__http_client.get_content(self.root_url + '/chartrepo/' + self.name + '/charts')
        charts = []
        for c in content.json():
            charts.append(Chart(self.__http_client, c, self.__url))
        return charts

