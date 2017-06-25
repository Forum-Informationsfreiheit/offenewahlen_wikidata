#!/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

import pyApiToolkit as at
import json
import os
from wikidataintegrator import wdi_core, wdi_login
import include

__author__ = "Stefan Kasberger"
__copyright__ = "Copyright 2017"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Stefan Kasberger"
__email__ = "mail@stefankasberger.at"
__status__ = "Development" # 'Development', 'Production' or 'Prototype'

###    GLOBAL   ###

DELAY_TIME = 5 # in seconds
TS = at.get_timestring()
# TS = '2015-10-28-14-59'

###    FUNCTIONS   ###

def login(user, password):
	login_instance = wdi_login.WDLogin(user=user, pwd=password)
	return login_instance

def query_item(itemID):
	return wdi_core.WDItemEngine(wd_item_id=itemID)

def get_data(results):
	return results.get_wd_json_representation()

def write_item():
	# Search for and then edit/create new item
	wd_item = wdi_core.WDItemEngine(item_name='<your_item_name>', domain='genes', data=[entrez_gene_id])
	wd_item.write(login_instance)

def save_to_files(data, rootFolder):
	for item in data:
		at.save_to_json(data[item], rootFolder+'/data/raw/json/wikidata_'+item+'.json')

###    MAIN   ###

if __name__ == "__main__":
	startTime = at.start_timer()

	rootFolder = at.get_root_folder()
	config = include.data['wikidata']
	#data = {}

	# wikidata API
	login_instance = login(config['user'], config['password'])
	
	data = json.loads(at.read_file(rootFolder+'/data/raw/everypolitician-austria.json'))

	for politician in data['persons']:

		identifiers = politician['identifiers']
		for identifier in identifiers:
			if identifier['scheme'] == 'wikidata':
				wdID = identifier['identifier']

		vorname = wdi_core.WDString(value=politician['given_name'], prop_nr='P735') 
		
		ts = politician['birth_date'].split('-') 
		tsGebDatum = '+'+ts[0]+'-'+ts[1]+'-'+ts[2]+'T00:00:00Z'
		gebDatum = wdi_core.WDTime(time=tsGebDatum, prop_nr='P569')

		gender = politician['gender']
		if gender == 'male':
			genderID = 'Q6581097'
		elif gender == 'female':
			genderID = 'Q6581072'
		gender = wdi_core.WDItemID(value=genderID, prop_nr='P21')


		if 'contact_details' in politician:
			contactDetails = politician['contact_details']
			for contactDetail in contactDetails:
				if contactDetail['type'] == 'twitter':
					twitter = contactDetail['value']
		twitterHandle = wdi_core.WDString(value=twitter, prop_nr='2002') 

		tsAmtStart = '+2013-10-29T00:00:00Z'
		amt = wdi_core.WDItemID(value='Q17535155', prop_nr='P39', qualifiers=[wdi_core.WDTime(time=tsAmtStart, prop_nr='P580', is_qualifier=True)])
		
		data = [amt, twitterHandle, gebDatum, gender]
		wd_item = wdi_core.WDItemEngine(wd_item_id=wdID, data=data)
		wd_item.write(login_instance)

	at.stop_timer(startTime)
