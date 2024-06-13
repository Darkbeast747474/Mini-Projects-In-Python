import requests
class CurrencyConverter:
    '''
       api_key: Your API Key
       base_currency : Default USD.
    '''
    def __init__(self, api_key, base_currency='USD'):
        self.api_key = api_key
        self.base_currency = base_currency
        self.conversion_rates = {}
        self.update_rates(base_currency)

    def update_rates(self, base_currency):
        '''Fetches the Conversion rates'''
        self.base_currency = base_currency
        api_url = f'https://v6.exchangerate-api.com/v6/{self.api_key}/latest/{base_currency}'
        response = requests.get(api_url)
        if response.status_code == 200:
            self.conversion_rates = response.json().get('conversion_rates', {})
        else:
            raise Exception("Failed to fetch conversion rates")

    def convert(self, amount, from_currency, to_currency):
        '''
            Converts the One Currency amount to the Base currency (By default USD) and returns amount as it is, 
            if Base currency Amount is given         
        '''
        if from_currency != self.base_currency:
            self.update_rates(from_currency)

        if to_currency == self.base_currency:
            rate = self.conversion_rates.get(to_currency, None)
            if rate:
                return amount / rate
            else:
                raise ValueError(f"Conversion rate for {to_currency} not found")
        else:
            rate_to = self.conversion_rates.get(to_currency, None)
            if rate_to:
                return amount * rate_to
            else:
                raise ValueError(f"Conversion rate for {to_currency} not found")

    def get_conversion_rate(self, currency):
        '''Fetches the Specific conversion rate'''
        return self.conversion_rates.get(currency, None)

# Example usage
converter = CurrencyConverter('Your API Key')

# Convert 100 USD to EUR
amount_in_eur = converter.convert(100, "USD", "EUR")
print(f"100 USD is equal to {amount_in_eur:.2f} EUR")

# Convert 100 EUR to USD
amount_in_usd = converter.convert(100, "EUR", "USD")
print(f"100 EUR is equal to {amount_in_usd:.2f} USD")

# Convert 100 EUR to JPY
amount_in_jpy = converter.convert(100, "EUR", "JPY")
print(f"100 EUR is equal to {amount_in_jpy:.2f} JPY")