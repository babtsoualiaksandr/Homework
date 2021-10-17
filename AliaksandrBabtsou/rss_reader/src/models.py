from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    """[list news from link feed]
    """
    item_title: str
    date: str
    link: str
    description: str
    links: list[str]


@dataclass(frozen=True)
class Feed:
    """[Data from RSS]
    """
    url: str
    feed_title: str
    items: list[Item]


@dataclass(frozen=True)
class ListFeeds:
    """[Model list of Feed]
    """
    feeds: list[Feed]
