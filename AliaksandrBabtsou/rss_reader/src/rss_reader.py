import dataclasses
import json
import pkg_resources
import argparse
import sys
from src import log
import sys
from src.models import Feed, ListFeeds
from src.utilits import Colors
from src.parser_xml import read_rss
from src.local_storage import LocalStorage
from src.pdf import PDF
from src.print_to_html import print_HTML


@log.log_decorator
def parse_args(args: list):
    """[Parsing the input data]

    Args:
        args (list): [input data]

    Returns:
        [argparse ]
    """
    parser = argparse.ArgumentParser(
        description='Pure Python command-line RSS reader.')
    parser.add_argument('--version', action='store_true', required=False,
                        help='Print version info')
    parser.add_argument('--json', action='store_true',  required=False,
                        help='Print result as JSON in stdout')
    parser.add_argument('--verbose', action='store_true',  required=False,
                        help='Outputs verbose status messages')
    parser.add_argument('--limit', action='store', type=int, required=False,
                        help='Limit news topics if this parameter provided')
    parser.add_argument('--date', action='store', type=str, required=False,
                        help="Date in <20191020> format means actual publishing date the news.")
    parser.add_argument('--to-pdf', action='store_true', required=False,
                        help="PDF which format will be generated")
    parser.add_argument('--to-html', action='store_true', required=False,
                        help="HTML which format will be generated")
    parser.add_argument('--colorize', action='store_true', required=False,
                        help="print the result of the utility in colorized mode")
    parser.add_argument('source', nargs='?', help='RSS URL')
    return parser.parse_args(args)


@log.log_decorator
def get_version() -> str:
    """[Rotate the package version]

    Returns:
        str: [version]
    """
    version = f"Version { pkg_resources.require('rss_reader')[0].version}"
    return version


def format_output(_rss_out: Feed, json_out: bool, colors: Colors) -> None:
    """[Printing output to standard output]

    Args:
        _rss_out (Feed): [Received data from the parser]
        json_out (bool): [format output or json or ....]
        colors (Colors): [Coloring or not]
    """
    def print_out(feed: Feed) -> None:
        print(f'{colors.red}Feed: {feed.feed_title}')
        for item in feed.items:
            print(f'{colors.blue}Title: {item.item_title}')
            print(f'{colors.green}Date: {item.date}')
            print(f'{colors.orange}Link: {item.link}')
            print(f'{colors.purple}[ {item.description}]')
            print(f'{colors.red}Links:')
            for idx, link in enumerate(item.links):
                print(f'[{idx+1}] {link}')
            print('\n')

    if json_out:
        print(json.dumps(dataclasses.asdict(_rss_out), ensure_ascii=False))
    else:
        if isinstance(_rss_out, ListFeeds):
            for feed in _rss_out.feeds:
                print_out(feed)
        else:
            print_out(_rss_out)
    print(colors.blue)


@log.log_decorator
def main():
    conf = parse_args(sys.argv[1:])
    if conf.colorize:
        colors = Colors(True)
    else:
        colors = Colors(False)
    if conf.verbose:
        log.logger.addHandler(log.log_stream)
    if conf.version:
        print(get_version())

    ls = LocalStorage('rss.data')
    if conf.date:
        if conf.source:
            rss_out = ls.read_url(conf.source, conf.date, conf.limit)
        else:
            rss_out = ls.read_all(conf.date, conf.limit)
    else:
        rss_out = read_rss(conf.source, limit=conf.limit)

        ls.append(rss_data=rss_out)

    format_output(rss_out, json_out=conf.json, colors=colors)

    if conf.to_pdf:
        pdf = PDF()
        if isinstance(rss_out, ListFeeds):
            for feed in rss_out.feeds:
                pdf.print_page(feed)
        else:
            pdf.print_page(rss_out)
        pdf.output('report.pdf', 'F')

    if conf.to_html:
        print_HTML(rss_out)


if __name__ == '__main__':

    main()
