import random 

def create(l):


    let = "abcdefghijklmnopqrstuvwxyz"
    num = "1234567890"
    sym = "!@#$%^&*"

    dict = {}

    risposta = input("Vuoi un set di lettere nella password?:")
    if risposta == 'si':

        dict["lettere"]=let

    risposta = input("Vuoi un set di symbol nella password?:")
    if risposta == 'si':
        dict["symbol"]=sym

    risposta = input("Vuoi un set di numeri nella password?:")
    if risposta == 'si':

        dict["numeri"]=num


    def generatorpass():
        listasymbol = []
        for elemento in dict:
            listasymbol.append(dict[elemento])

        stringasymbol = "".join(listasymbol)
        password = []
        for i in range(0,l):
            password.append(random.choice(stringasymbol))
        pas = "".join(password)
        return print(pas)

    generatorpass()

create(7)   