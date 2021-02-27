import os
from Bio import SeqIO
import matplotlib.pyplot as plt 
import pandas as pd

files_fastas = os.listdir('/home/usuario/Documentos/Atividade/fastas_parte1')

aminoacids_dict={'A': 'Alanina', 'B': 'Asparagina ou ácido aspártico', 'C': 'Citosina', 
'D': 'Ácido aspártico', 'E': 'Ácido Glutâmico', 'F': 'Fenilalanina', 'G': 'Glicina', 
'H': 'Histidina', 'I': 'Isoleucina',  'K': 'Lisina', 'L': 'Leucina', 'M': 'Metionina', 
'N': 'Asparagina', 'P': 'Prolina', 'Q': 'Glutamina', 'R': 'Arginina','S': 'Serina',  
'T': 'Treonina', 'V': 'Valina', 'W': 'Triptofano',  'X': 'Desconhecido', 'Y': 'Tirosina', 
'Z': 'Glutamina ou ácido glutâmico'}

for file in files_fastas:
    seq_aminoacids = (SeqIO.read(f'/home/usuario/Documentos/Atividade/fastas_parte1/{file}', 'fasta')).seq
    list_position, frequency = [], 0

    with open('/home/usuario/Documentos/Atividade/proteina-aminoacidos.txt','w') as file_final:
            file_final.write(f'Código do aminoácido\t Nome do aminoácido\t Frequência\t Posições\t \n')
            
    for key, value in zip(aminoacids_dict.keys(), aminoacids_dict.values()):
        for aminoacid_position in range(len(seq_aminoacids)):
            if seq_aminoacids[aminoacid_position] == key:
                frequency += 1
                list_position.append(aminoacid_position+1)
        with open('/home/usuario/Documentos/Atividade/proteina-aminoacidos.txt','a') as file_final:
            file_final.write(f'{key}\t {value}\t {frequency}\t {list_position}\t \n')
        list_position, frequency = [], 0


##HISTOGRAMA
df = pd.read_csv('/home/usuario/Documentos/Atividade/proteina-aminoacidos.txt', sep='\t')
total_frequency = list(df.iloc[:,2])

plt.bar(list(aminoacids_dict.keys()), height=total_frequency, color='green')
plt.xlabel('Código letra única do aminoácido')
plt.ylabel('Frequência em número de ocorrências')
plt.savefig('/home/usuario/Documentos/Atividade/histograma.png')

print('Arquivos criados: proteina-aminoacidos.txt e histograma.png')

