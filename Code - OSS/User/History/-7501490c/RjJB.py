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
test_list = ['a', 'b', 'c', 'd']
  
# printing list
print("The original list : " + str(test_list))
  
# initializing append_str
append_str = 'gfg'
  
# Append suffix / prefix to strings in list
pre_res = [append_str + sub for sub in test_list]
suf_res = [sub + append_str for sub in test_list]
  
# Printing result
print("list after prefix addition : " + str(pre_res))
print("list after suffix addition : " + str(suf_res))