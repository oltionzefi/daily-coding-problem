# This problem will be solved with functional programming
# in which you have a function (interface) that accepts another function (implementation) and calls it as local
# We have cons - high order function that accepts two integers and returns another function,
# which accepts the third function that knows how to operate with this integers.
# After we implement function like left inside the car and right in cdr, and they return
# left of pair and right of pair correspondingly


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(f):
    def left(a, b):
        return a
    return f(left)


def cdr(f):
    def right(a, b):
        return b
    return f(right)
