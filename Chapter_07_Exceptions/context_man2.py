from decimal import Context, Decimal, getcontext, setcontext

one = Decimal("1")
three = Decimal("3")

orig_ctx = getcontext()
ctx = Context(prec=5)
setcontext(ctx)

try:
    print(ctx)
    print(one / three)
# Resets it irrespective of whether previous code run
finally:
    setcontext(orig_ctx)

print(one / three)