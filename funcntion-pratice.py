#finding the maximum of 3 numbers
def max_num(num1, num2, num3):
    max_number = max(num1, num2, num3)
    return max_number

#multiplying all the numbers in a list
def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

#reversing a string
def rev_string(string):
    reversed_string = string[::-1]
    return reversed_string

#checking whether a number falls in a given range
def num_within(number, start_range, end_range):
    if start_range <= number <= end_range:
        return True
    else:
        return False

#printing out the first rows of n rows of Pascal's triangle
def pascal(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                num = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(num)
        triangle.append(row)

    for row in triangle:
        print(' '.join(str(num) for num in row))

