def my_sum(*args, **kwargs):
        result = 0
        result2 = ""
        for x in args:
                result += x
        for y in kwargs.values():
                result2 += y
        return {result, result2}

print(my_sum(1, 2, 3,5,6,7,8, a="real", b="Extra kwarg", c="NO!"))