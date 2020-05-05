from double_linked import DoubleLinked


class BigInteger:
    def __init__(self, init_value='0'):
        self.num = DoubleLinked()
        self.negative = False

        not_started = True
        for i in range(len(init_value)):
            if i == 0 and init_value[i] == '-':
                self.negative = True
                continue
            # Getting all zeros at first: незначущі цифри
            if init_value[i] == '0' and not_started:
                continue
            not_started = False
            self.num.append(int(init_value[i]))

    # COMPARABLE
    def __lt__(self, other):
        ans = self.num.compare(other.num, self.negative, other.negative)
        return True if ans == -1 else False

    def __le__(self, other):
        ans = self.num.compare(other.num, self.negative, other.negative)
        return False if ans == 1 else True

    def __gt__(self, other):
        ans = self.num.compare(other.num, self.negative, other.negative)
        return True if ans == 1 else False

    def __ge__(self, other):
        ans = self.num.compare(other.num, self.negative, other.negative)
        return False if ans == -1 else True

    def __eq__(self, other):
        ans = self.num.compare(other.num, self.negative, other.negative)
        return True if ans == 0 else False

    def __ne__(self, other):
        ans = self.num.compare(other.num, self.negative, other.negative)
        return False if ans == 0 else True

    def __add__(self, other):
        """
        Adds two big integers together and returns one
        """
        # if of the same negativity:
        if self.negative == other.negative:
            res_double_linked = self.num.simple_add(other.num)
            res = BigInteger()
            res.num = res_double_linked
            res.negative = self.negative
            return res
        comparison = self.num.simple_compare(other.num)
        if comparison == 1:
            res_double = self.num.simple_sub(other.num)
            res = BigInteger(str(res_double))
            res.negative = True if self.negative else False
        elif comparison == -1:
            res_double = other.num.simple_sub(self.num)
            res = BigInteger(str(res_double))
            res.negative = True if other.negative else False
        else:
            res = BigInteger()
        return res

    def __sub__(self, other):
        """
        Subttract the two big integers together and returns one
        """
        other.negative = False if other.negative else True
        res = self + other
        other.negative = False if other.negative else True
        return res

    def __mul__(self, other):
        """
        Multiplies two numbers together:
        """
        double_res = self.num.sumple_multiplication(other.num)
        res = BigInteger(str(double_res))
        if self.negative == other.negative:
            res.negative = False
        else:
            res.negative = True
        return res

    def __pow__(self, power):
        """
        Raises it to the power of 'power'
        I KNOW I DID'T MAKE IT FOR NEGATIVES
        """
        res = BigInteger()
        res = res + self
        for i in range(power-1):
            res = res.__mul__(res)
        return res

    def __floordiv__(self, other):
        """
        That's usual // in python
        """
        res = 0
        other.negative = False
        self.negative = False
        x = self
        while x >= other:
            x = x.__sub__(other)
            res += 1
        return BigInteger(str(res))

    def __mod__(self, other):
        """
        And this is usual %(mod in python)
        """
        other.negative = False
        self.negative = False
        x = self
        while x >= other:
            x = x.__sub__(other)
        return x

    @staticmethod
    def _int_to_bin(integer):
        """
        Convert int to bin, obviously
        """
        res = DoubleLinked()
        res1 = ''
        while integer >= BigInteger('1'):
            if integer % BigInteger('2') == BigInteger():
                integer = integer // BigInteger('2')
                num_remainder = 1
                res.append('0')
                res1 += '0'
            elif integer % BigInteger('2') == BigInteger('1'):
                integer = integer // BigInteger('2')
                num_remainder = 1
                res1 += '1'
        return BigInteger(res1[::-1])

    def __and__(self, other):
        """
        Usual and(&)
        """
        x = self._int_to_bin(self)
        other = other._int_to_bin(other)
        new = DoubleLinked()

        if x.num.size > other.num.size:
            bigger_tail = x.num._head
            smaller_tail = other.num._head
        else:
            bigger_tail = other.num._head
            smaller_tail = x.num._head
        while smaller_tail:
            num = bigger_tail.value * smaller_tail.value
            new.append(num)
            bigger_tail = bigger_tail.next
            smaller_tail = smaller_tail.next
        while bigger_tail:
            new.append(bigger_tail.value)
            bigger_tail = bigger_tail.next
        return new

    def __xor__(self, other):
        """
        Usual xor(^)
        """
        x = self._int_to_bin(self)
        other = other._int_to_bin(other)
        new = DoubleLinked()

        if x.num.size > other.num.size:
            bigger_tail = x.num._head
            smaller_tail = other.num._head
        else:
            bigger_tail = other.num._head
            smaller_tail = x.num._head
        while smaller_tail:
            if bigger_tail.value * smaller_tail.value == 1:
                num = 0
            elif bigger_tail.value == 0 and smaller_tail.value == 0:
                num = 0
            else:
                num = 1
            new.append(num)
            bigger_tail = bigger_tail.next
            smaller_tail = smaller_tail.next
        while bigger_tail:
            new.append(bigger_tail.value)
            bigger_tail = bigger_tail.next
        return new

    def __or__(self, other):
        """
        Usual or(|)
        """
        x = self._int_to_bin(self)
        other = other._int_to_bin(other)
        new = DoubleLinked()

        if x.num.size > other.num.size:
            bigger_tail = x.num._head
            smaller_tail = other.num._head
        else:
            bigger_tail = other.num._head
            smaller_tail = x.num._head
        while smaller_tail:
            if bigger_tail.value == 0 and smaller_tail.value == 0:
                num = 0
            else:
                num = 1
            new.append(num)
            bigger_tail = bigger_tail.next
            smaller_tail = smaller_tail.next
        while bigger_tail:
            new.append(bigger_tail.value)
            bigger_tail = bigger_tail.next
        return new

    def __rshift__(self, bit_num):
        return self._int_to_bin(self // (BigInteger('2') ** int(str(bit_num))))

    def __lshift__(self, bit_num):
        return self._int_to_bin(self * (BigInteger('2') ** int(str(bit_num))))

    def toString(self):
        return str(self)

    def __len__(self):
        return self.num.size

    def __str__(self):
        return '-' + str(self.num) if self.negative else str(self.num)
