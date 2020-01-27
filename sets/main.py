'''
Sets
A set is a collection which is unordered and unindexed.
'''


def main():
    '''
    main()
    '''

    # Create empty set
    set_a = set()

    # Only one item can exist in set
    set_a.add(5)
    set_a.add(10)
    set_a.add(10)
    set_a.add(20)
    print(type(set_a))
    print(set_a)

    set_b = {10, 20, 30, 40}
    print(type(set_b))
    print(set_b)

    # Print sorted set
    for item in sorted(set_b):
        print(item)

    # Union
    set_c = set_a | set_b
    print('Union')
    print(set_c)

    # Intersection
    set_c = set_a & set_b
    print('Intersection')
    print(set_c)

    # Test to see if all managers are users
    users = {'Bob', 'Billy', 'Adam'}
    managers = {'Bob', 'Billy'}

    # Are all the managers users
    print(managers.issubset(users))

    if 'Adam' not in managers:
        print('Adam is not a manager')


if __name__ == "__main__":
    main()
