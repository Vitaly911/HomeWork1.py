Peter = 0
Kate = 0
Seryozha = 0
number = 24
if number % 6 != 0:
    print("Нельзя определить")
else:
    if number % 6 == 0:
        Peter = number // 6
        Seryozha = number // 6
        Kate = Seryozha * 4
        print(Peter, Kate, Seryozha)