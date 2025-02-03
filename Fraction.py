class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

        if denominator == 0:
            raise ZeroDivisionError
        
        if not isinstance(numerator, float):
            if isinstance(numerator, str):
                spl = numerator.split("/")
                if len(spl) == 2:
                    numerator = spl[0]
                    denominator = spl[1]

            if self.is_int(numerator) and self.is_int(denominator):
                self.numerator = int(numerator)
                self.denominator = int(denominator)
            else:
                self.numerator = 0
                self.denominator = 0
        else:
            self.numerator = 0
            self.denominator = 0
            
    @staticmethod
    def is_int(string):
        try:
            int(string)
            return True
        except ValueError:
            return False
    
    def gcd(a, b):
        if (b == 0 or a == 0): 
            return 0 
        while b: 
            a, b = b, a % b
        return a

    def get_numerator(self):
        divisor = Fraction.gcd(self.numerator, self.denominator)        
        return str(self.numerator // divisor) if divisor != 0 else str(self.numerator)

    def get_denominator(self):
        divisor = Fraction.gcd(self.numerator, self.denominator)
        return str(self.denominator // divisor) if divisor != 0 else str(self.denominator)

    def get_fraction(self):
        numerator = self.get_numerator()
        denominator = self.get_denominator()
        
        if numerator == "0":
            return "0"
        if denominator == "1":
            return numerator
        return f"{numerator}/{denominator}"
