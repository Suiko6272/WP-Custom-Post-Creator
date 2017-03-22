from wpitem import WPItemCreator

creator = WPItemCreator()


#creator.xyz();

# Grab JSON
# Grab XML
#Grab JSON Variables per unique Item
#Grab XML Fields Location
#Shove JSON Variables into XML Fields

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


#import json
myData = LoadJSON()
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


data = {'name':'test', 'address':'Pune, india'}
creator.CreateItem(data)
#print xmlTemplate%data