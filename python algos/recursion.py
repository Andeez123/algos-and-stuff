def listSum(numList: list) -> int:
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSum(numList[1:])

numbers = [1,3,5,7]
print(listSum(numbers))

def hexconv(n: int, base: int) -> str:
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        leadingDigits = hexconv(n//base, base)
        lastDigit = convertString[n%base]
        return leadingDigits + lastDigit

print(hexconv(11, 16))

# multiplication table
def printTable(n: int, i=1):
    # base case
    if (i == 11):
        return
    # print table for current iteration
    print(n, '*', i, "=", n*i)
    i+=1
    # recursive call to next iteration
    printTable(n, i)

printTable(5)