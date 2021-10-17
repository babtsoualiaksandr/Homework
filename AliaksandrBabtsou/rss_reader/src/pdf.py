from fpdf import FPDF
from datetime import date
from contextlib import suppress

from requests.models import HTTPError

from src.models import Feed, ListFeeds
import pkg_resources
from src.utilits import FormatRows, get_rows_from_text, is_url_image
from urllib.request import urlopen


class PDF(FPDF):
    """[create file PDF]

    Args:
        FPDF ([type]): [use FPDF]
    """

    def __init__(self):
        """[pdf A4 use font for Cyrillic]
        """
        super().__init__()
        self.WIDTH = 210
        self.HEIGHT = 297
        path_tp_font = 'static/fonts/DejaVuSans-Bold.ttf'
        font_DejaVu = pkg_resources.resource_filename(__name__, path_tp_font)
        self.add_font('DejaVu', '', font_DejaVu, uni=True)
        path_tp_logo = 'static/EPAM_logo.png'
        self.filelogo = pkg_resources.resource_filename(__name__, path_tp_logo)

    def header(self):
        """[Header Each page]
        """
        self.image(self.filelogo, 10, 8, 33)
        self.set_font('DejaVu', size=12)
        self.cell(self.WIDTH - 80)
        self.cell(0, 8, 'Introduction to Python. Final task', border=False, ln=True, align='R', )
        self.set_font('DejaVu', '', 7)
        self.cell(0, 1, f'{date.today()}', border=False, ln=True, align='R', )
        self.ln(1)

    def footer(self):
        """[Footer Each page]
        """
        self.set_y(-15)
        self.set_font('DejaVu', '', 8, )
        self.set_text_color(128)
        self.cell(0, 10, f'Page: {self.page_no()}', border=0, ln=False, align='C')

    def _print_row(self, char_first: str, txt: str, len_row=80) -> None:
        """[Display lines of specified width]

        Args:
            char_first (str): [Line header]
            txt (str): [Text]
            len_row (int, optional): [Line length]. Defaults to 80.
        """
        for idx, row in enumerate(get_rows_from_text(txt, len_row-len(char_first)-1)):
            if idx == 0:
                self.cell(0, 5, f'{char_first}{row}', ln=True)
            else:
                self.cell(0, 5, f'{" "*len(char_first)}{row}', ln=True)

    def page_body(self, feed: Feed):
        """[Body of the page]

        Args:
            feed (Feed): [Data RSS]
        """
        self.set_font(family='DejaVu', style='', size=10)
        self.set_text_color(0, 153, 176)
        self._print_row('Url: ', feed.url)
        self.ln(1)
        self.set_text_color(0, 128, 255)
        self._print_row('Feed: ', feed.feed_title)
        self.ln(1)
        for item in feed.items:
            self.set_text_color(0, 0, 0)
            self._print_row('  Title: ', item.item_title)
            self._print_row('  Date: ', item.date)
            self._print_row('  Link: ', item.link)
            self._print_row('  ', item.description)
            self.ln(1)
            self.set_text_color(51, 0, 102)
            self.cell(0, 5, f'  Links: ', ln=True)
            for idx, link in enumerate(item.links):
                self._print_row(f'   ', f'[{idx+1}]: {link}', 80)
                if is_url_image(link):
                    with suppress(HTTPError):
                        self.image(name=link, link=link, w=self.WIDTH-30)
            self.ln(3)

    def print_page(self, feed: Feed):
        """[Generates the report]

        Args:
            feed (Feed): [Data RSS]
        """
        # Generates the report
        self.add_page()
        self.set_auto_page_break(auto=True, margin=10)
        self.set_font('DejaVu', '', 8, )
        self.page_body(feed)


if __name__ == '__main__':
    pass
