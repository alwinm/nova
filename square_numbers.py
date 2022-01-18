def list_comprehension(n):
    return [i*i for i in range(n)]

def map_lambda(n):
    return list(map(lambda x:x*x,range(n)))

def appending(n):
    _list = []

    for i in range(n):
        _list.append(i*i)

    return _list

def access(n):

    _list = [0]*n # if you can add lists together, you can surely multiply them too ;)

    for i in range(n):
        _list[i] = i*i

    return _list

