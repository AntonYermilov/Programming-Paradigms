import random

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return 0

    mid = left + (right - left) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, mid)
    number_of_inversions += get_number_of_inversions(a, b, mid, right)

    a[left:mid] = b[left:mid]
    i, j, k = left, mid, left
    while i < mid and j < right:
        if a[j] < b[i]:
            a[k] = a[j]
            j += 1
            number_of_inversions += mid - i
        else:
            a[k] = b[i]
            i += 1
        k += 1
    while i < mid:
        a[k] = b[i]
        k += 1
        i += 1
    return number_of_inversions

if __name__ == '__main__':
    n = 1000
    a = [random.randint(0, 1000) for _ in range(n)]
    b = [0 for _ in range(n)]
    print(get_number_of_inversions(a, b, 0, n))
