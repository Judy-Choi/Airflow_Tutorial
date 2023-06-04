# 1. Get 'num_list' as an argument of function
# 2. Insert 10 to 'num_list'
# 3. Return list
def func_insert_list(num_list):
    num_list.append(10)
    return num_list

# 1. Get num_list (Return value of 'func_get_list')
# 2. Get sum value of the list
# 3. Return sum value


def func_sum_list(response_num_list):
    sum_val = sum(response_num_list)
    return sum_val

# Store data to output.txt


def func_save(sum_val):
    # Get return value of function 'func_sum_list' using task id 'id_sum_list'
    with open("output.txt", "w") as file:
        file.write(f"Sum of list: {sum_val}")


if __name__ == "__main__":
    num_list = [1, 2, 3]
    response_num_list = func_insert_list(num_list)
    sum_val = func_sum_list(response_num_list)
    func_save(sum_val)
