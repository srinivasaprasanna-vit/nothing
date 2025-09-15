t=10
i=0

while(t>0):
    
    n=int(input())
    if n<=t:
        print(f"Booking {n} tickets")
        s=str(input())
        if s=='yes' and n<=(t-n):
            t=t-n
            print(f"Remaining Seats: {t}")
        elif s=='no':
            print("All seats have been booked.Thank you!")
    else:
        print("Not enough seats available.")
print("Thank you for using our Ticket Booking System!")