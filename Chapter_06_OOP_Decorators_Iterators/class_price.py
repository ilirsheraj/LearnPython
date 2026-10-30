class Price:
    def final_price(self, vat, discount=0):
        """
        Returns price after applying VAT and a fixed discount
        """
        return (self.net_price * (100 + vat) / 100) - discount

def main():
    # Create an instance
    p1 = Price()
    # Define net price
    p1.net_price = 100

    # Now call it either this way
    print(Price.final_price(p1, 20, 10))
    # Or cleaner way
    print(p1.final_price(20, 10))

if __name__ == "__main__":
    main()