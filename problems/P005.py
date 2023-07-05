import math


def main() -> None:
    c: str = input()
    if c == 'P':
        p = math.sqrt(7 + math.sqrt(6 + math.sqrt(5)))
        p = round(p, 6)
        print(f'pi = {p}')
    elif c == 'R':
        n: int = int(input())
        p: float = sum(math.pow(-3, -k) / (2 * k + 1) for k in range(n + 1))
        p *= math.sqrt(12)
        p = round(p, 12)
        print(f'pi = {p}')
    elif c == 'S':
        m: int = int(input())
        q, r, t, k, n, x, i = 1, 0, 1, 1, 3, 3, 0
        p: str = ''
        while i < m:
            if 4 * q + r - t < n * t:
                p += str(n)
                i += 1
                a = 10 * (r - n * t)
                n = 10 * (3 * q + r) // t - 10 * n
                q *= 10
            else:
                a = (2 * q + r) * x
                b = (7 * q * k + 2 + x * r) // (x * t)
                q *= k
                t *= x
                x += 2
                k += 1
                n = b
            r = a
        p = f'{p[0]}.{p[1:]}'
        print(f'pi = {p}')
    else:
        print("Invalid")


if __name__ == '__main__':
    main()
