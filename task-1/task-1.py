from datetime import datetime

def get_days_from_today(date: str)->int:    
    try:
        now = datetime.today().date()
        check_date = datetime.strptime(date, '%Y-%m-%d').date()
        difference = now - check_date
        return difference.days
    except TypeError:
        print("Oops! That was not valid value. Try again...")
    except ValueError:
        print("Oops! Date does not match the format 'YYYY-MM-DD'. Try again...")   
