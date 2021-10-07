import json
import pkg_resources
import argparse
import sys 
import log
import sys
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
def get_version()-> str:
    version = f"Version { pkg_resources.require('rss_reader')[0].version}"
    return version


def format_output(rss_out:object, json_out:bool)->None:
    def print_out(feed:dict)->None:
        print('Feed:',feed['Feed'],'\n')
        for item in feed['items']:
            print('Title:',item['Title'])
            print('Dte:',item['Date'])
            print('Link:',item['Link'],'\n')

            print(f"[{item['describe_link']['description']}]",'\n')
            print('Links:'),
                    
            for idx, link in enumerate(item['Links']):
                print(f'[{idx+1}] {link}')
            print('\n')

    if json_out:
        print(json.dumps(rss_out,ensure_ascii=False))
    else:
        if isinstance(rss_out, list):            
            for feed in rss_out:
                print_out(feed)
        else:
            print_out(rss_out)


@log.log_decorator
def main():
    conf = parse_args(sys.argv[1:])
    if conf.limit is not None:
        conf.limit-=1
    print(conf)
    if conf.verbose:
        log.logger.addHandler(log.log_stream)
    if conf.version:
        print(get_version())
    
    ls = LocalStorage('rss.json')
    if conf.date:
        if conf.source:
            rss_out = ls.read_url(conf.source, conf.date, conf.limit)
        else:
            rss_out =ls.read_all(conf.date, conf.limit)
    else:
        rss_out = read_rss(conf.source, limit=conf.limit)    
        ls.append(rss_data=rss_out)
    format_output(rss_out, json_out=conf.json)

if __name__ == '__main__':

    main()
