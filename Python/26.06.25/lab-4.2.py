#Restaurant Bill Calculator

print("Please Enter Restaurant Bill Total:")
Bill_total = int (input())
Tax = round(Bill_total * 30 / 100,2)
Tips = round(Bill_total * 10 / 100,2)


print(f"Tax of {Bill_total} is: {Tax}")
print(f"Tips of the waiter of {Bill_total} are: {Tips}")