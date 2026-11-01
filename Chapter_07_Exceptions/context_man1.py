from decimal import Context, Decimal, getcontext, setcontext

one = Decimal("1")
print(one)
three = Decimal("3")
print(three)

# Get the original context
orig_ctx = getcontext()
# Set the precision to 5 decimal places
ctx = Context(prec=5)
setcontext(ctx)
print(ctx)
print()
print(one / three)

# reset the context back to the original
setcontext(orig_ctx)
print(one / three)
