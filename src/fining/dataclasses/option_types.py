# Author: Iris Lin
# Date: 2026-07
# Description: option type and market data class defination

from enum import Enum
from dataclasses import dataclass

class OptionType(Enum):
    CALL = 'call'
    PUT = 'put'

class ExeriseType(Enum):
    EUROPEAN = 'european'
    AMERICAN = 'american'

@dataclass(frozen = True)
class MarketData:
    S: float
    K: float
    T: float
    r: float
    sigma: float
    q: float = 0.0

    def __post_init__(self):
        if self.S <= 0:
            raise ValueError
        if self.K <= 0:
            raise ValueError
        if self.T <= 0:
            raise ValueError
        if self.sigma <= 0:
            raise ValueError
        if self.q < 0:
            raise ValueError
