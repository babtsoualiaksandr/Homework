from src import log
from src.models import Feed, ListFeeds
from src.parser_xml import read_rss
from src.pdf import PDF
from src.print_to_html import print_HTML


@log.log_decorator
def get_news_from_url(url: str = None, limit: int = None, format: str = 'json') -> Feed:
    """[Get data from rss url]

    Args:
        url (str, optional): [url]. Defaults to None.
        limit (int, optional): [Number of news]. Defaults to None.
        format (str, optional): [output format (json, pdf, html)]. Defaults to 'json'.

    Returns:
        Feed: [Data of Feed]
    """
    result = read_rss(url, limit)
    if format == 'pdf':
        pdf = PDF()
        if isinstance(result, ListFeeds):
            for feed in result.feeds:
                pdf.print_page(feed)
        else:
            pdf.print_page(result)
        pdf.output('report.pdf', 'F')
    if format == 'html':
        print_HTML(result)
    return result
