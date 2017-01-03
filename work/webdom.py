from .domSignaturer import DomSignaturer


class WebDom:
    children = []
    classes = []
    parent = None

    def __init__(self, webelement, parent, webpage, deep=0):
        self.webelement = webelement
        self.webpage = webpage
        self.parent = parent
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
        self.children = [WebDom(
            e, self, webpage, self.deep + 1
        ) for e in children]

    def getSelfSignature(self):
        domSignaturer = DomSignaturer()
        return domSignaturer.getDomSignature(self.tagName, self.classes)

    def getSignature(self):
        signs = [self.getSelfSignature()]
        signs.extend([child.getSignature() for child in self.children])
        return ''.join(signs)

    def getRootSelector(self):
        selector = self.getSelector()
        parent = self.parent
        while parent is not None:
            selector = parent.getSelector() + '>' + selector
            parent = parent.parent
        return selector

    def getSelector(self):
        return (
            self.tagName +
            ''.join(['.' + className for className in self.classes])
        )

    def print(self):
        print(
            '  ' * self.deep +
            self.getSelector() +
            '(' + self.getRootSelector() + ')'
        )
        for child in self.children:
            child.print()
