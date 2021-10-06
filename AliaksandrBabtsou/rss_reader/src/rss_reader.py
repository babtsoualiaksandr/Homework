import json
import pkg_resources
import argparse
import sys 
import log
import sys
from parser_xml import read_rss
import pprint
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


def format_output(rss_out:object, json_out:bool)->None:
    if json_out:
        print(json.dumps(rss_out,ensure_ascii=False))
    else:
        print('Feed:',rss_out[0]['Feed'],'\n')
        for item in rss_out[0]['items']:
            print('Title:',item['Title'])
            print('Date:',item['Date'])
            print('Link:',item['Link'],'\n')

            print('[',item['describe_link']['description'],']','\n')
            print('Links:'),
            
            for idx, link in enumerate(item['Links']):
                print(f'[{idx+1}] {link}')



#Feed: Yahoo News - Latest News & Headlines

#Title: Nestor heads into Georgia after tornados damage Florida
#Date: Sun, 20 Oct 2019 04:21:44 +0300
#Link: https://news.yahoo.com/we
# t-weekend-tropical-storm-warnings-131131925.html

#[image 2: Nestor heads into Georgia after tornados damage Florida][2]Nestor raced across Georgia as a post-tropical cyclone late Saturday, hours after the former tropical storm spawned a tornado that damaged
#homes and a school in central Florida while sparing areas of the Florida Panhandle devastated one year earlier by Hurricane Michael. The storm made landfall Saturday on St. Vincent Island, a nature preserve
#off Florida's northern Gulf Coast in a lightly populated area of the state, the National Hurricane Center said. Nestor was expected to bring 1 to 3 inches of rain to drought-stricken inland areas on its
#march across a swath of the U.S. Southeast.


#Links:
#[1]: https://news.yahoo.com/wet-weekend-tropical-storm-warnings-131131925.html (link)
#[2]: http://l2.yimg.com/uu/api/res/1.2/Liyq2kH4HqlYHaS5BmZWpw--/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media.zenfs.com/en/ap.org/5ecc06358726cabef94585f99050f4f0 (image)


@log.log_decorator
def main():
    conf = parse_args(sys.argv[1:])
    print(conf)
    if conf.verbose:
        log.logger.addHandler(log.log_stream)
    print(get_version())
    rss_out = read_rss(conf.source[0], limit=conf.limit)
    format_output(rss_out, json_out=conf.json)

if __name__ == '__main__':

    main()
