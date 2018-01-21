# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:06:00 2017

@author: Tiago
"""

import xml.etree.cElementTree as et
import pandas as pd


def getvalueofnode(node):
    """ return node text or None """
    return node.text if node is not None else None


def main():
    """ main """
    parsed_xml = et.parse("2454.xml")
    dfcols = ['processo', 'requerente', 'procurador']
    df_xml = pd.DataFrame(columns=dfcols)

    for node in parsed_xml.getroot():
        processo = node.attrib.get('processo')
        requerente = node.find('requerente')
        procurador = node.find('procurador')

        df_xml = df_xml.append(
            pd.Series([processo, getvalueofnode(requerente), getvalueofnode(procurador)], index=dfcols), ignore_index=True)

    print(df_xml)


main()