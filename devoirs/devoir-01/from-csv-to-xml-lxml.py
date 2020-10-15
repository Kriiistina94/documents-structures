from lxml import etree
import csv
from lxml.builder import E

def TYPE(*args):
    return {"type":' '.join(args)}

def STATUT(*args):
    return {"statut":' '.join(args)}

with open('sanisettesparis.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    xmlFile = 'toilettes-paris-librairieLXML.xml'
    xmlData = open(xmlFile, 'w')
    xmlData.write('<?xml version="1.0"?>' + "\n")
    xmlData.write('<!DOCTYPE toilettes SYSTEM "wc.dtd">' + "\n")
    xmlData.write('<toilettes>' + "\n")
    for row in spamreader:
        xml = page = (
                E.toilette( TYPE(row[0]),STATUT(row[1]),
                    E.adresse(
                        E.libelle(row[2]),
                        E.arrondissement(row[3])
                    ),
                    E.horaire(row[4]),
                    E.services(
                        E.acces_pmr(row[5]),
                        E.relais_bebe(row[6])
                    ),
                    E.equipement(row[7])
                    )
                )
        xmlData.write(str(etree.tostringlist(page,  pretty_print=False)))
    xmlData.write('</toilettes>' + "\n")
    xmlData.close()     
    
