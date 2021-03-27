food= ['rice', 'beans']
food.append('broccoli')
food.extend(['bread','pizza'])
print (food[:2])
print (food[-1:])

groceries= "eggs,fruit,orange juice"
breakfast= groceries.split (",")
print (breakfast)
print (len(breakfast))

values= input("floating point values:")
print (values)


if name == "main":
    user_list = []
    user_input = "start"
    while user_input != "stop":
        user_input = input("please:")
        if user_input == "stop":
            breakpoint
        else:
            user_list.append(user_input)
    for i in range(len(user_list)):
        user_list[i] = float(user_list[i])
    print(f"average: {sum(user_list)/float(len(user_list))}")