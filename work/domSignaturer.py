from .utils import singleton


@singleton
class DomSignaturer:
    _dimension = {}

    def _getNewDimension(self):
        return {
            'index': len(self._dimension) + 1,
            'values': []
        }

    def addDimensionValue(self, dimName, value):
        if dimName not in self._dimension:
            self._dimension[dimName] = self._getNewDimension()
        dim = self._dimension[dimName]
        if value not in dim['values']:
            dim['values'].append(value)
        return self.getDimensionValueSign(dimName, value)

    def addClass(self, className):
        self.addDimensionValue('class', className)

    def addHtmlTag(self, tagName):
        self.addDimensionValue('tag', tagName)

    def getDimensionValueSign(self, dimName, value):
        dim = self._dimension.get(dimName, None)
        if dim is None or value not in dim['values']:
            return chr(0)
        return chr(dim['index'] * 1000 + dim['values'].index(value))

    def getDomSignature(self, tagName, classes=[]):
        signs = []
        signs.append(self.getDimensionValueSign('tag', tagName))
        for className in classes:
            signs.append(self.getDimensionValueSign('class', className))
        signs = sorted(signs)
        return ''.join(signs)

    def print(self):
        for k in self._dimension:
            print(k)
            dim = self._dimension[k]
            for v in dim['values']:
                print('  ', v)
