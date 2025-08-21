#!/usr/bin/env python3
"""Module for accessing Finna.fi REST API"""

# Activate virtual environment: source finna_venv/bin/activate     
# (To deactivate venv: conda deactivate) (if that doesn't work try: deactivate or source deactivate)
# Select interpreter (View -> Command Palette -> Python interpreter): Python 3.12.3('finna:venv':venv)
# Usage: python3 finna.py

from finna_client import FinnaClient
import requests
import json

# Default API base URL
API_BASE = 'https://api.finna.fi/api/v1/'

# Creating a client
finna = FinnaClient()
print("Now we have a FinnaClient object:", finna)

# Testing search
#print("* Performing a general search")
#result = finna.search('bicycle', limit=2)
#print("Search would have matched {} records".format(result['resultCount']))
#for rec in result['records']:
#    print(rec)

print("* Performing a general search")


print("Syötä ISBN: ")
isbn = input()

# Check that ISBN is not empty
if not isbn or isbn.strip() == "":
    print("Virhe: ISBN ei voi olla tyhjä!")
    exit()

# Finna search
finna_endpoint = 'https://api.finna.fi/api/v1/search?lookfor=' + isbn + '&type=AllFields&field[]=accessRestrictions&field[]=alternativeTitles&field[]=authors&field[]=awards&field[]=bibliographicLevel&field[]=bibliographyNotes&field[]=buildings&field[]=callNumbers&field[]=childRecordCount&field[]=classifications&field[]=cleanDoi&field[]=cleanIsbn&field[]=cleanIssn&field[]=cleanOclcNumber&field[]=collections&field[]=containerEndPage&field[]=containerIssue&field[]=containerReference&field[]=containerStartPage&field[]=containerTitle&field[]=containerVolume&field[]=corporateAuthors&field[]=dedupIds&field[]=dissertationNote&field[]=edition&field[]=embeddedComponentParts&field[]=events&field[]=findingAids&field[]=formats&field[]=fullRecord&field[]=generalNotes&field[]=genres&field[]=geoCenter&field[]=geoLocations&field[]=hierarchicalPlaceNames&field[]=hierarchyParentId&field[]=hierarchyParentTitle&field[]=hierarchyTopId&field[]=hierarchyTopTitle&field[]=humanReadablePublicationDates&field[]=id&field[]=identifierString&field[]=imageRights&field[]=images&field[]=imagesExtended&field[]=inscriptions&field[]=institutions&field[]=isbns&field[]=isCollection&field[]=isDigitized&field[]=isPartOfArchiveSeries&field[]=issns&field[]=languages&field[]=lccn&field[]=manufacturer&field[]=measurements&field[]=newerTitles&field[]=nonPresenterAuthors&field[]=oclc&field[]=onlineUrls&field[]=openUrl&field[]=originalLanguages&field[]=otherLinks&field[]=physicalDescriptions&field[]=physicalLocations&field[]=placesOfPublication&field[]=playingTimes&field[]=presenters&field[]=previousTitles&field[]=primaryAuthors&field[]=productionCredits&field[]=projectedPublicationDate&field[]=publicationDates&field[]=publicationEndDate&field[]=publicationFrequency&field[]=publicationInfo&field[]=publishers&field[]=rating&field[]=rawData&field[]=recordLinks&field[]=recordPage&field[]=relationshipNotes&field[]=secondaryAuthors&field[]=sectors&field[]=series&field[]=sfxObjectId&field[]=shortTitle&field[]=source&field[]=subjectActors&field[]=subjectDetails&field[]=subjectPlaces&field[]=subjects&field[]=subjectsExtended&field[]=subTitle&field[]=summary&field[]=systemDetails&field[]=targetAudienceNotes&field[]=title&field[]=titleSection&field[]=titleStatement&field[]=toc&field[]=uniformTitles&field[]=unitId&field[]=urls&field[]=year&sort=relevance,id&limit1'
response = requests.get(finna_endpoint)
response_dict = response.json()
#response_dict = response.json()['records'][0] 
if response.status_code == 200:
    #print(response.json()['records'][0])
    print(json.dumps(response_dict, indent=4, sort_keys=True))
else: print(response.status_code)
