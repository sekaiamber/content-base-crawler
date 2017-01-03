from .webdom import WebDom


class WebPage(WebDom):
    def __init__(self, bodyelement):
        super().__init__(bodyelement, self)
