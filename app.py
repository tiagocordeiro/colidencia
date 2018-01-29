from revistas import ultimaRevista
from download import baixaRevista
from lista import processos, buscaProcurador



# Verifica o link para ultima revista
ultimarevista = ultimaRevista()

# baixa o arquivo zip da ultima revista e descompacta na pasta xml
baixaRevista(ultimarevista)

# Imprime os processos da ultima revista
processos()

# Retorna processos de um procurador específico
buscaProcurador("Marcelle de Oliveira Campos")
