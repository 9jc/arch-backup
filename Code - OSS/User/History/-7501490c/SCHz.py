# text = """
# --dark-pink 
# --dark-pink2 
# --dark-purple 
# --dark-blue 
# --dark-cyan 
# --dark-green 
# --dark-lgreen  
# --dark-red 
# --dark-yellow 
# --dark-orange 
# --dark-white 
# --dark-brown  
# --grey-blue 
# --grey-green 
# --gruvbox  
# --dark  
# --cherry
# """
  
# initializing list
# text = ["--dark-pink","--dark-pink2","--dark-purple","--dark-blue","--dark-cyan","--dark-green","--dark-lgreen","--dark-red","--dark-yellow","--dark-orange","--dark-white","--dark-brown","--grey-blue","--grey-green","--gruvbox ","--dark","--cherry"]
text1 = "--dark-pink --dark-pink2 --dark-purple --dark-blue --dark-cyan --dark-green --dark-lgreen  --dark-red --dark-yellow --dark-orange --dark-white --dark-brown  --grey-blue --grey-green --gruvbox  --dark  --cherry"
text = text1.split(" ")
print(text)

# space = ("\n") 
# printing list
# print("The original list : " + str(text))
  
# initializing append_str
append_str = ') "$SDIR"/styles.sh '
  
# Append suffix / prefix to strings in list
pre_res = [append_str + sub for sub in text]
suf_res = [sub + append_str for sub in text]
  
restults1 = '' + '\n'.join(pre_res) + ''

# Printing result
restults = ("list after prefix addition : " + str(pre_res))
print(restults1)

file = (open('/home/i0xfce/MEGAsync/Projects/Python/Text Editor/output.txt', "w"))
file.write(restults1)
# file.write(space)
file.close()
# print("list after suffix addition : " + str(suf_res))