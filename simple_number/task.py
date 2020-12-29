class SimpleNumber:
    @staticmethod
    def is_simple(x):
        for i in range(2, x - 1):
            if x % i == 0:
                return False
        return True
