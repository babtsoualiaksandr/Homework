import log
from models import ListFeeds
from parser_xml import read_rss
from pdf import PDF
from print_to_html import print_HTML


@log.log_decorator
def get_news_from_url(url: str = None, limit: int = None, format: str = 'json'):
    print('format', format)
    result = read_rss(url, limit)
    if format == 'pdf':
        pdf = PDF()
        if isinstance(result, ListFeeds):
            for feed in result.feeds:
                pdf.print_page(feed)
        else:
            pdf.print_page(result)
        pdf.output('report.pdf', 'F')
    print(format, '$'*123)
    if format == 'html':
        print_HTML(result)

    return result
