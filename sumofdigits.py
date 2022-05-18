# Finding the sum of the digits of each number
for count in range(1, 101):
    
    sum_of_count = 0
    string_number = str(count)
    for i in string_number:
        sum_of_count += int(i)
        
    if i == sum_of_count:
        print(count) 
