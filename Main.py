# login = sys.argv[0]
# pwd = sys.argv[1]
import datetime
import logging
from reqs.HttpClient import HttpClient
from reqs.IEntity import IEntity
from reqs.Project import Project
from reqs.Projects import Projects
from reqs.Repository import Repository

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


class ChartEntity(IEntity):
    def __init__(self, project_name: str, chart_name=None, tag=None):
        self.__project_name = project_name
        self.__content = None
        if chart_name:
            self.__chart_name = chart_name
        if tag:
            self.__tag = tag

    @property
    def project_name(self):
        return self.__project_name

    @property
    def chart_name(self):
        return self.__chart_name

    @property
    def tag(self):
        return self.__tag

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content


# class Chart(ChartEntity):
#     def __init__(self, project_name: str):
#         super().__init__(project_name)
#
#     def get_url(self, root_url):
#         url = root_url + 'chartrepo/' + str(self.project_name.replace('/', '%2F')) + '/charts'
#         return url
#
#     def get_entity(self):
#         return 'chart'

#
# class ChartTags(ChartEntity):
#     def __init__(self, project_name: str, chart_name: str):
#         super().__init__(project_name, chart_name)
#
#     def get_url(self, root_url):
#         url = root_url + 'chartrepo/' + str(self.project_name.replace('/', '%2F')) + '/charts/' \
#               + str(self.chart_name.replace('/', '%2F'))
#         return url
#
#     def get_entity(self):
#         return 'chart_tags'
#
#
# class DeleteChartTag(ChartEntity):
#     def __init__(self, project_name: str, chart_name: str, tag):
#         super().__init__(project_name, chart_name, tag)
#
#     def get_url(self, root_url):
#         url = root_url + 'chartrepo/' + str(self.project_name.replace('/', '%2F')) + '/charts/' \
#               + str(self.chart_name.replace('/', '%2F')) + '/' + str(self.tag)
#         return url
#
#     def get_entity(self):
#         return 'chart_tag'

all_projects = Projects('https://harbor.corp.tele2.ru/', HttpClient()).get_all_projects()


project = Projects('https://harbor.corp.tele2.ru/', HttpClient()).get_project_by_name('library')

all_repositories_in_project = project.get_repositories()

all_tags_in_image = Repository(HttpClient(), project.content, project.root_url).get_tags_by_image_name('library/filebeat')

tag = 1


# single_project = Projects('https://harbor.corp.tele2.ru/', HttpClient()).get_project_by_name('pd')
#
# all_tags_in_image = Repository(
#     HttpClient(), single_repository_in_project.content, single_repository_in_project.root_url)\
#     .get_tags()
#
# single_tag_in_image = Repository(
#     HttpClient(), single_repository_in_project.content, single_repository_in_project.root_url)\
#     .get_image_tag_by_name('6.6.2')
#
# single_tag_in_image.remove()


# all_charts_in_project = Project(HttpClient(), single_project.content, single_project.root_url).get_charts()

# rep = harbor.get_all_charts_in_project('pd')

# rep = harbor.get_all_tags_in_chart('pd', 'auth-service')

# rep = harbor.delete_chart_tag('pd', 'auth-service', '2021.01.13-PD-CI-all-service-v2')