from reqs import Harbor
from reqs.IEntity import IEntity


class Projects(IEntity):

    def __init__(self, harbor: Harbor):
        self.__content = None
        self.__url = harbor.root_url()

    @property
    def url(self):
        return self.__url + 'projects'

    def get_entity(self):
        return 'project'

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content

    @property
    def removable(self):
        return False
