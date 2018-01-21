import xml.etree.ElementTree as ET
import os


downloads_folder = "downloads/xml"
arquivos = []

for file in os.listdir(downloads_folder):
    if file.endswith(".xml"):
        # print(os.path.join(downloads_folder, file))
        arquivos.append(file)

ultimo_arquivo = os.path.join(downloads_folder, arquivos[-1])


def processos(arquivo=ultimo_arquivo):
    tree = ET.parse(arquivo)
    root = tree.getroot()

    for processo in root.iter('processo'):
        print('Processo:   ', processo.attrib)
        # print(processo.attrib['numero'])

        for requerente in processo.iter('requerente'):
            print('Requerente: ', requerente.attrib['nome-razao-social'])

        for procurador in processo.iter('procurador'):
            print('Procurador: ', procurador.text)

        print('=' * 79)

if __name__ == '__main__':
    protocolos = processos()
