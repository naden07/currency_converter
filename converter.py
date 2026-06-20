from requests import get
from pprint import PrettyPrinter
from abc import ABC, abstractmethod

# ABSTRACTION
class BaseConverter(ABC):
    @abstractmethod
    def fetch_rate(self, currency1, currency2):
        """Hides complex API fetching details."""
        pass

# ENCAPSULATION & INHERITANCE
class FreeCurrencyConverter(BaseConverter):
    def __init__(self):
        # ENCAPSULATION: Sensitive API credentials are kept private
        self.__base_url = "https://free.currconv.com/"
        self.__api_key = "562ddaf40c95f5d58108"
        self.printer = PrettyPrinter()

    def get_currencies(self):
        endpoint = f"api/v7/currencies?apiKey={self.__api_key}"
        url = self.__base_url + endpoint
        try:
            data = get(url).json()['results']
            data = list(data.items())
            data.sort()
            return data
        except Exception as e:
            print(f"Error connecting to API: {e}")
            return []

    def print_currencies(self, currencies):
        for name, currency in currencies:
            name = currency['currencyName']
            _id = currency['id']
            symbol = currency.get("currencySymbol", "")
            print(f"{_id} - {name} - {symbol}")

    def fetch_rate(self, currency1, currency2):
        endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={self.__api_key}"
        url = self.__base_url + endpoint

        try:
            data = get(url).json()
            if len(data) == 0:
                print('Invalid currencies.')
                return None

            rate = list(data.values())[0]
            print(f"{currency1} -> {currency2} = {rate}")
            return rate
        except Exception:
            print("API Error. Please check your internet or API key limits.")
            return None

    def convert(self, currency1, currency2, amount):
        rate = self.fetch_rate(currency1, currency2)
        if rate is None:
            return

        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount.")
            return

        converted_amount = rate * amount
        print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
        return converted_amount

# POLYMORPHISM
class PremiumCurrencyConverter(BaseConverter):
    def fetch_rate(self, currency1, currency2):
        print("\n[PREMIUM SIMULATION] Accessing ultra-fast, dedicated VIP servers...")
        return 1.25  # Simulating a mock premium rate

    def convert(self, currency1, currency2, amount):
        rate = self.fetch_rate(currency1, currency2)
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount.")
            return

        converted_amount = rate * amount
        print(f"[PREMIUM RESULT] {amount} {currency1} is equal to {converted_amount} {currency2}")
        return converted_amount