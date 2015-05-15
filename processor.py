# -*- coding: ISO-8859-1 -*-
import os
import xml.etree.cElementTree as ET

def parseXML(tree):
	records = []
	fields = ["REFNO","Title","AdditionalTitle","PhysicalDescription","ArchiveLocation"]	
	idstring = "{http://www.inmagic.com/webpublisher/query}"
	for record in tree.iter(tag=idstring+"Record"):
		details = record.getchildren()
		dc = {}
		for i in details:
			stag = i.tag.replace(idstring,'')
			if stag in fields:
				dc[stag] = i.text
		records.append(dc)
	return records


tree = ET.ElementTree(file=source)

data =	parseXML(tree)

for record in data: