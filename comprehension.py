
all_numbers = [12, -4, 57, 34, 89, 65, -21, 0, 67, 90]

# Create an empty list
# num = []
# # Loop over the numbers list, extract all even numberand append them into the empty list
# for numbers in all_numbers:
#      if numbers % 2 == 0:
#         num.append(numbers)
# # Display the list
# print(num)    

# List comprehension
even_numbers = [number for number in all_numbers if number % 2 == 0]
print(all_numbers)
print(even_numbers)

temp_data = {12.3, 23, 37.7, 40, 12, 18, 21}
above_25 = {temp for temp in temp_data if temp > 25}
print(temp_data)
print(above_25)