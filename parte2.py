import modulo

dict_seqs, list_ids = modulo.read_fastas()
cont = 0

while cont < 3:
    print("Escolha dois animais para a comparação da topoisomerase 1: horse, dog, hamster, rat \n Não repita as duplas!")
    organism1 = input("Escolha o primeiro organismo para comparação:")
    organism2 = input("Escolha o segundo organismo para comparação:")      
    modulo.comparation_seq(organism1, organism2)
    cont += 1