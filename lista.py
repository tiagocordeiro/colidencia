import xml.etree.ElementTree as ET
import os

downloads_folder = "downloads/xml"
arquivos = []

empresa_registro = "SPI - Marcas e Patentes S/C Ltda."
processos_casa = []

for file in os.listdir(downloads_folder):
    if file.endswith(".xml"):
        # print(os.path.join(downloads_folder, file))
        arquivos.append(file)

ultimo_arquivo = os.path.join(downloads_folder, arquivos[-1])


def processos(arquivo=ultimo_arquivo):
    tree = ET.parse(arquivo)
    root = tree.getroot()
    quebra = 0

    for processo in root.iter('processo'):
        # Quebra para teste
        quebra = quebra + 1
        if quebra == 100:
            break

        print('📂 Processo:    ', processo.attrib)
        # print(processo.attrib['numero'])

        for despacho in processo.iter('despacho'):
            print('\u255F\u2500\u2500 Despacho:   ', despacho.attrib)

        for texto in processo.iter('texto-complementar'):
            print('\u255F\u2500\u2500 Texto comp.:', texto.text)

        for protocolo in processo.iter('protocolo'):
            print('\u255F\u2500\u2500 Protocolo:  ', protocolo.attrib)

        for requerente in processo.iter('requerente'):
            print('\u255F\u2500\u2500 Requerente: ',
                  requerente.attrib['nome-razao-social'])

        for procurador in processo.iter('procurador'):
            print('\u255F\u2500\u2500 Procurador: ', procurador.text)

        for marca in processo.iter('marca'):
            print('\u255F\u2500\u2500 Marca:      ', marca.attrib)

        for nome in processo.iter('nome'):
            print('\u255F\u2500\u2500 Nome:       ', nome.text)

        for titular in processo.iter('titular'):
            print('\u255F\u2500\u2500 Titular:    ', titular.attrib)

        for classe in processo.iter('classe-nice'):
            print('\u255F\u2500\u2500 Classe Nice:', classe.attrib['codigo'])

        for especificacao in processo.iter('especificacao'):
            print('\u2559\u2500\u2500 Especific.: ', especificacao.text)

        print('\u2550' * 79)


def buscaProcurador(empresa=empresa_registro, arquivo=ultimo_arquivo):
    tree = ET.parse(arquivo)
    root = tree.getroot()

    for processo in root.iter('processo'):
        #print('Processo: ', processo.attrib['numero'])

        for procurador in processo.iter('procurador'):
            #print('Procurador: ', procurador.text)
            if procurador.text == empresa:
                processos_casa.append(processo.attrib['numero'])

    print(processos_casa)
    return processos_casa


if __name__ == '__main__':
    protocolos = processos()
    # procuradores = buscaProcurador('A Provincia Marcas e Patentes Ltda.')
