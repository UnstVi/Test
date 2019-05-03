

def main():
    name = input("Enter car's name: ")
    name = name.capitalize()
    file = open("cars.txt")
    similar = 0
    for i in file:
        if name in i:
            i.replace('\n', '')
            i = i.split(' - ', 2)
            print(name,' price is ',i[1])
            similar = True
            file.close()
            break
    if not(similar):
        new_car = n_price()
        print(str(name,' price is ',' '.join(new_car)))
        file = open("cars.txt", "a")
        file.write('\n',name," - ",' '.join(new_car))
        file.close()
def n_price():
    try:
        tar_for_car = int(input('Enter price: '))
    except ValueError:
        print("Enter numbers")
        return n_price()
        tar_for_car = str(tar_for_car)
    mon = input('Enter (USD, EUR, GBP) ')
    mon = mon.upper()
    if mon == 'USD' or mon == 'EUR' or mon == 'GBP':
        return tar_for_car, mon
    else:
        print("USD, EUR, GBP")
        return n_price()
main()