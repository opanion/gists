import pendulum

def main():
    dt1 = pendulum.datetime(2021, 7, 10, 23)
    dt2 = pendulum.datetime(2022, 1, 11)

    #print('-------Original Dates ------')
    #print(dt1.to_date_string())
    ##print(dt2.to_date_string())
    #print('------\n')
    #new_date = dt1.add(hours=1, days=5)
    #print(new_date.to_date_string())

    period = dt1.diff(dt2)
    print(period.in_days())
    print(dt2.diff_for_humans(dt1))
if __name__ == '__main__': main()