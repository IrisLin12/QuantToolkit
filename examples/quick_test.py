import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from fining import MarketData, OptionType, BlackScholesMertonEngine

def main():
    market_data = MarketData(S=100.0, K=100.0, T=1.0, r=0.05, sigma=0.20, q=0.02)
    bsm_engine = BlackScholesMertonEngine()

    call_price = bsm_engine.calculate_price(market_data, OptionType.CALL)
    put_price = bsm_engine.calculate_price(market_data, OptionType.PUT)

    print(f" Call price: ${call_price:.4f}")
    print(f" Put price: ${put_price:.4f}")

if __name__ == "__main__":
    main()
