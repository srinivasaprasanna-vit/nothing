t=10
i=0

while(i<t):
    n=int(input())
    print(f"Booking {n} tickets")
    s=str(input())
    yes="yes"
    no="no"
    if s==yes and n<=(t-n-i):
        print(f"Remaining Seats: {t-n-i}")
        i+=n
    elif s==no:
        print("All seats have been booked.Thank you!")
    else:
        print("Not enough seats available.")
    
print("Thank you for using our Ticket Booking System!")