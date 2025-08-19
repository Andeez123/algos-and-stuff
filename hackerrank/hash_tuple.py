# hashes the tuple of the inputs
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(list(integer_list))
    my_tuple = tuple(integer_list)
    print(hash(my_tuple))