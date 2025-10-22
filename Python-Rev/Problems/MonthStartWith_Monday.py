import datetime as dt

year = int(input('Enter the Year: '))

monday = 0

for i in range(1, 13):  # months 1 to 12
    x = dt.date(year, i, 1)  # 1st day of each month
    
    if x.weekday() == 0:     # 0 means Monday
        monday += 1
        print(f"{x.strftime('%B')} starts on a Monday")

print(f"\nTotal months starting on Monday in {year}: {monday}")
