class Calculator:
    def add(self,a,b):
        return a+b

    def div(self,a,b):
        if b == 0:
            return "error"
        return a/b