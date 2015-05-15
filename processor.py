# -*- coding: ISO-8859-1 -*-
import os
import xml.etree.cElementTree as ET
from  collections import OrderedDict

def rules(field,data):
	if field == 'Title' or field == 'AdditionalTitle':
		return ".  ".join(data)
	elif field == 'ArchiveLocation':
		return " -- ".join(data)
	elif field == 'PhysicalDescription':
		return " ; ".join(data)

def processRecord(record):
	for item in record.iteritems():
		if len(item[-1]) > 1:
			record[item[0]] = [rules(*item)]
			
def parseXML(tree):
	records = []
	fields = ["REFNO","Title","AdditionalTitle","PhysicalDescription","ArchiveLocation"]	
	idstring = "{http://www.inmagic.com/webpublisher/query}"
	for record in tree.iter(tag=idstring+"Record"):
		details = record.getchildren()
		dc = OrderedDict()
		for i in details:
			stag = i.tag.replace(idstring,'')
			if stag in fields:
				if i.text:
					if stag in dc.keys():
						dc[stag].append(i.text)
					else:
						dc[stag] = [i.text]
		records.append(dc)
	return records


path = 'data/'
files = os.listdir(path)

for f in files:
	tree = ET.ElementTree(file=os.path.join(path,f))
	data =	parseXML(tree)
	for r in data:
		processRecord(r)
