def array_of_products(array):
    # Write your code here.
    array_product = [1 for _ in range(len(array))]

    left_running_product = 1
    for i in range(len(array)):
        array_product[i] = left_running_product
        left_running_product *= array[i]

    right_running_product = 1
    for i in reversed(range(len(array))):
        array_product[i] *= right_running_product
        right_running_product *= array[i]

    return array_product, print(array_product)


if __name__ == '__main__':
    array = [5, 1, 4, 2]
    array_of_products(array)

"""Stay hungry, stay foolish"""
