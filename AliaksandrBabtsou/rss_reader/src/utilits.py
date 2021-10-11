from typing import List
import requests
from requests.models import HTTPError
import log


class FormatRows:
    def __init__(self, text: str, size_page: int) -> None:
        self.text = text
        self.size_page = size_page
        self.pages = [text[idx:idx+size_page]
                      for idx in range(0, len(text), size_page)]
        self.page_count = len(self.pages)
        self.item_count = len(text)

    def count_items_on_page(self, page_number: int) -> int:
        try:
            return len(self.pages[page_number])
        except IndexError:
            return f'Exception: Invalid index. Page is missing.'

    def find_page(self, search_str: str) -> List[int]:
        idxes_start = [i for i in range(len(self.text)) if self.text.startswith(search_str, i)]
        if not len(idxes_start):
            return f"Exception: '{search_str}' is missing on the pages"
        else:
            result = set()
            for idx in idxes_start:
                print(idx)
                result.add(idx//self.size_page)
                result.add((idx+len(search_str))//self.size_page)
            return list(result)

    def display_page(self, page_number: int) -> str:
        return self.pages[page_number]

    def __repr__(self) -> str:
        return f'{self.__class__.__name__ }({self.text},{self.size_page!r})'


def get_rows_from_text(text: str, len_row: int) -> list[str]:
    formatRows = FormatRows(text, len_row)
    return formatRows.pages


@log.log_decorator
def is_url_image(image_url: str) -> bool:
    result = False
    try:
        image_formats = ("image/png", "image/jpeg", "image/jpg")
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}
        req = requests.get(image_url, headers=headers, timeout=5)
    except Exception as err:
        print(err)
        result = False
    else:
        if req.headers["content-type"] in image_formats:
            result = True
    return result


class Colors:

    def __init__(self, is_color: bool = False):
        if is_color:
            self.black = '\033[30m'
            self.red = '\033[31m'
            self.green = '\033[32m'
            self.orange = '\033[33m'
            self.blue = '\033[34m'
            self.purple = '\033[35m'
            self.cyan = '\033[36m'
            self.lightgrey = '\033[37m'
            self.darkgrey = '\033[90m'
            self.lightred = '\033[91m'
            self.lightgreen = '\033[92m'
            self.yellow = '\033[93m'
            self.lightblue = '\033[94m'
            self.pink = '\033[95m'
            self.lightcyan = '\033[96m'
        else:
            self.black = None
            self.red = None
            self.green = None
            self.orange = None
            self.blue = None
            self.purple = None
            self.cyan = None
            self.lightgrey = None
            self.darkgrey = None
            self.lightred = None
            self.lightgreen = None
            self.yellow = None
            self.lightblue = None
            self.pink = None
            self.lightcyan = None
            