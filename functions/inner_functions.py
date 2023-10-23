def power(exponent):
    def inner(base):
        return base**exponent
        """
        Inner in this case is a closure, it remembers the value of exponent,
        even after the outer function has finished executing.
        """

    return inner


square = power(2)
cube = power(3)

print(square(5))  # 25
print(cube(5))  # 125
print(power(4)(2))  # 16
