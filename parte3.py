import random
import modulo

cont = 0
dict_seqs, list_ids = modulo.read_fastas()

for organism in dict_seqs.keys():
    position_aminoacid = random.randint(0, len(dict_seqs[organism]))
    list_aminoacids = ['A', 'B', 'C','D','E', 'F', 'G', 'H', 'I','K', 'L', 'M','N', 'P', 'Q', 'R','S', 'T', 'V', 'W',  'X', 'Y', 'Z']
    aminoacid_tochange = random.choice(list_aminoacids)
    new_seq = dict_seqs[organism][:position_aminoacid] + aminoacid_tochange + dict_seqs[organism][position_aminoacid+1:]
    print(f"Troca de {dict_seqs[organism][position_aminoacid]} por {aminoacid_tochange}, na posição {position_aminoacid+1} em {organism}")
        
    with open (f'/home/usuario/Documentos/Atividade/fastas_parte2/{organism}-mutacao', 'w') as file_final:
        file_final.write(f'>{list_ids[cont]}\n{new_seq}')
           

dict_seqs, list_ids = modulo.read_fastas()

cont = 0
while cont<4:
    organism = input(f"Escolha o {cont+1}º animal para a comparação de topoisomerase 1 mutada e não mutada:")
    modulo.comparation_seq(organism, f'{organism}-mutacao')
    cont += 1 
    







