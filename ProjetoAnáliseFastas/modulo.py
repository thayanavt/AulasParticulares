import os
from Bio import SeqIO

dict_seqs = {}
list_ids = []

def read_fastas():
    list_fastas = os.listdir('/home/usuario/Documentos/Atividade/fastas_parte2')
    for file in list_fastas:
        protein = SeqIO.read(f'/home/usuario/Documentos/Atividade/fastas_parte2/{file}', 'fasta')
        id_protein = protein.id
        list_ids.append(id_protein)
        seq_protein = protein.seq
        dict_seqs[f'{file}'.replace('.fasta', '')] = str(seq_protein)
    return dict_seqs, list_ids

def comparation_seq(organism1, organism2):
    min_seq = min(len(dict_seqs[organism1]), len(dict_seqs[organism2]))
    for position, amino1, amino2 in zip(range(1,min_seq), dict_seqs[organism1], dict_seqs[organism2]):
        if amino1 != amino2:
            with open ('/home/usuario/Documentos/Atividade/comparation_topoisomerase1', 'a') as file_final:
                file_final.write(f'Position|{organism1}|{organism2}\n')
                file_final.write(f'{position}\t|{amino1}    |{amino2}\n\n')            
            print("Posição adicionada ao arquivo \n")
            break