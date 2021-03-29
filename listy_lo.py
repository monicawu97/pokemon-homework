food= ['rice', 'beans']
food.append('broccoli')
food.extend(['bread','pizza'])
print (food[:2])
print (food[-1:])

groceries= "eggs,fruit,orange juice"
breakfast= groceries.split (",")
print (breakfast)
print (len(breakfast))




user_list = []
user_input = "start"
while user_input != "stop":
    user_input = input("Enter Values until stop:")
    if user_input == "stop":
        breakpoint
    else:
        user_list.append(user_input)
for numbers in range(len(user_list)):
    user_list[numbers] = float(user_list[numbers])
print(f"average: {sum(user_list)/float(len(user_list))}")
print(f"Maximum is: {min(user_list)}")
print(f"Minimum is: {max(user_list)}")