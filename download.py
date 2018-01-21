from urllib.request import urlopen
from zipfile import ZipFile
from revistas import ultimaRevista


def baixaRevista(zipurl):
    """

    :param zipurl: 'http://revistas.inpi.gov.br/txt/RM####.zip'
    :return:

    Download the file from the URL
    Create a new file on the hard drive
    Write the contents of the downloaded file into the new file
    Close the newly-created file
    Re-open the newly-created file with ZipFile()
    Extract its contents into downloads/xml
    note that extractall will automatically create the path
    close the ZipFile instance
    """

    zipresp = urlopen(zipurl)

    tempzip = open("downloads/tmp/tempfile.zip", "wb")
    tempzip.write(zipresp.read())
    tempzip.close()

    zf = ZipFile("downloads/tmp/tempfile.zip")
    zf.extractall(path = 'downloads/xml')
    zf.close()
    return

if __name__ == '__main__':
    zipurl = ultimaRevista()
    baixaRevista(zipurl)
