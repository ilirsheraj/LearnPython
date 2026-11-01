# Examples of cases where we get errors
gen = (n for n in range(2))

print(next(gen))
print(next(gen))
# Now we get StopIteration error because the generator got exhausted
print(next(gen))

my_list = [1, 2, 3]
# There is no 5th element in list, so we get IndexError
print(my_list[5])

my_dict = {"a": "A", "b": "B"}
# We get KeyError because key c does not exist
print(my_dict["c"])

# Here we get ZeroDivisionError because we cant divide by 0
print(1 / 0)
