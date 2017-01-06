from .webdom import WebDom


class WebPage(WebDom):
    def __init__(self, bodyelement):
        super().__init__(bodyelement, None, self)

    def getSimilarBySignature(self, **argd):
        sims = super().getSimilarBySignature(**argd)
        return sims
