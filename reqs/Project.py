
class Project:
    def __init__(self, projects: Projects):
        self.__all_projects = projects
        self.__result = None

    @property
    def entity(self):
        return self.__result

    @entity.setter
    def entity(self, result):
        self.__result = result

    def __filtering_project(self, project_name):
        self.entity = list(filter(lambda project: project['name'] == project_name, self.__all_projects.content))
        return self

    def get_repositories(self, project_name: str):
        self.__filtering_project(project_name)
        return 123

    def get_charts(self):
        pass
