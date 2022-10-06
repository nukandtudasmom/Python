targets =[
    'line 8', 
    'team',
    'search'
    ]
with open(r'myfile.txt', 'r') as file:
    # read all content from a file using the "read" function
    content = file.read()
    # check if keywords exist
    for target in targets:
        if target in content: 
            print ('string exists')
        else:
            print('string does not exist')
# the string we are searching for
# todo - print results of findings, adding additional search criteria to array, switch from strings to regex



# another try at searching for a string in a document.
# with open (r'myfile.txt', 'r') as fp:
# lines = fp.readlines()
# for row in lines:
# word = 'line 3'
 #   print(row.find(word))
  #  if row.find(word) == 0:
  #  print('string exists in file')
 #       print ('line number:', lines.index(line))
