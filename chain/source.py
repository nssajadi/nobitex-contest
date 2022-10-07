class Chain:
    def __init__(self, val):
        self.val = val

    def __call__(self, new_val):
        if (isinstance(new_val, int) or isinstance(new_val, float)) and (isinstance(self.val, int) or isinstance(self.val, float)):
            return Chain(self.val + new_val)
        elif isinstance(new_val, str) and isinstance(new_val, str):
            return Chain(self.val + ' ' + new_val)
        else:
            raise Exception("invalid operation")

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        return self.val == other


# print(Chain(1))
# print(Chain(1.6)(3)(5))
# print(Chain('Ali')('Gholi')('Kio'))
# print(Chain('abc')('defg') == 'abc defg')
# print(Chain(64) == 64)
# print(Chain(9)([1, 2]))
# print(Chain('Ali')('Gholi')(1))
