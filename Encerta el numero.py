import random
import time

intents = 0 

baix = input("Des de quin numero vols encertar:")
alt = input("Fins a: ")
if baix and alt.isnumeric():
    print("Perfecte!")
else:
  print("No pots entrar lletres! El pròxim cop ja ho faràs bé")
  time.sleep(0.5)
  print("El programa és tancarà en 10 segons")
  time.sleep(10)
  quit()

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
        time.sleep(0.5)
        print("Només pots entrar lletres!")
        #quit()
print("Intents: ", intents)
