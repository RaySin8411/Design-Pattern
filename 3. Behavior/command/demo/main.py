def demo(a, b, c):
    print('a:', a)
    print('b:', b)
    print('c:', c)


class Command:
    def __init__(self, cmd, *args):
        self._cmd = cmd
        self._args = args

    def __call__(self, *args):
        return self._cmd(*self._args + args)


if __name__ == '__main__':
    cmd = Command(dir, __builtins__)
    print(cmd())

    cmd = Command(demo, 1, 2)
    cmd(3)
