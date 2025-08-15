from dataclasses import dataclass
from typing import Optional, List


def replace_formatting(old_string: str):
    return ' '.join(old_string.split())


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
    branches: Optional[str] = None

    def asdict(self):
        result = {}
        result['number'] = str(self.number)
        result['link'] = str(self.link)
        result['dt_start'] = str(replace_formatting(self.dt_start))
        result['dt_end'] = str(replace_formatting(self.dt_end))
        result['description'] = str(replace_formatting(self.description))
        result['address'] = str(replace_formatting(self.address))
        result['region'] = str(replace_formatting(self.region))
        result['starting_price'] = str(self.starting_price)
        result['branches'] = str(replace_formatting(self.branches))
        return result

