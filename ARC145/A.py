import sys


def main():
    _ = int(input())
    S = sys.stdin.readline().strip()

    if S == "AB" or S == "BA":
        print("No")
        return

    if S[0] == "A" and S[-1] == "B":
        print("No")
        return

    print("Yes")
    return


if __name__ == "__main__":
    main()
