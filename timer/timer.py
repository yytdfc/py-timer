import time


class Timer():
    def __init__(self, name=''):
        self.name = name + ' '

    def __enter__(self):
        self.tic = time.time()

    def __exit__(self, a, b, c):
        print(self.name, f'using {time.time() - self.tic:.6f} seconds.')
