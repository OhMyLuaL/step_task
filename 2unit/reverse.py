def rotate():
    string = input()
    if len(string) == 5:
        reverse = string[::-1]
        print(int(reverse))
    else:
        reverse1 = string[0] + string[::-1]
        final_rev = reverse1[0:-1]
        print(int(final_rev))

rotate()