class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def gcd(a, b):
        if (b == 0):
            return 0
        return (gcd(b, a % b))

    def get_numerator(self):
        return '' + self.numerator

    def get_denominator(self):
        return '' + self.denominator

    def get_fraction(self):
        
