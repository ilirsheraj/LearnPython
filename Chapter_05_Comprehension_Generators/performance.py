from time import time
# Compare execution speed for for-loop, list comprehension and generator
mx = 5000

# Start the time for for-loop
t = time()
for_loop = []

for a in range(1, mx):
    for b in range(a, mx):
        for_loop.append(divmod(a, b))

print("for-loop: {:.4f} s".format(time() - t))
# print(len(for_loop))
print()

# time for comprehension
t = time()
compr = [divmod(a,b) for a in range(1, mx) for b in range(a,mx)]
print("Comprehension: {:.4f} s".format(time() - t))
print()

# Time for generator
t = time()
gener = list(divmod(a, b) for a in range(1, mx) for b in range(a, mx))
print("Generator: {:.4f} s".format(time() - t))