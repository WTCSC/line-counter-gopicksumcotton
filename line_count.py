def line_count():
  """
  Reference the "Reading Files in Python" lesson to open the `file.txt` file, count the number of words in the file, and return the count:
  """
  #open the file 
  file = open('file.txt', 'r')
  #read all lines into a list
  lines = file.readlines()
  x=0 
  #itterate over each line 
  for line in lines:
    x=x+1 
  #close the file
  file.close()
  return x



