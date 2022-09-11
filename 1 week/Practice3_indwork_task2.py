def season_events(number_of_month):
    if number_of_month == 1:
        return 'You were born in January. White snow fell outside the window.'
    elif number_of_month == 2:
        return 'You were born in February. White snow fell outside the window.'
    elif number_of_month == 3:
        return 'You were born in March. Birds sang beautiful songs.'
    elif number_of_month == 4:
        return 'You were born in April. Birds sang beautiful songs.'
    elif number_of_month == 5:
        return 'You were born in May. Birds sang beautiful songs.'
    elif number_of_month == 6:
        return 'You were born in June. The sun shone brighter than ever.'
    elif number_of_month == 7:
        return 'You were born in July. The sun shone brighter than ever.'
    elif number_of_month == 8:
        return 'You were born in August. The sun shone brighter than ever.'
    elif number_of_month == 9:
        return 'You were born in September. The harvest was incredible.'
    elif number_of_month == 10:
        return 'You were born in October. The harvest was incredible.'
    elif number_of_month == 11:
        return 'You were born in November. The harvest was incredible.'
    elif number_of_month == 12:
        return 'You were born in December. White snow fell outside the window.'
    else:
        return 'You need to enter the real number of the month.'
n = int(input('Enter the number of month: '))
print(season_events(n))
#Sepbossynova Laura CS-2120
