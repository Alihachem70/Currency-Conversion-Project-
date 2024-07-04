import requests

API_KEY = 'fca_live_ryJ4c3Vf2YdITpGRBL2zRFuG51QSB6K3WRlBWB8U'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = {
    "AUD": "Australian Dollar",
    "BGN": "Bulgarian Lev",
    "BRL": "Brazilian Real",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "CZK": "Czech Koruna",
    "DKK": "Danish Krone",
    "EUR": "Euro",
    "GBP": "British Pound Sterling",
    "HKD": "Hong Kong Dollar",
    "HRK": "Croatian Kuna",
    "HUF": "Hungarian Forint",
    "IDR": "Indonesian Rupiah",
    "ILS": "Israeli New Shekel",
    "INR": "Indian Rupee",
    "ISK": "Icelandic Króna",
    "JPY": "Japanese Yen",
    "KRW": "South Korean Won",
    "MXN": "Mexican Peso",
    "MYR": "Malaysian Ringgit",
    "NOK": "Norwegian Krone",
    "NZD": "New Zealand Dollar",
    "PHP": "Philippine Peso",
    "PLN": "Polish Złoty",
    "RON": "Romanian Leu",
    "RUB": "Russian Ruble",
    "SEK": "Swedish Krona",
    "SGD": "Singapore Dollar",
    "THB": "Thai Baht",
    "TRY": "Turkish Lira",
    "USD": "United States Dollar",
    "ZAR": "South African Rand"
}


def print_currencies_table(currencies):
    print("{:<10} {:<40}".format("Code", "Currency Name"))
    print("-" * 50)
    for code, name in currencies.items():
        print("{:<10} {:<40}".format(code, name))


def convert_currency(base):
    if base not in CURRENCIES:
        print(f"Invalid base currency: {base}")
        return

    currencies_str = ",".join(CURRENCIES.keys())
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies_str}"
    try:
        response = requests.get(url)
        data = response.json()
        if 'data' in data:
            rates = data['data']
            print(f"Exchange rates for {base}:")
            for currency, rate in rates.items():
                print(f"{base} -> {currency}: {rate}")
        else:
            print("Error: 'data' key not found in the response.")
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")


# Print the currencies table
print_currencies_table(CURRENCIES)

# Main loop to convert currencies until user decides to stop
while True:
    print("\nType 'q' to quit.")
    base_currency = input("Enter the base currency code from the table above: ").upper()

    if base_currency == 'Q':
        break

    convert_currency(base_currency)
