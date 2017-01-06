# This is an example to get Jandan.net index page
# $ python3 setup.py 'http://jandan.net' -d chrome -w examples/jandan.py


from work.domSignaturer import DomSignaturer
from work.webpage import WebPage
from work.utils import editDistance


# get body element
body = driver.find_element_by_css_selector('#content')
timer.addTag('Dom ready')
# build webpage
webpage = WebPage(body)
timer.addTag('Webpage inited')

# test
allsims = webpage.getSimilarBySignature(
    minChildrenCount=config.MIN_CHILDREN_COUNT,
    minChildrenMaxDeep=config.MIN_DEEP,
    threshold=config.SIM_THRESHOLD,
    minSimilarCount=config.MIN_SIMILAR_COUNT
)
for sims in allsims:
    print(sims['selector'])
    for sim in sims['sims']:
        print('    Find dom pattern:')
        for simchild in sim:
            print('        ' + simchild['sign'])

timer.addTag('Show Doms:')
print('\r\n\r\n')
for sims in allsims:
    timer.addTag(sims['selector'])
    for sim in sims['sims']:
        print('    Find dom pattern:')
        for simchild in sim:
            webdom = simchild['dom']
            print('--------------------------------')
            dom = webdom.webelement.text
            print(dom)
