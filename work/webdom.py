from .domSignaturer import DomSignaturer
from .utils import editDistance


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

    def getChildrenMaxDeep(self):
        if len(self.children) == 0:
            return 0
        else:
            deeps = [child.getChildrenMaxDeep() for child in self.children]
            return max(deeps) + 1

    # get similar dom by their signature
    def getSimilarBySignature(self, **argd):
        sims = []
        if not argd['minChildrenCount'] > len(self.children):
            # get valid children
            children = [
                child for child in self.children
                if child.getChildrenMaxDeep() >= argd['minChildrenMaxDeep']
            ]
            if not argd['minChildrenCount'] > len(children):
                # classification
                children = [{
                    'dom': child,
                    'sign': child.getSignature()
                } for child in children]
                for child in children:
                    isAdd = False
                    for sim in sims:
                        edsums = sum([editDistance(
                            simchild['sign'],
                            child['sign'],
                            len(simchild['sign']),
                            len(child['sign'])
                        ) for simchild in sim])
                        edavg = edsums / len(sim)
                        if edavg / len(child['sign']) < 1 - argd['threshold']:
                            sim.append(child)
                            isAdd = True
                            break
                    if not isAdd:
                        sims.append([child])
                sims = [sim for sim in sims if len(sim) > argd['minSimilarCount']]
                if len(sims) > 0:
                    sims = [{
                        'selector': self.getSelector(),
                        'sims': sims
                    }]
        for child in self.children:
            child_sims = child.getSimilarBySignature(**argd)
            sims.extend(child_sims)
        return sims

    def print(self):
        print(
            '  ' * self.deep +
            self.getSelector()
        )
        for child in self.children:
            child.print()
