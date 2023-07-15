def price(x, y):
    return x * y

print("1.Dates price------- 3.3 - taka per gram")
print("2.Blueberry price--- 3.5 - taka per gram")
print("3.Apple price------- 1.3 - taka per gram")
print("4.Grape price------- 3.0 - taka per gram")

while True:
    choice = input("Select your item(1 - 4): ")
    print()

    if choice == '1':
        weights = float(input("Enter Dates waighth in gram: "))
        prices = float(input("Enter Dates price per gram : "))
        print("Total waight : ", weights/1000, "kg")
        print("Dates price  : ", price(weights, prices), "Taka")

    elif choice == '2':
        weights = float(input("Enter Blueberry waighth in gram: "))
        prices = float(input("Enter Blueberry price per gram : "))
        print("Total waight    : ", weights/1000, "kg")
        print("Blueberry price : ", price(weights, prices), "Taka")

    elif choice == '3':
        weights = float(input("Enter Apple waighth in gram: "))
        prices = float(input("Enter Apple price per gram : "))
        print("Total waight : ", weights/1000, "kg")
        print("Apple price  : ", price(weights, prices), "Taka")

    elif choice == '4':
        weights = float(input("Enter Grape waighth in gram: "))
        prices = float(input("Enter Grape price per gram : "))
        print("Total waight : ", weights/1000, "kg")
        print("Grape price  : ", price(weights, prices), "Taka")

    print()   
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
    else:
        pass