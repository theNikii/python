def trim_and_repeat(untrim_string,offset=0,repetitions=1):
    trim_string = ''
    for i in range(0,repetitions,+1):
        count_loop = 0
        for simvol in untrim_string: 
            if(count_loop >= offset):
                trim_string += simvol
            count_loop+=1   
    return trim_string
untrim_string = 'fdgegdefd'
offset = 1
repetitions = 3

trim_and_repeat(untrim_string,offset,repetitions)
