import re
targets =[
    'line 8', 
    'team',
    'search'
    ]
with open(r'myfile.txt', 'r') as file:
    # read all content from a file using the "read" function
    content = file.read()
    #print(content)

   # check if keywords exist
   # x = re.findall ("GNS3")
    # x = bool(re.search(r'^l', targets[0]))
    # if x:
    #         print(f"yes, {targets[0]} exists!")
    x = re.findall(r'^l', targets[])
    print(x)
    y = re.findall(r'$ch', targets[2])
    print(y)
            #print(f"yes, {targets[2]} exists!")

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
