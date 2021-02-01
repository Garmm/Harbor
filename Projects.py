from IEntity import *


class Projects(IEntity):

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
