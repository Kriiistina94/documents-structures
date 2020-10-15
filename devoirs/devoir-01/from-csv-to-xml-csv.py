import csv
with open('sanisettesparis.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    xmlFile = 'toilettes-paris-librairieCSV.xml'
    xmlData = open(xmlFile, 'w')
    xmlData.write('<?xml version="1.0"?>' + "\n")
    xmlData.write('<!DOCTYPE toilettes SYSTEM "wc.dtd">' + "\n")
    xmlData.write('<toilettes>' + "\n")
    rowNum = 0
    for row in spamreader:

        xmlData.write('<toilette type="'+ row[0]+'"'+ ' '+'statut="'+ row[1]+ '"' +'>' + "\n")

        xmlData.write("\t"+'<adresse>' + "\n")
        xmlData.write("\t"+ "\t"+'<libelle>'+row[2]+'</libelle>' + "\n")
        xmlData.write("\t"+ "\t"+'<arrondissement>'+row[3]+'</arrondissement>' + "\n")
        xmlData.write("\t"+'</adresse>' + "\n")

        xmlData.write("\t"+'<horaire>'+row[4]+'</horaire>' + "\n")

        xmlData.write("\t"+'<services>' + "\n")
        xmlData.write("\t"+ "\t"+'<acces-pmr>'+row[5]+'</acces-pmr>' + "\n")
        xmlData.write("\t"+ "\t"+'<relais-bebe>'+row[6]+'</relais-bebe>' + "\n")
        xmlData.write("\t"+'</services>' + "\n")

        xmlData.write("\t"+'<equipement>'+row[7]+'</equipement>' + "\n")
        

        xmlData.write('</toilette>' + "\n")
        rowNum = rowNum+1

    xmlData.write('</toilettes>' + "\n")
    xmlData.close()