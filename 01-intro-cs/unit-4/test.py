def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

print(simple_divide(4,0))