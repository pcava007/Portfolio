from datetime import datetime, timedelta

def calculate_shift_hours(clock_in, clock_out):
    # Calculate total shift duration in minutes
    shift_duration = (clock_out - clock_in).total_seconds() / 60
    
    # Subtract breaks every 4 hours
    num_breaks = shift_duration // 240  # 240 minutes = 4 hours
    total_break_duration = num_breaks * 30  # 30 minutes break per 4 hours
    
    # Calculate net shift duration after deducting breaks
    net_shift_duration = shift_duration - total_break_duration
    
    # Convert duration to hours and minutes
    net_shift_hours = int(net_shift_duration // 60)
    net_shift_minutes = int(net_shift_duration % 60)
    
    return net_shift_hours, net_shift_minutes

# Get the year
year = int(input("Enter the year: "))

# Get number of dates and loop through them
num_dates = int(input("Enter the number of dates: "))
shift_details = []

for i in range(num_dates):
    print(f"\nShift {i+1}:")
    month = int(input("Enter the month (MM): "))
    day = int(input("Enter the day (DD): "))

    valid_input = False
    while not valid_input:
        clock_in_time_str = input("Enter the clock-in time (H:MM AM/PM): ")
        clock_out_time_str = input("Enter the clock-out time (H:MM AM/PM): ")
        
        try:
            # Convert time input to datetime objects
            clock_in_datetime = datetime.strptime(f"{year}-{month:02d}-{day:02d} {clock_in_time_str}", "%Y-%m-%d %I:%M %p")
            clock_out_datetime = datetime.strptime(f"{year}-{month:02d}-{day:02d} {clock_out_time_str}", "%Y-%m-%d %I:%M %p")
            
            # Calculate the net shift hours and minutes
            net_shift_hours, net_shift_minutes = calculate_shift_hours(clock_in_datetime, clock_out_datetime)
            net_shift_duration = timedelta(hours=net_shift_hours, minutes=net_shift_minutes)
            
            valid_input = True
        except ValueError:
            print("Invalid time format. Please enter the time in H:MM AM/PM format.")

    # Append shift details to the list
    shift_details.append((clock_in_datetime, clock_out_datetime, net_shift_duration))

# Print the shift details table
print("\nShift Details:")
print("-----------------------------------------------------------")
print("| Date       | Clock-in     | Clock-out    | Shift Duration |")
print("-----------------------------------------------------------")
for shift in shift_details:
    clock_in_datetime, clock_out_datetime, net_shift_duration = shift
    clock_in_time_str = clock_in_datetime.strftime("%I:%M %p")
    clock_out_time_str = clock_out_datetime.strftime("%I:%M %p")
    net_shift_hours = net_shift_duration // timedelta(hours=1)
    net_shift_minutes = (net_shift_duration % timedelta(hours=1)).seconds // 60
    print(f"| {clock_in_datetime.strftime('%Y-%m-%d')} | {clock_in_time_str.ljust(12)} | {clock_out_time_str.ljust(12)} | {str(net_shift_hours).rjust(2)}:{str(net_shift_minutes).rjust(2)}            |")
print("-----------------------------------------------------------")

# Calculate the total shift duration
total_shift_duration = sum(shift[2].total_seconds() for shift in shift_details)
total_shift_duration = timedelta(seconds=total_shift_duration)

# Ask for the pay rate
pay_rate = float(input("\nEnter your pay rate per hour: $"))

# Calculate the total pay
total_pay = total_shift_duration.total_seconds() / 3600 * pay_rate

# Print the total shift duration and pay
total_shift_hours = total_shift_duration // timedelta(hours=1)
total_shift_minutes = (total_shift_duration % timedelta(hours=1)).seconds // 60
print(f"\nTotal shift duration: {total_shift_hours:02d}:{total_shift_minutes:02d}")
print(f"Total pay: ${total_pay:.2f}")
