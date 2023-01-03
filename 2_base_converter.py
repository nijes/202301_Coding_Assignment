class Transformer(object):
    """
    Convert numbers from base 10 integers to base N strings and back again.
    Sample usage:
        base20 = Transformer('0123456789abcdefghij')
        base20.from_decimal(1234)
        > '31e'
        base20.to_decimal('31e')
        > 1234
    """
    def __init__(self, digits):
        self.digits = digits
        self.decimal_digits = '0123456789'

    def from_decimal(self, i:int) -> str:
        return self._convert(i, self.decimal_digits, self.digits)

    def to_decimal(self, s:str) -> int:
        return int(self._convert(s, self.digits, self.decimal_digits))

    def _convert(self, number, fromdigits, todigits):
        # from_decimal
        if fromdigits == self.decimal_digits:
            rev_result = ''
            while number > 0 :
                rev_result += todigits[number % len(todigits)]
                number //= len(todigits)
            return rev_result[::-1]
        # to_decimal
        else:
            result = 0
            for i in range(len(number)):
                result += fromdigits.index(number[i])*(len(fromdigits)**(len(number)-i-1))
            return result