# given a string, swap the cases of the letters
def swap_case(s):
    arr = []
    for c in s:
        if c.islower():
            arr.append(c.upper())
        elif c.isupper():
            arr.append(c.lower())
        else:
            arr.append(c)
    result_str = "".join(arr)
    return result_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)