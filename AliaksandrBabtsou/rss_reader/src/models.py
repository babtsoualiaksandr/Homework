from dataclasses import dataclass



@dataclass(frozen=True)
class Item:
    Title: str
    Date: str
    Link: str
    description: str
    Links: list[str]


@dataclass(frozen=True)
class Feed:
    url: str
    Feed: str
    items: list[Item]

@dataclass(frozen=True)
class ListFeeds:
    Feeds:list[Feed]        





