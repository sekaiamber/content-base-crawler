# This is an example to get bilibili page
# $ python3 setup.py 'http://www.bilibili.com/video/bangumi-two-1.html' -d chrome -w examples/bilibili.py


from work.domSignaturer import DomSignaturer
from work.webpage import WebPage
from work.utils import editDistance


# get body element
body = driver.find_element_by_css_selector('.vd-list-cnt')
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
