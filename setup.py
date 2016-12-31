import sys
import re
from optparse import OptionParser, OptionGroup


class Config(object):
    # settings
    SIM_THRESHOLD = -1
    CHILDREN_COUNT = -1
    url = ''
    # options
    usage = 'Usage: %prog <URL> [options]'
    parser_system_options = [
        # system
        {
            "short": "--sim-threshold",
            "action": "store",
            "dest": "threshold",
            "default": 10,
            "help": "Similarity threshold",
            "type": "int"
        },
        {
            "short": "--children-count",
            "action": "store",
            "dest": "childrenCount",
            "default": 6,
            "help": "Min children count of a DOM",
            "type": "int"
        },
    ]
    parser_options = []

    def __init__(self, args):
        self.verify(args)

    def verify(self, args):
        parser = OptionParser(usage=self.usage)
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
        # other
        self.SIM_THRESHOLD = options.threshold
        self.CHILDREN_COUNT = options.childrenCount


if __name__ == "__main__":
    conf = Config(sys.argv)
