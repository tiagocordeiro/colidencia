from revistas import ultimaRevista
from download import baixaRevista
from lista import processos, buscaProcurador



# Verifica o link para ultima revista
# ultimarevista = ultimaRevista()

# baixa o arquivo zip da ultima revista e descompacta na pasta xml
# baixaRevista(ultimarevista)

# Imprime os processos da ultima revista
# processos("downloads/xml/2454.xml")
# print("Fim da lista de processos")


# Retorna processos de um procurador específico
buscaProcurador("Marcelle de Oliveira Campos", "downloads/xml/2454.xml")
print("Fim da lista da Procuradoria MP revista 2454")


# buscaProcurador("Marcelle de Oliveira Campos", "downloads/xml/2455.xml")
# print("Fim da lista da Procuradoria MP revista 2455")