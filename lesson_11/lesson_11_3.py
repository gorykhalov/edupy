# def add_str(*args): # звездочка означает что передается кортеж
#     print(type(args))
#     return "".join(args)
#
# print(add_str("1абра", "2кадабра", "3-змея"))

def add_str(*args, **kwargs): # звездочка означает что передается кортеж
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)
    sep = " "
    if kwargs.get("sep"):
        sep = kwargs["sep"]
    res = sep.join(args)
    if kwargs.get("upper"):
        res = res.upper()
    return res

res = add_str("1абра", "2кадабра", "3-змея", sep="-", upper=True)
print(res)