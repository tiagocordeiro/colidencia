import xml.etree.ElementTree as ET
tree = ET.parse('2454.xml')
root = tree.getroot()


for processo in root.iter('processo'):
    print('Processo:   ', processo.attrib)
    # print(processo.attrib['numero'])

    # for requerente in processo.iter('requerente'):
    #     print('Requerente: ', requerente.attrib['nome-razao-social'])

    for procurador in processo.iter('procurador'):
        print('Procurador: ', procurador.text)

    print('=' * 79)

