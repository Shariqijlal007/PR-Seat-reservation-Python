print(' PAKISTAN RAILWAYS TRAIN RESERVATION SYSTEM BY SHARIQ IJLAL TAHIR BEE-57B')

lst=list()
for i in range(1,51):
    lst.append(i)
fname=list()
for j in range(1,51):
    fname.append(j)
lname=list()
for k in range(1,51):
    lname.append(k)
email=list()
for k in range(1,51):
    email.append(k)
phonep=list()
for i in range(1,51):
    phonep.append(i)
agep=list()
for i in range(1,51):
    agep.append(i)
r=1
while r !=0:
    print("  Train: Rawalpindi Express ")
    print("  Train Information:")
    print("   Time of departure: 1500hrs")
    print("   Time of Arrival: 2100hrs")
    print("   Travel Duration: 6 hrs")
    print("   City of Arrival: Lahore")
    print("   departure: Rawalpindi")
    print("   Fare of route: fare from Rawalpindi")
    print("1.Book Ticket ")
    print("2.Check Ticket Status ")
    print('3.Cancel Ticket')
    print("4.Check detail of Booked Ticket ")
    print('5.Exit ')
    choice = int(input("\nEnter your option : "))
    if choice==1:
        tic=int(input('Enter seat no.: '))
        if lst[tic-1]==tic:
            fname1=str(input('Enter your First name: \n'))
            lname1=str(input('Enter your Last name: \n'))
            email1=str(input('Enter your Email: \n'))
            phone1=int(input('Enter your Phone no.: \n'))
            age1=int(input('Enter your age: \n'))
            lst.pop(tic-1)
            fname.pop(tic-1)
            lname.pop(tic-1)
            email.pop(tic-1)
            phonep.pop(tic-1)
            agep.pop(tic-1)
            lst.insert(tic-1,'B')
            fname.insert(tic-1,fname1)
            lname.insert(tic-1,lname1)
            email.insert(tic-1,email1)
            phonep.insert(tic-1,phone1)
            agep.insert(tic-1,age1)
            print('\n*************************')
            print("Your Ticket has been booked successfully.")
            print('*************************\n')
        else:
            print('\n*************************')
            print('Seat is already booked, please try another seat.')
            print('*************************\n')
    elif choice==2:
        for k in lst:
            print(k,end=" ")
        print('\n')
    elif choice==3:
        tic=int(input('Enter seat no.: '))
        if lst[tic-1]==tic:
            print('\n*************************')
            print("This seat has not been Booked")
            print('*************************\n')
        else:
            lst.pop(tic-1)
            lst.insert(tic-1,tic)
            print('\n*************************')
            print('Your ticket has been canceled')
            print('*************************\n')
    elif choice==4:
        s=int(input('Enter seat no.: \n'))
        s=s-1
        if fname[s]==s+1:
            print('\n*************************')
            print('This seat is not booked')
            print('*************************\n')
        else:
            print('\n*************************')
            print('Passenger Name is :',fname[s].title(),lname[s].title())
            print('Email :',email[s].title())
            print('Phone no. :',phonep[s])
            print('his/her Age :',agep[s])
            print('*************************\n')
    elif choice==5:
        r=0
        exit()
    else:
        print('\n*************************')
        print('you have entered the wrong key\n')
        print('*************************\n')
