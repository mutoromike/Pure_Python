def power(exponent):
    def inner(base):
        return base**exponent
        """
        Inner in this case is a CLOSURE (encloses the needed non-local variable
        together with the function object), it remembers the value of exponent,
        even after the outer function has finished executing.

        Exponent is a non-local variable for inner. It is also called
        a cell variable (a reference to the exponent variable from the
        outer scope).
        """

    return inner


square = power(2)
cube = power(3)

print(square(5))  # 25
print(cube(5))  # 125
print(power(4)(2))  # 16
