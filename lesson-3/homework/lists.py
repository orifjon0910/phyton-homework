
#1
numbers = [1,2 ,3, 1, 4, 6, 1]
numbers.count(1)

#2
apple = [1, 2, 3, 4, 5]
total = sum(apple)
print(total)

#3
apple = [1, 2, 3, 4, 5]
new_apple = max(apple)
print(new_apple)


#4
apple = [1, 2, 3, 4, 5]
new_apple = min(apple)
print(new_apple)


#5
apple = [1, 2, 3, 4, 5]
element = 4
if element in apple:
    print("Yes")
else:
    print("No")   


#6
apple = [1, 2, 3, 4, 5]
new_apple = print(apple[0])

#7
apple = [1, 2, 3, 4, 5]
new_apple = print(apple[-1])

#8
apple = [1, 2, 3, 4, 5]
new_apple = print(apple[:3])

#9
apple = [1, 2, 3, 4, 5]
apple.reverse()
print(apple)

#10
apple = [5, 6, 3, 1, 5]
apple.sort()
print(apple)

#11
apple = [5, 6, 6, 3, 1, 5]
new_apple = set(apple)
print(new_apple)


#12
my_list = [1, 2, 3, 5]
element = 4
index = 3  

my_list.insert(index, element)
print(my_list)

#13
apple = [1, 4, 4, 7, 8]
element = 4
print(apple.index(element))

#14
my_list = []
is_empty = not my_list  
print(is_empty)

#15
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = sum(num for num in my_list if num % 2 == 0)
print(even_count)

#16
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_count = sum(num for num in my_list if num % 2 != 0)
print(odd_count)

#17
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)

#18
main_list = [1, 2, 3, 4, 5, 6]
sub_list = [3, 4, 5]

exists = str(sub_list)[1:-1] in str(main_list)[1:-1]
print(exists)

#19
apple = [3, 7, 8, 19, 21]
old = 7
new = 9
if old in apple:
    index = apple.index(old)  
    apple[index] = new 
    print(apple)


#20
my_number = [10, 20, 4, 45, 99, 99]
second_largest = sorted(set(my_number))[-2]  
print(second_largest)

#21
my_list = [10, 20, 4, 45, 99, 4]
second_smallest = sorted(set(my_list))[1]  
print(second_smallest)

#22
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = [num for num in my_list if num % 2 == 0]  
print(even_list)

#23
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_list = [num for num in my_list if num % 2 != 0]  
print(odd_list)

#24
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = len(my_list)
print(length)

#25
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
asd = my_list.copy()
print(asd)

#26
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
asd = len(my_list)
mid = asd // 2
if length % 2 == 0:
    middle_elements = [my_list[mid - 1], my_list[mid]]  # Two middle elements
else:
    middle_elements = my_list[mid]  # Single middle element

print(middle_elements)


# %%
#27
my_list = [1, 3, 5, 7, 9, 2, 4, 6, 8]
start, end = 2, 6  
sublist = my_list[start:end]  
max_element = max(sublist)  
print(max_element)

# %%
#28
my_list = [1, 3, 5, 7, 9, 2, 4, 6, 8]
start, end = 2, 6  
sublist = my_list[start:end]  
min_element = min(sublist)  
print(min_element)

# %%
#29
my_list = [1, 2, 3, 4, 5]
index = 2 
del my_list[index]
print(my_list)

# %%
#30
my_list = [1, 2, 3, 4, 5]
is_sorted = my_list == sorted(my_list)  
print(is_sorted)

# %%
#31
my_list = [1, 2, 3]
repeat_times = 3  
repeated_list = [num for num in my_list for _ in range(repeat_times)]
print(repeated_list)


# %%
#32
list1 = [3, 1, 4]
list2 = [2, 5, 6]
merged_sorted = sorted(list1 + list2)  
print(merged_sorted)

# %%
#33
my_list = [1, 2, 3, 2, 4, 2]
element = 2
indices = [i for i, x in enumerate(my_list) if x == element]
print(indices)

# %%
#34
my_list = [1, 2, 3, 4, 5]
shift = 2  
rotated = my_list[-shift:] + my_list[:-shift]
print(rotated)

# %%
#35
range_list = list(range(1, 11))  
print(range_list)

# %%
#36
my_list = [-3, 5, -1, 7, -2, 10]
positive_sum = sum(num for num in my_list if num > 0)
print(positive_sum)

# %%
#37
negative_sum = sum(num for num in my_list if num < 0)
print(negative_sum)

# %%
#38
my_list = [1, 2, 3, 2, 1]
is_palindrome = my_list == my_list[::-1]
print(is_palindrome)

# %%
#39
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
size = 3
nested_list = [my_list[i:i + size] for i in range(0, len(my_list), size)]
print(nested_list)

# %%
#40
my_list = [1, 2, 2, 3, 4, 3, 5, 6, 5]
unique_list = list(dict.fromkeys(my_list))  
print(unique_list)

