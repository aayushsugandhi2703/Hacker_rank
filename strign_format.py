def convert(number):
    for i in range(1,number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]

        print(f'{deci}, {octa}, {hexa}, {bina}')

n = int(input())
convert(n)