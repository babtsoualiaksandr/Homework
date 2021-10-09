from dataclasses import dataclass
import dataclasses
import json
import pkg_resources
import argparse
import sys
import log
import sys
from models import Feed
from parser_xml import read_rss
from local_storage import LocalStorage


@log.log_decorator
def parse_args(args: list) -> list:
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
    parser.add_argument('source', nargs='?', help='RSS URL')
    return parser.parse_args(args)


@log.log_decorator
def get_version() -> str:
    version = f"Version { pkg_resources.require('rss_reader')[0].version}"
    return version


def format_output(_rss_out: Feed, json_out: bool) -> None:

    def print_out(feed: Feed) -> None:
        print('Feed:', feed.Feed, '\n')
        for item in feed.items:
            print('Title:', item.Title)
            print('Date:', item.Date)
            print('Link:', item.Link, '\n')

            print(f"[{item.description}]", '\n')
            print('Links:'),

            for idx, link in enumerate(item.Links):
                print(f'[{idx+1}] {link}')
            print('\n')

    if json_out:
        print(json.dumps(dataclasses.asdict(_rss_out), ensure_ascii=False))
    else:
        if isinstance(_rss_out, list):
            for feed in _rss_out:
                print_out(feed)
        else:
            print_out(_rss_out)


@log.log_decorator
def main():
    conf = parse_args(sys.argv[1:])
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
    format_output(rss_out, json_out=conf.json)


if __name__ == '__main__':

    main()
