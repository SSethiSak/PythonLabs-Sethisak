def find_largest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], find_largest(lst[1:]))


user_input = input("enter a list of integers (space-separated): ")
lst = [int(x) for x in user_input.split()]
largest = find_largest(lst)
print("the largest element in the list is:", largest)