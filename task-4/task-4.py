from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    now = datetime.today().date()
    current_year = now.year

    birthday_congratulate_list = []

    for user in users:   
        user_birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        user_birthday_month = user_birthday.month
        user_birthday_date = user_birthday.day

        birthday_this_year = datetime(year=current_year, month=user_birthday_month, day=user_birthday_date).date()

        difference_birthday = birthday_this_year - now

        if difference_birthday.days >= 0 and difference_birthday.days <= 7:
            corrected_birth_date = birthday_this_year

            if birthday_this_year.weekday() == 5:
                corrected_birth_date = birthday_this_year + timedelta(days=2)

            elif birthday_this_year.weekday() == 6:
                corrected_birth_date = birthday_this_year + timedelta(days=1)

            congratulation_date = corrected_birth_date.strftime('%Y.%m.%d') 
            birthday_congratulate_list.append({'name': user['name'], 'congratulation_date': congratulation_date})
    
    return birthday_congratulate_list


