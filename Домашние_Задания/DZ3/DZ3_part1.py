def sum_distance(count_from=0,count_to=0):
    if(count_from < count_to):
        sum = 0
        for i in range(count_from,count_to,+1):
            sum = sum+i
            print (sum)
    else:
        sum =0
        for i in range(count_to,count_from,+1):
            sum = sum+i
        

first_count = 2
second_count = 5

sum_distance(first_count,second_count)