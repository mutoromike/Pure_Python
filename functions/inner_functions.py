def power(exponent):
    def inner(base):
        return base**exponent

    return inner


square = power(2)
cube = power(3)

print(square(5))  # 25
print(cube(5))  # 125
print(power(4)(2))  # 16
