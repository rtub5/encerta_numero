import random
intents = 0 

baix = input("Desdes quin numero vols encertar:")
alt = input("Fins a: ")
if baix and alt.isnumeric():
    print("fica un numero!")


numero_a_encertar = random.randint(int(baix), int(alt))
while True:
    in_put = input("Encerta el numero entre el 0 i el 100: ")
    intents += 1 
    if in_put.isnumeric():
        intp = int(in_put)
        if intp < numero_a_encertar:
            print("Casi, el numero es més gran")
        elif intp > numero_a_encertar:
            print("Casi! El numero es més petit")
        elif intp == numero_a_encertar:
            print("Perfecte!")
            break
    else:
        print("ERROOOR!!!!!")

print("Intents: ", intents)