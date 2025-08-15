from dataclasses import dataclass
from typing import Optional, List


def replace_formatting(old_string: str):
    return ' '.join(old_string.split())

@dataclass
class Branch:
    name: Optional[str] = None

    def format(self):
        return str(replace_formatting(self.name))


@dataclass
class Tender:
    number: Optional[str] = None
    link: Optional[str] = None
    dt_start: Optional[str] = None
    dt_end: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    region: Optional[str] = None
    starting_price: Optional[str] = None
    branches: Optional[List[Branch]] = None

    def asdict(self):
        result = {}
        result['Номер'] = str(self.number)
        result['Адрес'] = str(replace_formatting(self.address))
        result['Регион'] = str(replace_formatting(self.region))
        result['От'] = str(replace_formatting(self.dt_start))
        result['До'] = str(replace_formatting(self.dt_end))
        result['Описание'] = str(replace_formatting(self.description))
        result['Ссылка'] = str(self.link)
        result['Категории'] = [branch.format() for branch in self.branches]
        result['Начальная цена'] = str(self.starting_price)
        return result

