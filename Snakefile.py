import re
targets =[
    'win', 
    'zeus.exe',
    'search'
    ]
with open(r'myfile.txt', 'r') as file:
    # read all content from a file using the "read" function
    content = file.read()
    #print(content)

   # check if keywords exist
   # x = re.findall ("GNS3")
    # x = bool(re.search(r'^WindowsNT', targets[0]))
    # if x:
    #         print(f"yes, {targets[0]} exists!")


    # print the keyword or phrase found
    x = re.findall(r'^Win', targets[0])
    for x in targets[0]:
        print(x)

    y = re.findall(r'+zeus.exe', targets[2])
    for y in targets[2]:
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
