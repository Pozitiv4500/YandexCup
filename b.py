from string import ascii_lowercase

n = int(input())
m = int(input())
X = list(map(int, input().split()))
B = list(map(int, input().split()))

a = []


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        gcd = self.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}" if self.denominator != 1 else str(self.numerator)


def row_echelon_form(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i].numerator) > abs(matrix[max_row][i].numerator):
                max_row = k
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        leading_coefficient = matrix[i][i]
        for j in range(i, m):
            matrix[i][j] = matrix[i][j] / leading_coefficient
        for j in range(i + 1, n):
            ratio = matrix[j][i]
            for k in range(i, m):
                matrix[j][k] -= ratio * matrix[i][k]
    return matrix


def reduced_row_echelon_form(matrix):
    n = len(matrix)
    m = len(matrix[0])
    row_echelon_form(matrix)
    for i in range(n):
        leading_index = next((j for j in range(m - 1) if matrix[i][j].numerator != 0), None)
        if leading_index is not None:
            for j in range(i + 1, n):
                ratio = matrix[j][leading_index]
                for k in range(m):
                    matrix[j][k] -= ratio * matrix[i][k]
            for j in range(i - 1, -1, -1):
                ratio = matrix[j][leading_index]
                for k in range(m):
                    matrix[j][k] -= ratio * matrix[i][k]
    return matrix


'''mat = []
for j in range(m):
    mat_row = []
    for i in range(1, n + 1):
        mat_row.append(Fraction(X[j] ** (i - 1), 1))
    mat_row.append(-Fraction(B[j], 1))
    mat.append(mat_row)
result = reduced_row_echelon_form(mat)
x4 = 0

'''

def mod_inverse(a, mod):
    return pow(a, mod - 2, mod)
def gauss_mod(matrix, mod):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(min(rows, cols - 1)):
        for j in range(i, rows):
            if matrix[j][i] != 0:
                matrix[i], matrix[j] = matrix[j], matrix[i]
                break
        inv = mod_inverse(matrix[i][i], mod)
        for k in range(i, cols):
            matrix[i][k] = (matrix[i][k] * inv) % mod
        for j in range(i + 1, rows):
            factor = matrix[j][i]
            for k in range(i, cols):
                matrix[j][k] = (matrix[j][k] - factor * matrix[i][k]) % mod
    for i in range(min(rows, cols - 1) - 1, -1, -1):
        for j in range(i):
            factor = matrix[j][i]
            for k in range(i, cols):
                matrix[j][k] = (matrix[j][k] - factor * matrix[i][k]) % mod

    return matrix

matrix = []
for j in range(m):
    row = []
    for i in range(1, n + 1):
        row.append(pow(X[j], i - 1, 23))
    row.append(B[j])
    matrix.append(row)
result = gauss_mod(matrix, 23)
password_indices = [int(result[i][-1]) for i in range(len(result))]
while len(password_indices) != n:
    password_indices.append(0)
password = ''.join(ascii_lowercase[i] for i in password_indices)
print(password)