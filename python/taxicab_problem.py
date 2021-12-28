##
#
# filename: taxicab_problem.py
# by: Abhay Gupta
# date: 03-26-2020
#
# Desc: Find the numbers that are the sum of two distinct cubes of integers
##


def taxicab(n):
    numbers = {}
    count = 0
    taxi_numbers = []

    while len(taxi_numbers) < n:
        count += 1
        instances = 0

        for i in range(1, int(count**(1/3)+1)):
            j = round((count - i**3)**(1/3))

            if j < i:
                break

            if j**3 + i**3 == count:
                instances += 1
                if instances == 2:
                    taxi_numbers.append(count)
                    break

    return taxi_numbers


def main():
    print(taxicab(10))


if __name__ == '__main__':
    main()
