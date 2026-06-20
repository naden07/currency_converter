from converter import FreeCurrencyConverter, PremiumCurrencyConverter

def main():
    # Instantiate our OOP objects imported from converter.py
    free_converter = FreeCurrencyConverter()
    premium_converter = PremiumCurrencyConverter()

    # Pre-fetch list using our encapsulated object
    currencies = free_converter.get_currencies()

    print("--- Welcome to the OOP Currency Converter! ---")
    print("list    - lists the different currencies")
    print("convert - convert from one currency to another (Standard API)")
    print("premium - convert using the Premium Converter (Polymorphism Demo)")
    print("rate    - get the exchange rate of two currencies")
    print("----------------------------------------------")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            print("Goodbye!")
            break
        elif command == "list":
            free_converter.print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            free_converter.convert(currency1, currency2, amount)
        elif command == "premium":
            # Testing out polymorphism dynamically!
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            premium_converter.convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            free_converter.fetch_rate(currency1, currency2)
        else:
            print("Unrecognized command!")


if __name__ == "__main__":
    main()