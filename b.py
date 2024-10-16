from string import ascii_letters
n = int(input())
m = int(input())
x = list(map(int, input().split()))
b = list(map(int, input().split()))
mat = []
for j in range(m):
    row = [pow(x[j], i, 23) for i in range(n)]
    row.append(b[j])
    mat.append(row)
r = len(mat)
c = len(mat[0])
for i in range(min(r, c - 1)):
    for j in range(i, r):
        if mat[j][i] != 0:
            mat[i], mat[j] = mat[j], mat[i]
            break
    inv = pow(mat[i][i], 23 - 2, 23)
    for k in range(i, c):
        mat[i][k] = (mat[i][k] * inv) % 23
    for j in range(i + 1, r):
        factor = mat[j][i]
        for k in range(i, c):
            mat[j][k] = (mat[j][k] - factor * mat[i][k]) % 23
for i in range(min(r, c - 1) - 1, -1, -1):
    for j in range(i):
        factor = mat[j][i]
        for k in range(i, c):
            mat[j][k] = (mat[j][k] - factor * mat[i][k]) % 23
ab = [int(mat[i][-1]) for i in range(len(mat))]
while len(ab) < n:
    ab.append(0)
a = ''.join(ascii_letters[i] for i in ab)
print(a)
