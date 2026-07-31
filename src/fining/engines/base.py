# Author: Iris Lin
# Date: 2026-07
# Description: Define the abc class of pricingEngine

from abc import ABC, abstractmethod
from fineng.dataclasses import MarketData, OptionType

class PricingEngine(ABC):
    @abstractmethod
    def calculate_price(self, data: MarketData, option_type: OptionType) -> float:
        raise NotImplementedError
