from urllib.request import urlopen
from bs4 import BeautifulSoup


def ultimaRevista():
    """
    Retorna o link para última Revista da Propriedade Industrial
    SEÇÃO V MARCAS
    Arquivo em formato .xml (compactado .zip)
    Ex:
    >>> from revistas import *
    >>> ultimarevista = revista()
    >>> ultimarevista
    'http://revistas.inpi.gov.br/txt/RM2454.zip'
    """

    html = urlopen("http://revistas.inpi.gov.br/rpi/")
    bsObj = BeautifulSoup(html.read(), "html.parser")
    link = bsObj.find_all("tr")[1].find_all("td")[6].find_all("a")[1]['href']

    return link


if __name__ == '__main__':
    ultimarevista = ultimaRevista()
    print(ultimarevista)
