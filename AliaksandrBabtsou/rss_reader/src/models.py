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
    feeds:list[Feed]   




class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[90m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m' 
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan='\033[96m'    





