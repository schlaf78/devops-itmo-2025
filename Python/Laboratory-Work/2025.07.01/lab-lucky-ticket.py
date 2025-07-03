
TicketNumber = input( "Enter ticket number:")

#String Length Check
if len(TicketNumber) > 6:
    print("Ticket Number contains 6 symbols max.")
else:
    print("You enter:", TicketNumber)

#Check and comparing of the ticket number summ
Digit1 = int(TicketNumber[0])
Digit2 = int(TicketNumber[1])
Digit3 = int(TicketNumber[2])
Digit4 = int(TicketNumber[3])
Digit5 = int(TicketNumber[4])
Digit6 = int(TicketNumber[5])

SumLeft = Digit1 + Digit2 + Digit3
SumRight = Digit4 + Digit5 + Digit6

if SumLeft == SumRight:
    print("Your ticket is lucky")
else:
    print("Your ticket is unlucky")
print(SumLeft, SumRight)
