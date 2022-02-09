x1, x2, x3, x4, x5 = [int(k) for k in input().split()]


def flow() -> None:
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
    if x1 - x5 > x2:
        if x2 > x3 + x1:
            if x3 + x5 > x4:
                print('C5')
            else:
                if x3 < x5:
                    print('C6')
                else:
                    print('C7')
                print('C8')
        else:
            return
    else:
        if x2 - x1 > x3:
            return
        else:
            if x4 < x5 + x1:
                if x3 + x2 > x5:
                    print('C3')
                else:
                    print('C2')
                print('C4')
            else:
                print('C1')


flow()
