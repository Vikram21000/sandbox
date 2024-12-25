month_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]
def main():
    user_date = input("Date: ")
    try:
        if user_date[0].isalpha():
            long_date(user_date)
        else:
            short_date(user_date)
    except ValueError:
        main()

def short_date(user_date):
    month,day,year = user_date.split("/")
    month = int(month)
    day = int(day)
    year = int(year)
    if month > 12 or day > 31:
        raise ValueError
    else:
        print(f"{year}-{month:02}-{day:02}")

def long_date(user_date):
    months_days,years = user_date.split(", ")
    months,days = months_days.split(" ")
    index_month = month_list.index(months)+1
    if " " in days or " " in years:
        raise ValueError

    days = int(days)
    years = int(years)
    
    if days > 31:
        raise ValueError
    else:
        print(f"{years}-{index_month:02}-{days:02}")
main()


