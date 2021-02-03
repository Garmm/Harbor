
from reqs.IEntity import IEntity
from reqs.IHttpClient import IHttpClient
from reqs.ISearching import ISearching
from reqs.Project import Project


class Projects(IEntity, ISearching):

    def __init__(self, url: str, http_client: IHttpClient):
        self.__url = url + 'api'
        self.__http_client = http_client

    @property
    def root_url(self):
        return self.__url

    @property
    def url(self):
        return self.__url + '/projects'

    def search_entity_in_content(self, target):
        all_projects = self.get_all_projects()
        for project in all_projects:
            if project.name == target:
                return project

    def get_all_projects(self):
        content = self.__http_client.get_content(self.url)
        projects = []
        for c in content.json():
            projects.append(Project(self.__http_client, c, self.root_url))
        return projects

    def get_project_by_name(self, project_name: str):
        return self.search_entity_in_content(project_name)

