import sys


def main():
    _ = int(input())
    S = sys.stdin.readline().strip()
    S = list(S)

    S1 = S.copy()
    S2 = list(reversed(S))

    if S1 == S2:
        print("Yes")
        return

    for i, (s1, s2) in enumerate(zip(S1, S2)):
        if s1 == "B":
            if s2 == "B":
                print("Yes")
                return

            if i == (len(S) - 1) // 2:
                print("No")
                return

            print("Yes")
            return

        if s2 == "B":
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
