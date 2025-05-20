import subprocess


process = subprocess.Popen(
    ["bash"],
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
    universal_newlines=True
)

ativacao_unicycler = "conda activate unicycler"
stdout, stderr = process.communicate(ativacao_unicycler)

#aqui vem o codigo que usamos no unicycler
#comando_unicycler = 

montagem = ''

print("Saida:")
print(stdout)
f = open("arquivo.txt","r") 
conteudo = f.read()

#Quasta
#qtd de contig 
#alto valor de N5
#L50 proximo de 1

#if(qualidade = boa )
    #checkm
    #if(contaminação >= 1)


if stderr:
    print("Erros;")
    print(stderr)