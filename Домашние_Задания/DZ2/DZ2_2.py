# результат н слов = %

list_requests = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт'
]
two_count_words = 0
three_count_words = 0
count_words = 0
for request in list_requests:
    count_words = count_words+1
    words=request.split()
    if(len(words) == 2):
        two_count_words = two_count_words + 1
    elif(len(words) ==3):
        three_count_words = three_count_words + 1

print(f"Поисковых запросов, содержащих 2 слов(а):{round(two_count_words/count_words*100,2)}%")

print(f"Поисковых запросов, содержащих 3 слов(а):{round(three_count_words/count_words*100,2)}%")