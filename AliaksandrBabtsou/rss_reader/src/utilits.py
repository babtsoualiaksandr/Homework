from typing import List, final
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
