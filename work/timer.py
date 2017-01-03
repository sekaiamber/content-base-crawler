from datetime import datetime
from colors import bold
from .utils import singleton


@singleton
class Timer:
    _tags = []

    def addTag(self, tagName):
        self._tags.append((tagName, datetime.now()))
        self.print(tagName)

    def getTag(self, tagName):
        for tag in self._tags:
            if tag[0] == tagName:
                return tag

    def print(self, tagName=None):
        if tagName is not None:
            tag = self.getTag(tagName)
            print(bold(tag[0], bg='green') + '  ' + str(tag[1]))
        else:
            for tag in self._tags:
                print(bold(tag[0], bg='green') + '  ' + str(tag[1]))
