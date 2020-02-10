def xxx(num):
    def wrapper(func):
        def inner():
            for i in range(num):
                func()
        return inner
    return wrapper

@xxx(3)
def func():
    print('1')

func()