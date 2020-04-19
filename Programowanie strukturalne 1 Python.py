'''
print("cdv")
print(2)
print('test')

#potęga
pow=2**10
print(pow)

text="CDV"
print(text * 2)

#pobieranie danych z klawiatury
name=input()
print("Twoje imię: " + name)
surname = input("Podaj swoje nazwisko: ")
print("Imie: " + name + ", nazwisko: " + surname)

lenghtSurname=len(surname)  #<class 'str'>
print(type(surname))        #<class 'int'>
print(type(lenghtSurname))
lenghtSurname=str(lenghtSurname)
print("Długość nazwiska: " + lenghtSurname)
'''
'''
Użytownik podaje z klawiatury
imie i nazwisko oraz wiek
wyswietl w formacie:
Imie i nazwisko: ....., wiek: .....
'''

'''
name = input("Podaj imie: ")
surname = input("Podaj nazwisko: ")
age = input("Podaj wiek: ")
print("Imie i nazwisko: " + name + " " + surname + ", "+ "wiek: " + age)
'''

#konwersja
x="5"
print(type(x))  #str
x=int(x)
print(type(x))  #int

y=5
y=4
print(type(y))  #int
y=y/2
#y/=2
print(type(y))  #float
print(y)        #2.0

surname="Kowalski"
print(surname[0])   #K
print(surname[0:3])   #Kow
print(surname[-2])   #k
print(surname[-2:])   #ki
print(surname[:-2])   #Kowals
print(surname[:-2:2])   #Kwl