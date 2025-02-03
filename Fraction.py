class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        self.numerator = 0 
        self.denominator = 1

        try:
            if isinstance(numerator, str):
                numerator = numerator.strip()
                if '/' in numerator:
                    num, denom = numerator.split('/')
                    numerator = int(num)
                    denominator = int(denom)
                else:
                    raise ValueError
            elif isinstance(numerator, float):
                raise ValueError
            
            if self.is_int(numerator) and self.is_int(denominator):
                self.numerator = int(numerator)
                self.denominator = int(denominator)
            else:
                raise ValueError
        
        except (ValueError, TypeError):
            self.numerator = 0
            self.denominator = 1
        
        if self.denominator == 0: 
            raise ZeroDivisionError
    
        if self.numerator != 0 and self.denominator != 0:
            self.gcd = Fraction.gcd(self.numerator, self.denominator)

        else:
            self.gcd = 1  


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
        
        if self.gcd == 0: 
            return 0 

        numerator = self.numerator // self.gcd
        
        return str(numerator)

    def get_denominator(self):
        if self.gcd == 0: 
            return 0 

        denominator = self.denominator // self.gcd
        
        return str(denominator)

    def get_fraction(self):
        numerator = self.get_numerator()
        denominator = self.get_denominator()
        
        if numerator == "0":
            return "0"
        if denominator == "1":
            return numerator
        
        return f"{numerator}/{denominator}"