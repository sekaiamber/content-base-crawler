# This is an example to get taobao index page
# $ python3 setup.py 'https://s.taobao.com/list?spm=a219r.lm872.0.0.eTjwG1&q=%E6%89%8B%E6%9C%BA&spu_title=%E5%B0%8F%E7%B1%B3+%E5%B0%8F%E7%B1%B3Max&app=detailproduct&pspuid=1346576&cat=1512&from_pos=20_1512.default_0_43_1346576&from_type=3c&spu_style=grid' -d chrome -w examples/taobao.py


from work.domSignaturer import DomSignaturer
from work.webpage import WebPage
from work.utils import editDistance


# get body element
body = driver.find_element_by_css_selector('body')
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
