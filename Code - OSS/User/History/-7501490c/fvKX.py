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

# text = ["--dark-pink","--dark-pink2","--dark-purple","--dark-blue","--dark-cyan","--dark-green","--dark-lgreen","--dark-red","--dark-yellow","--dark-orange","--dark-white","--dark-brown","--grey-blue","--grey-green","--gruvbox ","--dark","--cherry"]


# for i in range(1, 18):
#     print(f') "$SDIR"/styles.sh {text.}')

# Python3 code to demonstrate working of
# Append suffix / prefix to strings in list
# Using list comprehension + "+" operator
  
# initializing list
text = ["--dark-pink","--dark-pink2","--dark-purple","--dark-blue","--dark-cyan","--dark-green","--dark-lgreen","--dark-red","--dark-yellow","--dark-orange","--dark-white","--dark-brown","--grey-blue","--grey-green","--gruvbox ","--dark","--cherry"]
space = ("\n") 
# printing list
# print("The original list : " + str(text))
  
# initializing append_str
append_str = ') "$SDIR"/styles.sh '
  
# Append suffix / prefix to strings in list
pre_res = [space + append_str + sub for sub in text]
suf_res = [sub + append_str for sub in text]
  
# Printing result
restults = ("list after prefix addition : " + str(pre_res))


file = (open('output.txt', "w"))
file.write(restults)
file.write(space)
file.close()
# print("list after suffix addition : " + str(suf_res))