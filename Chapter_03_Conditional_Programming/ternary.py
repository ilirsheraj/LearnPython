# classical if-else
order_total = 246

if order_total > 100:
    discount = 25
else:
    discount = 0

print(order_total, discount)

# shorter
discount = 25 if order_total > 100 else 0
print(order_total, discount)