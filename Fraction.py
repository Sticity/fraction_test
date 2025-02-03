class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if self.is_int(numerator) and self.is_int(denominator):
            self.numerator = int(numerator)
            self.denominator = int(denominator)

        if denominator == 0:
            raise ZeroDivisionError

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
        lowest = self.numerator / self.gcd(self.numerator, self.denominator)
        
        return '' + lowest

    def get_denominator(self):
        lowest = self.denominator / self.gcd(self.numerator, self.denominator)
        
        return '' + lowest

    def get_fraction(self):
        if self.numerator == 0:
            return '0'
        
        return 'f{self.numerator}/{self.denominator}'
