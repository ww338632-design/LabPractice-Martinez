def seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

def hms_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

def convert_24_to_12(hour, minute):
    if hour == 0:
        period = "AM"
        hour_12 = 12
    elif hour < 12:
        period = "AM"
        hour_12 = hour
    elif hour == 12:
        period = "PM"
        hour_12 = 12
    else:
        period = "PM"
        hour_12 = hour - 12
    return f"{hour_12}:{minute:02d} {period}"

def convert_12_to_24(hour, minute, period):
    period = period.upper()
    if period == "AM":
        if hour == 12:
            hour_24 = 0
        else:
            hour_24 = hour
    else:
        if hour== 12:
            hour_24 = 0
        else:
            hour_24 = hour + 12
    return f"{hour_24:02d}:{minute:02d}"

def show_menu():
    print("\n==== TIME CONVERTER ====")
    print("1. Seconds -> Hours, Minutes, Seconds")
    print("2. Hours, Minutes, Seconds -> Seconds")
    print("3. 24-Hour -> 12-Hour format")
    print("4. 12-Hour -> 24-Hour format")
    print("5> Exit")
    
while True:
    show_menu()
    choice = input("Enter your choice(1-5): ")
    
    if choice == "1":
        total = int(input("Enter total seconds: "))
        h, m, s = seconds_to_hms(total)
        print(f"Result: {h} hour(s), {m} minute(s), {s} second(s)")
    elif choice == "2":
        h = int(input("Enter Hours: "))
        m = int(input("Enter minute(: "))
        s = int(input("Enter seconds: "))
        print(f"Result: {hms_to_seconds(h, m,s)} second(s)")
    elif choice == "3":
        h = int(input("Enter hour(0-23): "))
        m = int(input("Enter minute(0-59): "))
        if 0 <= h <= 23 and 0 <= m <= 59:
            print(f"Result {convert_24_to_12(h, m)}")
        else:
            print("Invalid time!")
    elif choice == "4":
        h = int(input("Enter hour(1-12): "))
        m = int(input("Enter minute(0-59): "))
        p= input("AM or PM: ")
        if 1 <= h <= 12 and 0 <= m <=59 and p.upper() in ("AM", "PM"):
            print(f"Result {convert_12_to_24(h,m,p)}")
        else:
            print("Invalid time!")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 to 5.")