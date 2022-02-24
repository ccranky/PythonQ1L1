class Matrix():
    def __init__(self, in_lst):
        self.data = in_lst

    def __str__(self):
        out_str = ["".join(str(i)) + '\n' if cnt==len(k)-1 else "".join(str(i)) for k in self.data for cnt, i in enumerate(k)]
        return ' ' + ' '.join(out_str)

    def __add__(self, other):
        out_val = [[c+d for c, d in zip(a, b)]   for a, b in zip(self.data, other.data) ]
        return Matrix(out_val)

M = Matrix([[1, 2, 5], [2, 3, 1], [3, 5, 9]])
M2 = Matrix([[2, 3, 6], [3, 4, 2], [4, 6, 10]])
print(M+M2)