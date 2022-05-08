from functools import wraps
from datetime import datetime
import time

def decoration_params(path='log.txt'):
    def decorations(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            time_result = time.time() - start
            log = f'Function name: {func.__name__}\nResult: {result}\nDate: {datetime.now()} Time: {time_result} Args and Kwargs: {args}, {kwargs}\n{"*"*20}\n'
            with open(path, 'a+', encoding='utf-8') as logs:
                logs.write(log)
            return print('Successfully log!')
        return wrapper
    return decorations

@decoration_params()
def func_summator(a, b):
    '''Супер утилита, которая складывает 2 значения'''
    return a + b

if __name__ == '__main__':
    func_summator(1, 1)

