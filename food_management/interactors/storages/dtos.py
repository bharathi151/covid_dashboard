from datetime import date
from dataclasses import dataclass
from typing import Optional, List


@dataclass()
class ItemDto:
    item_id: int
    quantity: int

@dataclass()
class PreferedItemsQuantitiesDto:
    items_quantities : List[ItemDto]

@dataclass()
class NegativeQuantityItemsDto:
    negative_quantities_items: List[ItemDto]
