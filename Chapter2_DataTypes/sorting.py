from operator import itemgetter
a = [(5,3), (1,3), (1,2), (2,-1), (4,9)]
print(f"The list is: {a}")
print(f"Conventional Sorting: {sorted(a)}")
# Sort according to the first item
print(f"Sort by first item: {sorted(a, key=itemgetter(0))}")
# Sort according to the second item
print(f"Sort by second item: {sorted(a, key=itemgetter(1))}")
# Sort according to 1 first, then 2
print(f"Sort by first, then second: {sorted(a, key=itemgetter(0,1))}")
# Now reverse it
print(f"Reverse sorting by second item:"
      f"{sorted(a, key=itemgetter(1), reverse=True)}")