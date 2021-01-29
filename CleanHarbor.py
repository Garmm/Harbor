import json
import requests
from requests.auth import HTTPBasicAuth
import sys
import logging
import time
import datetime
from datetime import date, timedelta

# login = sys.argv[0]
# pwd = sys.argv[1]

# Базовая конфигурация логгера

logging.basicConfig(
    # filename="/var/log/harbor_clean/output_" + (datetime.datetime.now()).strftime("%Y-%m-%d") + ".txt",
    filename="output_" + (datetime.datetime.now()).strftime("%Y-%m-%d") + ".txt",
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Отключение проверки ssl сертификата
requests.packages.urllib3.disable_warnings()


class IEntity:

    def get_url(self, root_url):
        pass

    def get_entity(self):
        pass

    @property
    def content(self):
        pass

    @content.setter
    def content(self, content):
        pass


class Project(IEntity):

    def __init__(self):
        self.__content = None

    def get_url(self, root_url: str):
        url = root_url + 'projects'
        return url

    def get_entity(self):
        return 'project'

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content


class ProjectEntity(IEntity):
    def __init__(self, project_id: int):
        self.__project_id = project_id
        self.__content = None

    @property
    def project_id(self):
        return self.__project_id

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content


class Repository(ProjectEntity):
    def __init__(self, project_id: int):
        super().__init__(project_id)

    def get_url(self, root_url):
        url = root_url + 'repositories?project_id=' + str(self.project_id)
        return url

    def get_entity(self):
        return 'repository'


class ChartEntity(IEntity):
    def __init__(self, project_name: str, chart_name='default'):
        self.__project_name = project_name
        self.__content = None
        self.__chart_name = chart_name

    @property
    def project_name(self):
        return self.__project_name

    @property
    def chart_name(self):
        return self.__chart_name

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content


class Chart(ChartEntity):
    def __init__(self, project_name: str):
        super().__init__(project_name)

    def get_url(self, root_url):
        url = root_url + 'chartrepo/' + str(self.project_name.replace('/', '%2F')) + '/charts'
        return url

    def get_entity(self):
        return 'chart'


class ChartTags(ChartEntity):
    def __init__(self, project_name: str, chart_name: str):
        super().__init__(project_name, chart_name)

    def get_url(self, root_url):
        url = root_url + 'chartrepo/' + str(self.project_name.replace('/', '%2F')) + '/charts/' \
              + str(self.chart_name.replace('/', '%2F'))
        return url

    def get_entity(self):
        return 'chart_tags'


class RepositoryTagsEntity(IEntity):
    def __init__(self, repository_name: str):
        self.__repository_name = repository_name
        self.__content = None

    @property
    def repository_name(self):
        return self.__repository_name

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content


class RepositoryTags(RepositoryTagsEntity):
    def __init__(self, repository_name):
        super().__init__(repository_name)

    def get_url(self, root_url):
        url = root_url + 'repositories/' + str(self.repository_name.replace('/', '%2F')) + '/tags'
        return url

    def get_entity(self):
        return 'repository_tags'


class Harbor:
    def __init__(self, dns: str):
        self.api = dns + "api/"

    def __getcontent(self, entity: IEntity):

        try:
            response = requests.get(
                entity.get_url(self.api),
                verify=False
            )
            if response.status_code == 200:
                logger.info("Method: getcontent; Content " + entity.get_entity() + " was got successfully")
                entity.content = response.json()
                return entity
            else:
                logger.error("Method: getcontent; Response status code : " + str(response.status_code) +
                             "; Reason : " + str(response.reason))
        except Exception as e:
            logger.error(e)

    def get_all_projects(self):
        project = Project()
        self.__getcontent(project)
        return project.content

    def get_all_repositories(self, project_id: int):
        repository = Repository(project_id)
        self.__getcontent(repository)
        return repository.content

    def get_all_tags_in_repository(self, repository_name: str):
        repository_tags = RepositoryTags(repository_name)
        self.__getcontent(repository_tags)
        return repository_tags.content

    def get_all_charts_in_project(self, project_name: str):
        charts = Chart(project_name)
        self.__getcontent(charts)
        return charts.content

    def get_all_tags_in_chart(self, project_name: str, chart_name: str):
        chart_tags = ChartTags(project_name, chart_name)
        self.__getcontent(chart_tags)
        return chart_tags.content


harbor = Harbor("https://harbor.corp.tele2.ru/")

rep = harbor.get_all_projects()

# rep = harbor.get_all_repositories(9)

# rep = harbor.get_all_tags_in_repository('pd/backend/auth-service')

# rep = harbor.get_all_charts_in_project('pd')

# rep = harbor.get_all_tags_in_chart('pd', 'auth-service')

print(str(rep))