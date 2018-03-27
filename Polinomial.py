import operator

class Polynomial(object):
    def __init__(self, coeffs):
        if not isinstance(coeffs, list):
            raise TypeError("Coefficients should be constant or list")
        for coe in coeffs:
            if not isinstance(coe, (int, float)):
                raise TypeError("Coefficient list should contain only int or float value")
        if len(coeffs) == 0:
            raise TypeError("Coefficient list should not be empty")
        major_degree = next((i for i, coe in enumerate(coeffs) if coe != 0), -1)
        self.coeffs = coeffs[major_degree:]
        self.degree = len(self.coeffs) - 1

    def __eq__(self, q):
        if not isinstance(q, (Polynomial, int, float)):
            raise TypeError("Invalid data type")
        if isinstance(q, (int, float)):
            return len(self.coeffs) == 1 and self.coeffs[0] == q
        elif isinstance(q, Polynomial):
            return self.coeffs == q.coeffs

    def __ne__(self, q):
        if not isinstance(q, (Polynomial, int, float)):
            raise TypeError("Invalid data type")
        if isinstance(q, (int, float)):
            if len(self.coeffs) != 1:
                return True
            else:
                return self.coeffs[0] != q
        elif isinstance(q, Polynomial):
            return self.coeffs != q.coeffs

    def __radd__(self, q):
        return self + q

    def __rmul__(self, q):
        return self * q

    def __add__(self, q):
        if not isinstance(q, (Polynomial, int, float)):
            raise TypeError("Invalid data type")
        if isinstance(q, (int, float)):
            result = Polynomial(self.coeffs)
            result.coeffs[-1] += q
            return result
        elif isinstance(q, Polynomial):
            if (self.degree == q.degree):
                return Polynomial(list(map(operator.add, self.coeffs, q.coeffs)))
            elif self.degree > q.degree:
                return Polynomial(list(map(operator.add, self.coeffs, [0] * (self.degree - q.degree) + q.coeffs)))
            elif self.degree < q.degree:
                return Polynomial(list(map(operator.add, [0] * (q.degree - self.degree) + self.coeffs, q.coeffs)))

    def __neg__(self):
        return Polynomial([-coe for coe in self.coeffs])

    def __sub__(self, q):
        if not isinstance(q, (Polynomial, int, float)):
            raise TypeError("Invalid data type")
        if isinstance(q, (int, float)):
            return self.__add__(-q)
        elif isinstance(q, Polynomial):
            return self.__add__(q.__neg__())

    def __mul__(self, q):
        if not isinstance(q, (Polynomial, int, float)):
            raise TypeError("Invalid data type")
        if isinstance(q, (int, float)):
            result = Polynomial([coe * q for coe in self.coeffs])
            return result
        elif isinstance(q, Polynomial):
            result = [0] * (self.degree + q.degree + 1)
            for i, selfCoe in enumerate(self.coeffs):
                for j, qCoe in enumerate(q.coeffs):
                    result[i + j] += selfCoe * qCoe
            return Polynomial(result)

# [3,6,-2,8] = 3x^3+6x^2-2x+8
# coeStr+ 'x' + degStr

    def __str__(self):
        resStr = ""
        if (self.degree == 0):
            resStr += str(self.coeffs[0])
            return resStr
        elif (self.degree == 1):
            if (self.coeffs[0] == 0):
                resStr += str(self.coeffs[1])
                return resStr
        for i, coe in enumerate(self.coeffs):
            if coe != 0:
                if (i == 0):
                    if (coe == 1):
                        coeStr = ''
                    elif (coe == -1):
                        coeStr = '-'
                    else:
                        coeStr = str(coe)
                    if (self.degree == 1):
                        degStr = ''
                    else:
                        degStr = str(self.degree)
                    resStr += coeStr + 'x' + degStr

                elif (i == self.degree):
                    if (coe > 0):
                        resStr += '+' + str(coe)
                    elif (coe < 0):
                        resStr += str(coe)
                    return resStr

                else:
                    if (coe == 1):
                        coeStr = ''
                    elif (coe == -1):
                        coeStr = '-'
                    else:
                        coeStr = str(coe)
                    if (i == self.degree - 1):
                        degStr = ''
                    else:
                        degStr = str((self.degree - i))
                    if (coe > 0):
                        resStr += '+' + coeStr + 'x' + degStr
                    else:
                        resStr += coeStr + 'x' + degStr
        return resStr if resStr else "0"




