def unlim_args(*args, **kwargs):
    print(kwargs)
    for k, argument in kwargs.items():
        print(k, argument)


unlim_args(1, 2, 3, 4, name='Max', age=29)
