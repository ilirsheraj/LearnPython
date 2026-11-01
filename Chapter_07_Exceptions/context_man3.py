from decimal import Decimal, localcontext, Context

one = Decimal("1")
three = Decimal("3")

# with staement will clean everything automatically
with localcontext(Context(prec = 5)) as ctx:
    print(ctx)
    print(one / three)

print()
print("The precision has been set automatically")
print(one / three)
print()

# Combine everything in one
with localcontext(Context(prec=5)), open("out.txt", "w") as out_f:
    out_f.write(f"{one} / {three} = {one / three}\n")

print("The precision has been set automatically")
print(one / three)