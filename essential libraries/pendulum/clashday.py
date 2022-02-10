import pendulum

def main():
    today = pendulum.today().format('dddd, MMMM Do')
    clash_date = pendulum.datetime(pendulum.now().year, 2, 7)
    clash_date_fmt =clash_date.format('dddd, MMMM Do')
    

    print(f'Today is: {today}')
    print(f'International Clash day is : {clash_date_fmt}')

    
    days_to = 0
    if pendulum.today() > clash_date:
        days_ago = pendulum.now().diff(clash_date).in_days()
        went_by = pendulum.now().subtract(days=days_ago).diff_for_humans()
        clash_date = clash_date.add(years=1)
        days_to = pendulum.now().diff(clash_date).in_days()
        print(f'International Clash went by : {went_by}')
    else: 
        days_to = clash_date.diff(pendulum.now()).in_days()
    print(f'It\'s {days_to} days until International Clash Day!')
if __name__ == '__main__': main()