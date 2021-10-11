from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    item_title: str
    date: str
    link: str
    description: str
    links: list[str]


@dataclass(frozen=True)
class Feed:
    url: str
    feed_title: str
    items: list[Item]


@dataclass(frozen=True)
class ListFeeds:
    feeds: list[Feed]


