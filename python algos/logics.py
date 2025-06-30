# sum first n numbers
def sumNatural(n: int) -> int:
    return (n* (n+1)) // 2

# naive square approach: O(n) time
def sumSquares(n: int) -> int:
    return sum([i**2 for i in range(n+1)])

# efficient mathematical approact (using formula)
def sumSquaresEff(n: int) -> int:
    return (n*(n+1)*((2*n)+1)) // 6

if __name__ == "__main__":
    n = 3
    #print(sumNatural(5))
    #print(sumSquares(n))
    print(sumSquaresEff(n))