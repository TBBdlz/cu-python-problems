def main() -> None:
    n, k = [int(i) for i in input().split()]
    if n % 2 == 1:
        sum_a, sum_b, sum_c, m = 0, 0, 0, 0
        while m < k:
            a, b, c = [int(j) for j in input().split()]
            if a == b:
                if b == c:
                    if a + b > k:
                        sum_a -= 3
                        sum_b -= 2
                        sum_c += 1
                    else:
                        sum_a += 1
                        sum_b += 2
                        sum_c -= 3
                else:
                    sum_a += 2
                    sum_b -= 3
            m += 1
        print(sum_a, sum_b, sum_c)
    else:
        s, t = [int(k) for k in input().split()]
        x, y = s, t
        if s > t:
            x -= t
        elif s < t:
            y = 2 * (t - s)
        if x + y > k:
            x, y = y, x
            x = y + s ** 2
        print(x, y)


if __name__ == '__main__':
    main()
