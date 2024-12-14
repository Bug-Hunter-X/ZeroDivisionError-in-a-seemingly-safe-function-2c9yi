def function_with_uncommon_error_fixed(a, b):
    try:
        if a == 0:
            return b
        elif b == 0:
            return a
        else:
            return a / b
    except ZeroDivisionError:
        return float('inf')

result = function_with_uncommon_error_fixed(10, 0)
print(result)

result = function_with_uncommon_error_fixed(0,10)
print(result)

result = function_with_uncommon_error_fixed(10, 2)
print(result)