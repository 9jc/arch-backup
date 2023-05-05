# x_uiqwqw = "dark-pink dark-pink2 dark-purple dark-blue dark-cyan dark-green dark-lgreen dark-red dark-yellow dark-orange dark-white dark-brown grey-blue grey-green gruvbox dark-theme cherry"

totContent = ""
print("Enter the Name of File: ")
fileName = str(input())
fileHandle = open(fileName, "r")

for content in fileHandle:
    newContent = content.title()
    totContent = totContent + newContent

fileHandle.close()
fileHandle = open(fileName, "w")
fileHandle.write(totContent)

print("All Words Capitalized Successfully!")
fileHandle.close()

# https://codescracker.com/python/program/python-program-get-ip-address.htm