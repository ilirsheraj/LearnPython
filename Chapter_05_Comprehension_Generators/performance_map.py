from time import time

mx = 2*10**7
# again for-loop vs comprehension vs map
t = time()
absloop = []
for n in range(mx):
    absloop.append(abs(n))
print("for loop: {:.4f} s".format(time() - t))
print()

t = time()
abslist = [abs(n) for n in range(mx)]
print("list comprehension: {:.4f} s".format(time() - t))
print()

t = time()
absmap = list(map(abs, range(mx)))
print("map: {:.4f} s".format(time() - t))