def main():
    N = int(input())
    M = N * 2
    print(M)

    x = []
    for i in "4321":
        i_num = int(i)
        x.append(i * (N // i_num))
        N -= i_num * (N // i_num)

    x.reverse()
    x = "".join(x)
    print(x)

    return


if __name__ == "__main__":
    main()
