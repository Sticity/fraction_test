class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def gcd(a, b):
        if (a == 0 or b == 0):
            return 0
        return b % a

    def get_numerator(self):
        return '' + self.numerator

    def get_denominator(self):
        return '' + self.denominator

    def get_fraction(self):
        
