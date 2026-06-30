import json

class StockPayload:
    def __init__(self, scrip, price, company):
        self.scrip = scrip
        self.price = price
        self.company = company

    # Friendly string for basic logs/terminal outputs
    def __str__(self):
        return f"Stock: {self.scrip} is trading at NPR {self.price}"

    # Detailed debugging string showing state representation
    def __repr__(self):
        return f"StockPayload(scrip='{self.scrip}', price={self.price}, company='{self.company}')"

    # ALTERNATIVE CONSTRUCTOR: Instantiates class straight from a raw API JSON string
    @classmethod
    def from_api_json(cls, json_string):
        # Parse the string into a python dictionary
        parsed_data = json.loads(json_string)
        # Extract variables and inject them back into the main constructor
        return cls(
            scrip=parsed_data.get("symbol"),
            price=float(parsed_data.get("ltp", 0)),
            company=parsed_data.get("company_name")
        )

    # STATIC METHOD: Standalone utility that performs an isolated calculation
    @staticmethod
    def calculate_broker_commission(amount):
        # Standard Nepalese stock broker fee simulation (~0.4%)
        return amount * 0.004


# ---- RUNNING TEST BENCH ----
if __name__ == "__main__":
    # Test 1: Simulating an API string response
    mock_api_response = '{"symbol": "NICA", "company_name": "NIC Asia Bank Limited", "ltp": "488.5"}'
    
    # Using our classmethod constructor
    stock_obj = StockPayload.from_api_json(mock_api_response)
    
    # Test 2: Testing Dunder Output
    print("--- Testing __str__ ---")
    print(stock_obj) 
    
    print("\n--- Testing __repr__ ---")
    print(repr(stock_obj))
    
    # Test 3: Testing Static Utility
    trade_value = stock_obj.price * 100 # Buying 100 shares
    commission = StockPayload.calculate_broker_commission(trade_value)
    print(f"\nBroker Commission for 100 shares: NPR {commission:.2f}")