from .domSignaturer import DomSignaturer


class WebDom:
    children = []
    classes = []

    def __init__(self, webelement, webpage, deep=0):
        self.webelement = webelement
        self.webpage = webpage
        self.deep = deep
        domSignaturer = DomSignaturer()
        # html tag
        self.tagName = webelement.get_attribute('tagName').upper()
        domSignaturer.addHtmlTag(self.tagName)
        # get attributes
        classes = webelement.get_attribute('className')
        if classes is not None:
            self.classes = classes.split()
        for cls in self.classes:
            domSignaturer.addClass(cls)
        # if element's tag is SCRIPT or SVG, skip
        if self.tagName in ['SCRIPT', 'SVG']:
            return
        # build children
        children = webelement.find_elements_by_xpath('./*')
        self.children = [WebDom(e, webpage, self.deep + 1) for e in children]

    def print(self):
        print(
            '  ' * self.deep +
            self.tagName +
            ''.join(['.' + cls for cls in self.classes])
        )
        for child in self.children:
            child.print()
