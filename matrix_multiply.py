def matrix_multiply(A, B):

    # m: تعداد سطرهای ماتریس A
    # n: تعداد ستون‌های ماتریس A (باید با تعداد سطرهای B برابر باشد)
    # p: تعداد ستون‌های ماتریس B

    m = len(A)
    n = len(A[0])

    if n != len(B):
        print("Matrix multiplication is not possible!")
        return

    p = len(B[0])

    # ساخت ماتریس نتیجه با مقدار اولیه صفر
    C = [[0 for j in range(p)] for i in range(m)]

    # ضرب ماتریس‌ها
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

    return C


# Matrix A (2×3)
mat_A = [
    [1, 2, 3],
    [4, 5, 6]
]

# Matrix B (3×2)
mat_B = [
    [7, 8],
    [9, 1],
    [2, 3]
]

result = matrix_multiply(mat_A, mat_B)

if result != None:
    print("Result Matrix:")
    for row in result:
        print(row)