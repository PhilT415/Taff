


def concatenate(**words):
    result = 0
    for arg in words.values():
        result += arg
    return result

print(concatenate(a=1, b=2, c=5, d=5, e=125))


