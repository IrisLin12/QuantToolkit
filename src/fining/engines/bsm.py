# Author: Iris Lin
# Date: 2026-07
# Description: BlackScholes Model caculation

import numpy as np
from scipy.stats import norm
from fining.dataclasses import MarketData, OptionType
from fining.engines.base import PricingEngine

class BlackScholesMertonEngine(PricingEngine): 
    @staticmethod
    def _d1(data: MarketData) -> float:
        return (np.log(data.S / data.K) + (data.r - data.q + 0.5 * data.sigma ** 2) * data.T) / (data.sigma * np.sqrt(data.T))
    
    @staticmethod
    def _d2(data: MarketData) -> float:
        return BlackScholesMertonEngine._d1(data) - data.sigma * np.sqrt(data.T)

    def calculate_price(self, data: MarketData, option_type: OptionType) -> float:
        d1 = self._d1(data)
        d2 = self._d2(data)

        if option_type == OptionType.CALL:
            return data.S * np.exp(-data.q * data.T) * norm.cdf(d1) - data.K * np.exp(-data.r * data.T) * norm.cdf(d2)
        elif option_type == OptionType.PUT:
            return data.K * np.exp(-data.r * data.T) * norm.cdf(-d2) - data.S * np.exp(-data.q * data.T) * norm.cdf(-d1)
        else:
            raise ValueError(f"Does't allowed: {option_type}")
