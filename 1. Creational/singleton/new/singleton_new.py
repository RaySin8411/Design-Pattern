class SingleTonNew:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, a, b):
        self.a = a
        self.b = b


if __name__ == '__main__':
    s1 = SingleTonNew(a=11, b=21)
    print(id(s1))
