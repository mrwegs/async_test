
def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, *kwargs)
        next(g)
        return g

    return inner


class MyException(BaseException):
    pass


@coroutine
def subgen():
    while True:
        try:
            message = yield
        except MyException:
            print('Raise MyException')


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         message = yield
    #         g.send(message)
    #     except MyException as e:
    #         g.throw(e)
    yield from g

