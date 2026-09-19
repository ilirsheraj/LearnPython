# Give a 20% discount on all products expiring today

from datetime import date, timedelta

today = date.today()
# Add one extra day
tomorrow = today + timedelta(days=1)

products = [
        {"sku": "1", "expiration_date": today, "price": 100.0},
        {"sku": "2", "expiration_date": tomorrow, "price": 50.0},
        {"sku": "3", "expiration_date": today, "price": 20.0},
        ]

for product in products:
    if product["expiration_date"] != today:
        # This is not interesting, so skip it
        continue
    # else is not necessary, juts keeping up with the basic syntax
    else:
        product["price"] *= 0.8
    
    print("Price for sku", product["sku"], "is now", product["price"])
