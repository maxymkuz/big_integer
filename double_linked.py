class DoubleLinked:
    def __init__(self):
        self._head = None
        self.size = 0
        self.tail = None

    def add_start(self, value):
        """
        Adds a number at the 0 position
        """
        if self._head:
            new = DoubleNode(value, previous=None, next=self._head)
            self._head.previous = new
            self._head = new
        else:
            self._head = DoubleNode(value)
            self.tail = self._head

        self.size += 1

    def append(self, value):
        """
        Appends a value to the end, unless the value is 0
        """
        # If adding zero to blank
        if self.tail:
            new = DoubleNode(value, previous=self.tail, next=None)
            self.tail.next = new
            self.tail = new
            # print('      ', self.tail)
        else:
            x = DoubleNode(value)
            self._head = x
            self.tail = x
        self.size += 1

    def compare(self, other, first_negative, second_negative):
        """
        Compares the two input number and return 1 if
        the first is larger, -1 if the second is larger
        and 0 if equal.
        """
        # if one of them is negative and other is not
        if first_negative and not second_negative:
            return -1
        if second_negative and not first_negative:
            return 1

        # if they are of the same negativity:
        res = 0
        if self.size > other.size:
            res = 1
        elif self.size < other.size:
            res = -1
        else:
            curr_first = self._head
            curr_second = other._head
            for i in range(0, self.size):
                if curr_first.value > curr_second.value:
                    res = 1
                elif curr_first.value < curr_second.value:
                    res = -1
                curr_first = curr_first.next
                curr_second = curr_second.next

        if res == 0:
            return 0
        # they both positive:
        if not first_negative:
            return res
        else:  # if negative
            return 1 if res == -1 else -1

    def simple_add(self, other):
        """
        Simply adds two number together and returns another one
        """
        if self.size > other.size:
            bigger_tail = self.tail
            smaller_tail = other.tail
        else:
            bigger_tail = other.tail
            smaller_tail = self.tail
        add_res = DoubleLinked()
        next_plus_one = False

        while smaller_tail is not None:
            # print('tails', smaller_tail, bigger_tail)
            number = 1 if next_plus_one else 0
            number += smaller_tail.value + bigger_tail.value
            if number > 9:
                next_plus_one = True
                number = number % 10
            else:
                next_plus_one = False
            add_res.add_start(number)
            smaller_tail = smaller_tail.previous
            bigger_tail = bigger_tail.previous

        # We may need to add one more
        if self.size == other.size and next_plus_one:
            add_res.add_start('1')
        else:  # We just copy all the rest
            while bigger_tail:
                number = 1 if next_plus_one else 0
                number += bigger_tail.value
                if number > 9:
                    next_plus_one = True
                    number = number % 10
                else:
                    next_plus_one = False

                add_res.add_start(number)
                bigger_tail = bigger_tail.previous
        return add_res

    def simple_sub(self, other):
        """
        Simply subtracts two numbers(from bigger subtract
        smaller) together and returns another DoubleLinked
        """
        if self.size > other.size:
            bigger_tail = self.tail
            smaller_tail = other.tail
        else:
            bigger_tail = self.tail
            smaller_tail = other.tail
        add_res = DoubleLinked()
        next_minus_one = False

        while smaller_tail is not None:
            number = -1 if next_minus_one else 0
            number += bigger_tail.value - smaller_tail.value
            if number < 0:
                next_minus_one = True
                number = number + 10
            else:
                next_minus_one = False
            add_res.add_start(number)
            smaller_tail = smaller_tail.previous
            bigger_tail = bigger_tail.previous
        # the rest of the biggest number:
        while bigger_tail:
            number = -1 if next_minus_one else 0
            number += bigger_tail.value
            if number < 0:
                next_minus_one = True
                number = number + 10
            else:
                next_minus_one = False

            add_res.add_start(number)
            bigger_tail = bigger_tail.previous
        return add_res

    def simple_compare(self, other):
        """
        Compares the two input number and return 1 if
        the first is larger, -1 if the second is larger
        and 0 if equal. DOES NOT COUNT NEGATIVITY!
        """

        res = 0
        if self.size > other.size:
            res = 1
        elif self.size < other.size:
            res = -1
        else:
            curr_first = self._head
            curr_second = other._head
            for i in range(0, self.size):
                if curr_first.value > curr_second.value:
                    res = 1
                elif curr_first.value < curr_second.value:
                    res = -1
                curr_first = curr_first.next
                curr_second = curr_second.next
        if res == 0:
            return 0
        return res

    def sumple_multiplication(self, other):
        """
        Simply multiplies two numbers
        """
        second_tail = other.tail
        res = DoubleLinked()
        digit = 0

        while second_tail:
            first_tail = self.tail
            multiplier = second_tail.value
            temp_number = DoubleLinked()
            next_tenths = 0
            while first_tail:
                number = first_tail.value * multiplier + next_tenths
                if number > 9:
                    next_tenths = number // 10
                    number = number % 10
                else:
                    next_tenths = 0
                temp_number.add_start(number)
                first_tail = first_tail.previous

            if next_tenths > 0:
                temp_number.add_start(next_tenths)

            for i in range(digit):
                temp_number.append(0)

            res = res.simple_add(temp_number)
            second_tail = second_tail.previous
            digit += 1
        return res

    def __str__(self):
        if self.size == 0:
            return '0'
        curr_node = self._head
        res = ''
        while curr_node:
            res += str(curr_node)
            curr_node = curr_node.next
        return res


class DoubleNode:
    def __init__(self, num, previous=None, next=None):
        self.value = num
        self.next = next
        self.previous = previous

    def __str__(self):
        return str(self.value)
