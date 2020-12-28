class SimpleNumber:
    @staticmethod
    def isDiving(n, d):
        return n % d == 0
    @staticmethod
    def isSimple(x):
        for i in range(2,x-1):
            if SimpleNumber.isDiving(x, i):
                return False
        return True