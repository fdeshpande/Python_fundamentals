def miniMaxSum(arr):
    print(arr)
    arr_ = sorted(arr)
    print(arr_)
    min = arr_[:-1:]
    max = arr_[1::]
    print(min)
    print(max)
    print(sum(min))
    print(sum(max))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)