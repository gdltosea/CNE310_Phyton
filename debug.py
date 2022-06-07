def lone_sum(a, b, c):
    if a == b and a == c and b == c:
        return 0
    elif a == c:
        return b
    elif b == c:
        return a
    if a>=b:
        return c
    else:
        return a+b+c
print("lone_sum of 10, 10, 10 should be 0: " + str(lone_sum(10, 10, 10)))

