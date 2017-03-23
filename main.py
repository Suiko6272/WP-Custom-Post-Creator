from WPXML import WPXML
from slugify import slugify

def CorrectNotAvailable(data):
    count = 0
    for item in data:
        for key in item:
            if item[key] == 'NotAvailable':
                item[key] = ''
    return data

def CorrectCategories(data):
    for item in data:
        if item['category'] == 'churches':
            item['category'] = 'church-civic'
        elif item['category'] == 'medical':
            item['category'] = 'medical-dental'
        elif item['category'] == 'multifamily':
            item['category'] = 'multifamily-hospitality'
        elif item['category'] == 'office':
            item['category'] = 'office-retail'
        #TODO: categories
    return data

def AddSlugToData(data):
    for item in data:
        item['slug'] = slugify(item['project'])
        item['category-slug'] = slugify(item['category'])
    return data

def LoadJSON(file):
    import json
    with open(file) as json_file:
        data = json.load(json_file)
        return data

def BEC_Fixes():
    data = LoadJSON('bec_webscrape.json')
    data = CorrectCategories(data)
    data = AddSlugToData(data)
    data = CorrectNotAvailable(data)
    return data

#TODO: Handle cases of same title / permalinks during load before wordpress import.
myData = BEC_Fixes()
creator = WPXML()
creator.CreateXML_BEC(myData)





###Get old permalink for 301 redirect
def Permalink_301CSV(data):
    for item in data:
        oldUrl = item['url'] #grab old url
        oldPermalink = oldUrl #Strip starting url into permalink
        newPermalink = '/' + item['slug'] #create new url
        #TODO: #store both into 301CSV
        #Note: newPermaLink may require categories slug as well so .com/project/category-slug/slug