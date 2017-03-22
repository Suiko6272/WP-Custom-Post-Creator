from wpitem import WPItemCreator
from slugify import slugify
#http://stackoverflow.com/questions/5574042/string-slugification-in-python
#pip install python-slugify

creator = WPItemCreator()


#creator.xyz();

###PESUDO:
    # Grab JSON
    # Create permalink variable
    # Place variables into XML Template
    # Loop Item Creation and Save XML items



#Grab JSON

def LoadJSON():
    import json
    with open('bec_webscrape.json') as json_file:
        data = json.load(json_file)
        count = 0;
        test = False
        if test:
            for d in data:
                count += 1
                print('Item #', count)
                print('=============')
                print('Title: ' + d["project"])
                print('Url: ' + d['url'])
                print('Category: ' + d['category'])
                print('Address: ' + d['address'])
                print('Size: ' + d['size'])
                print('Cost: ' + d['cost'])
                print('Description: ' + d['description'])
                print('Owner: ' + d['owner'])
                print('Architect: ' + d['architect'])
                print('Architect Website: ' + d['architectWebsite'])
                print('')
            #end ForLoop
        #end IF test
        return data
#END LoadJSON



myData = LoadJSON()

#creator.CreateItem(myData[0])

for item in myData:
    project = item['project']
    item['slug'] = slugify(project) #convert project into slug
    print("Project: " + item['project'])
    print("Slug: " + item['slug'])
#     for val in item:
#         print(item[val])

    # name = ???  # figure out the name of the drug
    # number = ???  # figure out the number you want to append
    # drug_dictionary[name].append(number)

#import json
#print(json.dumps(myData))
###value test
# for item in myData:
#     for val in item:
#         print(item[val])
#     print('=====')
#     print('')


        # d["project"]
        # d['url']
        # d['category']
        # d['address']
        # d['size']
        # d['cost']
        # d['description']
        # d['owner']
        # d['architect']
        # d['architectWebsite']
#
# xmlTemplate = """<root>
#     <person>
#         <name>%(name)s</name>
#         <address>%(address)s</address>
#      </person>
# </root>"""
# data = {'name':'anurag', 'address':'Pune, india'}
# print(xmlTemplate%data)