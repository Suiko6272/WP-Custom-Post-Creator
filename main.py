from wpitem import WPItemCreator
from array import *
from slugify import slugify
#http://stackoverflow.com/questions/5574042/string-slugification-in-python
#pip install python-slugify

###PESUDO:
    # Grab JSON
    # Create slug variable
    # Place variables into XML Template
    # Loop Item Creation and Save XML items


###Grab JSON

def LoadJSON():
    import json
    with open('bec_webscrape.json') as json_file:
        data = json.load(json_file)
        return data
#END LoadJSON


###Create slug
def AddSlugToData(data):
    for item in data:
        item['slug'] = slugify(item['project'])
        item['category-slug'] = slugify(item['category'])
    return data

creator = WPItemCreator()

myData = LoadJSON() #Get Intial JSON Data
myData = AddSlugToData(myData) #Create Slug

masterXML = ""
for item in myData:
    xmlItem = creator.CreateItem(item) ###Place Variable into template
    masterXML += xmlItem ###Append to final XML

#print(masterXML)

xmlFile = open('output.txt', 'w')###Open text file to write XML to
#s = str(value)
xmlFile.write( masterXML )
xmlFile.close()

###Get old permalink for 301 redirect
def Permalink_301CSV(data):
    for item in data:
        oldUrl = item['url'] #grab old url
        oldPermalink = oldUrl #Strip starting url into permalink
        newPermalink = '/' + item['slug'] #create new url
        #TODO: #store both into 301CSV