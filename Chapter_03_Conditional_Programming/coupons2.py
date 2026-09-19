# Create a dictionary of customers: use switch
customers = [
        dict(id=1, total=200, coupon_code="F20"),
        dict(id=2, total=150, coupon_code="P30"),
        dict(id=3, total=100, coupon_code="P50"),
        dict(id=4, total=110, coupon_code="F15"),
        ]

# Create a dictionary of discounts
discounts = {
        # Each value is percent discount(P), or fixed discount (F)
        "F20": (0.0, 20.0),
        "P30": (0.3, 0.0),
        "P50": (0.5, 0.0),
        "F15": (0.0, 15.0),
        }

for customer in customers:
    code = customer["coupon_code"]
    # print(code)
    percent, fixed = discounts.get(code, (0.0, 0.0))
    # print(f"Percent is {percent}, fixed is {fixed}")
    customer["discount"] = percent * customer["total"] + fixed
    # print(customer["discount"])
    customer["pay"] = customer["total"] - customer["discount"]

# print(customers)

for customer in customers:
    print(customer["id"], customer["total"], customer["discount"], customer["pay"])
