import sys
import re
import os.path
from optparse import OptionParser, OptionGroup

from work import process


class Config(object):
    # settings
    SIM_THRESHOLD = -1
    MIN_CHILDREN_COUNT = -1
    MIN_DEEP = -1
    MIN_SIMILAR_COUNT = -1
    url = ''
    webdriver = ''
    chromeDriverPath = ''
    parser = None
    # options
    usage = 'Usage: %prog <URL> [-w workfile] [options]'
    parser_system_options = [
        # system
        {
            "short": "-w",
            "long": "--work-file",
            "action": "store",
            "dest": "workFile",
            "default": "./work.py",
            "help": "Work file path",
            "type": "string"
        },
        {
            "short": "--sim-threshold",
            "action": "store",
            "dest": "threshold",
            "default": 0.75,
            "help": "Similarity threshold",
            "type": "float"
        },
        {
            "short": "--min-children-count",
            "action": "store",
            "dest": "minChildrenCount",
            "default": 4,
            "help": "Min children count of a DOM",
            "type": "int"
        },
        {
            "short": "--min-children-deep",
            "action": "store",
            "dest": "minDeep",
            "default": 2,
            "help": "Minimum deep of children of a DOM",
            "type": "int"
        },
        {
            "short": "--min-similar-count",
            "action": "store",
            "dest": "minSimilar",
            "default": 1,
            "help": "Minimum count of a set of similar DOMs",
            "type": "int"
        },
    ]
    parser_options = [
        {
            "short": "-d",
            "long": "--webdriver",
            "action": "store",
            "dest": "webdriver",
            "default": "phantomjs",
            "help": "Web Driver",
            "type": "string"
        },
        {
            "short": "--chrome-driver-path",
            "action": "store",
            "dest": "chromeDriverPath",
            "default": "./chromedriver",
            "help": "Chromedriver path",
            "type": "string"
        },
    ]

    def __init__(self, args):
        self.verify(args)

    def verify(self, args):
        parser = OptionParser(usage=self.usage)
        self.parser = parser
        for opt in self.parser_options:
            parser.add_option(
                opt['short'],
                opt.get('long', None),
                action=opt['action'],
                dest=opt['dest'],
                default=opt['default'],
                help=opt['help'],
                type=opt['type'])
        group = OptionGroup(
            parser, "Other options",
            "Caution: These options usually use default values.")
        for opt in self.parser_system_options:
            group.add_option(
                opt['short'],
                opt.get('long', None),
                action=opt['action'],
                dest=opt['dest'],
                default=opt['default'],
                help=opt['help'],
                type=opt['type'])
        parser.add_option_group(group)
        (options, args) = parser.parse_args(args)
        # url
        if len(args) < 2:
            parser.print_help()
            parser.error("Need URL")
        self.url = args[1]
        m = re.match(
            r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)' +
            r'(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s(' +
            r')<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',
            self.url
        )
        if m is None:
            parser.print_help()
            parser.error("Invalid URL")
        # work file
        self.workFile = options.workFile
        if not os.path.isfile(self.workFile):
            parser.print_help()
            parser.error("Work file " + self.workFile + " is not exist")
        # other
        self.SIM_THRESHOLD = options.threshold
        self.MIN_CHILDREN_COUNT = options.minChildrenCount
        self.MIN_DEEP = options.minDeep
        self.MIN_SIMILAR_COUNT = options.minSimilar
        self.webdriver = options.webdriver
        self.chromeDriverPath = options.chromeDriverPath


if __name__ == "__main__":
    conf = Config(sys.argv)
    process(conf)
