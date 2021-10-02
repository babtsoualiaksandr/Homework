import pkg_resources
import argparse
import sys


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


def get_version():
    version = f"Version { pkg_resources.require('rss_reader')[0].version}"
    return version


def main():
    print(get_version())


if __name__ == '__main__':
    main()
