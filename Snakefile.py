import re
## importing REGEX library
targets =[
    'GNS3', 
    'team',
    'search',
    'issues'
    ]
with open(r'myfile.txt', 'r') as file:
    # read all content from a file using the "read" function
    content = file.read()
    # check if keywords exist
    for target in targets:
        if target in content: 
            print ('string exists' ' + ' (targets))
            
        else:
            print('string does not exist')
            
    #file.write(content)
