import pkg_resources
import argparse
import sys 
import log
import sys
from parser_xml import read_rss
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
    parser.add_argument('source', nargs='+', help='RSS URL')
    return parser.parse_args(args)

@log.log_decorator
def get_version()-> str:
    version = f"Version { pkg_resources.require('rss_reader')[0].version}"
    return version

@log.log_decorator
def main():
    conf = parse_args(sys.argv[1:])
    print(conf)
    if conf.verbose:
        log.logger.addHandler(log.log_stream)
    print(get_version())
    print(read_rss(conf.source, limit=conf.limit, json_out=conf.json))




if __name__ == '__main__':

    main()
