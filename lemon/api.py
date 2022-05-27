from lemon.config import LIVE_TRADING_API_URL, MARKET_DATA_API_URL, Config
from lemon.market_data.api import MarketDataApi
from lemon.trading.api import TradingApi


class Api:
    def __init__(self, config: Config):
        self._config = config

    @property
    def market_data(self) -> MarketDataApi:
        return MarketDataApi(self._config)

    @property
    def trading(self) -> TradingApi:
        return TradingApi(self._config)


def create(
    api_token: str,
    market_data_api_url: str = MARKET_DATA_API_URL,
    trading_api_url: str = LIVE_TRADING_API_URL,
) -> Api:
    return Api(
        Config(
            api_token=api_token,
            market_data_api_url=market_data_api_url,
            trading_api_url=trading_api_url,
        )
    )
