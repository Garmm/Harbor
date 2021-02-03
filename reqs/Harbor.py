from reqs.Project import Project
from reqs.Projects import Projects
from reqs.HttpClient import HttpClient


class Harbor:
    def __init__(self, dns: str):
        self.__api = dns + "api/"

    def get_all_projects(self):
        projects = Projects(self.__api)
        # http = HttpClient()
        # http.get_content(projects)
        return projects

    # def get_project(self):
    #     project = Project(self.get_all_projects())
    #     return project

    # def get_all_repositories(self, project_id: int):
    #     repository = Repository(project_id)
    #     self.__get_content(repository)
    #     return repository.content
    #
    # def get_all_tags_in_repository(self, repository_name: str):
    #     repository_tags = RepositoryTags(repository_name)
    #     self.__get_content(repository_tags)
    #     return repository_tags.content
    #
    # def get_all_charts_in_project(self, project_name: str):
    #     charts = Chart(project_name)
    #     self.__get_content(charts)
    #     return charts.content
    #
    # def get_all_tags_in_chart(self, project_name: str, chart_name: str):
    #     chart_tags = ChartTags(project_name, chart_name)
    #     self.__get_content(chart_tags)
    #     return chart_tags.content
    #
    # def delete_repository_tag(self, repository_name: str, tag):
    #     tag = DeleteRepositoryTag(repository_name, tag)
    #     self.__get_content(tag)
    #     if tag.content:
    #         self.__delete_content(tag)
    #     else:
    #         pass
    #
    # def delete_chart_tag(self, project_name: str, chart_name: str, tag):
    #     tag = DeleteChartTag(project_name, chart_name, tag)
    #     self.__get_content(tag)
    #     if tag.content:
    #         self.__delete_content(tag)
    #     else:
    #         pass

