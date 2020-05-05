# Implementation of the Polynomial ADT using a sorted linked list.


class Polynomial:
    # Create a new polynomial object.
    def __init__(self, degree=None, coefficient=None):
        if degree is None:
            self._polyHead = None
        else:
            self._polyHead = _PolyTermNode(degree, coefficient)
        self._polyTail = self._polyHead

    # Return the degree of the polynomial.
    def degree(self):
        if self._polyHead is None:
            return -1
        else:
            return self._polyHead.degree

    # Return the coefficient for the term of the given degree.
    def __getitem__(self, degree):
        assert self.degree() >= 0, "Operation not permitted on" \
                                   " an empty polynomial."
        curNode = self._polyHead
        while curNode is not None and curNode.degree > degree:
            curNode = curNode.next

        if curNode is None or curNode.degree != degree:
            return 0.0
        else:
            return curNode.coefficient

    # Evaluate the polynomial at the given scalar value.
    def evaluate(self, scalar):
        assert self.degree() >= 0, "Only non -empty polynomials " \
                                   "can be evaluated."
        result = 0.0
        curNode = self._polyHead
        while curNode is not None:
            result += curNode.coefficient * (scalar ** curNode.degree)
            curNode = curNode.next
        return result

    def _appendTerm(self, degree, value):
        """
        Function appends an polynomial element with
        degree and coefficient
        to a proper place in linked list.
        IF SUCH A DEGREE IS ALREADY IN LIST, RAISE EXCEPTION
        :param degree: float
        :param value: float
        :return: None
        """
        append_obj = _PolyTermNode(degree, value)
        curr_node = self._polyHead

        # If it's the first element in the list:
        if curr_node is None or degree > self.degree():
            append_obj.next = self._polyHead
            self._polyHead = append_obj
            self._polyTail = append_obj
            return

        while degree < curr_node.degree:
            # If the list has ended:
            if curr_node.next is None:
                curr_node.next = append_obj
                self._polyTail = append_obj
                return None
            elif degree == curr_node.next.degree:
                raise ValueError('Degree is already in the list')
            elif degree > curr_node.next.degree:
                append_obj.next = curr_node.next
                curr_node.next = append_obj
                self._polyTail = append_obj
                return None
            else:
                curr_node = curr_node.next
        # If the degree is the same as the first one
        raise ValueError('Degree is already in the list')

    # Polynomial multiplication: newPoly = self * rhsPoly.
    # Polynomial addition: newPoly = self + rhsPoly.

    def __add__(self, rhsPoly):
        """
        Adds coefficients of similar degrees together and returns
        this added polynomial
        :param rhsPoly: Polynomial
        :return: Polynomial
        """

        new_p = Polynomial()
        new_degree = max((self.degree(), rhsPoly.degree()))
        if new_degree < 0:
            return new_p
        else:
            for d in range(int(new_degree), -1, -1):
                coefficient = self[d] + rhsPoly[d]
                if coefficient > 0:
                    if new_p._polyHead is None:
                        new_p._polyHead = _PolyTermNode(float(d), coefficient)
                    else:
                        new_p._appendTerm(float(d), float(coefficient))
        return new_p

    def __mul__(self, rhsPoly):
        """
        Multiplies all the coefficients of two polynoms, returns
        added  ,.. polynomial
        :param rhsPoly: Polynomial
        :return: Polynomial
        """
        res = Polynomial()
        curr_node = self._polyHead
        while curr_node is not None:
            curr_other = rhsPoly._polyHead
            while curr_other is not None:
                coefficient = curr_node.coefficient * curr_other.coefficient
                degree = curr_node.degree + curr_other.degree
                if coefficient != 0:
                    if res._polyHead is None:
                        res = Polynomial(degree, coefficient)
                    else:
                        res = res + Polynomial(degree, coefficient)
                    curr_other = curr_other.next
            curr_node = curr_node.next
        return res

    def __sub__(self, rhsPoly):
        """
        Subtracts coefficients of similar degrees together
         and returns
        this added polynomial
        :param rhsPoly: Polynomial
        :return: Polynomial
        """
        new_p = Polynomial()
        new_degree = max((self.degree(), rhsPoly.degree()))
        if new_degree < 0:
            return new_p
        else:
            for d in range(int(new_degree), -1, -1):
                coefficient = self[d] - rhsPoly[d]
                if coefficient != 0:
                    new_p._appendTerm(float(d), float(coefficient))
        return new_p

    def __str__(self):
        curr_node = self._polyHead
        res = ''
        while curr_node:
            res += f'{str(curr_node)} + '
            curr_node = curr_node.next
        return res[:-3]


# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return str(self.coefficient) + "x^" + str(self.degree)


if __name__ == '__main__':
    poly = Polynomial()
    # poly._appendTerm(3, 55)
    poly._appendTerm(1, 3)
    poly._appendTerm(4, 7)
    poly._appendTerm(0, 1)
    print(poly)
