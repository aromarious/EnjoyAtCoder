N = int(input())
amr = N % 500
A = int(input())
if amr <= A:
    print('Yes')
else:
    print('No')
# --------------------------------------------------
# n, a = int(input()), int(input())
# print(['Yes', 'No'][(n%500)>a])