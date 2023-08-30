month_dict = {
    'Jan': 31,
    'Feb1': 28,
    'Feb2': 29,
    'Mar': 31,
    'Apr': 30,
    'May': 31,
    'Jun': 30,
    'Jul': 31,
    'Aug': 31,
    'Sep': 30,
    'Oct': 31,
    'Nov': 30,
    'Dec': 31
}

year = 1900
month = 'Jan'
day = 1
day_name = 'Mon'

day_names = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
month_names = ['Jan', 'Feb1', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

results = []
while True:

    if day == 31 and month == 'Dec' and year == 2000:
        break

    if day == 1 and day_name == 'Sun':
        results.append((month, year))

    # increment day
    try:
        day_name = day_names[day_names.index(day_name) + 1]
    except IndexError:
        day_name = 'Mon'

    if day >= month_dict[month]:
        day = 1
        try:
            if year % 4 == 0:
                month_names[1] = 'Feb2'
                if year % 100 == 0:
                    month_names[1] = 'Feb1'
                    if year % 400 == 0:
                        month_names[1] = 'Feb2'
            else:
                month_names[1] = 'Feb1'

            month = month_names[month_names.index(month) + 1]
        except IndexError:
            month = 'Jan'
            year += 1
    else:
        day += 1    

results = [i for i in results if i[1] != 1900]
total = len(results)

print(total)

