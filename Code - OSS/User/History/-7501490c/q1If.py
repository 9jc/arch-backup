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


text1 = input("Enter the text you want to format :")


# text1 = "--dark-pink --dark-pink2 --dark-purple --dark-blue --dark-cyan --dark-green --dark-lgreen  --dark-red --dark-yellow --dark-orange --dark-white --dark-brown  --grey-blue --grey-green --gruvbox  --dark  --cherry"


text = text1.split(" ")
# print(text)

# initializing append_str
append_str = '''
) "$SDIR"/styles.sh --dark-pink
) "$SDIR"/styles.sh --dark-pink2
) "$SDIR"/styles.sh --dark-purple
) "$SDIR"/styles.sh --dark-blue
) "$SDIR"/styles.sh --dark-cyan
) "$SDIR"/styles.sh --dark-green
) "$SDIR"/styles.sh --dark-lgreen
) "$SDIR"/styles.sh --dark-red
) "$SDIR"/styles.sh --dark-yellow
) "$SDIR"/styles.sh --dark-orange
) "$SDIR"/styles.sh --dark-white
) "$SDIR"/styles.sh --dark-brown
) "$SDIR"/styles.sh --grey-blue
) "$SDIR"/styles.sh --grey-green
) "$SDIR"/styles.sh --gruvbox
) "$SDIR"/styles.sh --dark
) "$SDIR"/styles.sh --cherry
'''
  
# Append suffix / prefix to strings in list
prefix_result = [append_str + sub for sub in text]
sufix_result = [sub + append_str for sub in text]
  
formated_text = '' + '\n'.join(prefix_result) + ''

# Printing result
# restults = (str(prefix_result)
# print(formated_text)

# file = (open('/home/i0xfce/MEGAsync/Projects/Python/Text Editor/output.txt', "w"))
# file.write(formated_text)
# file.close()

file = (open('/home/i0xfce/MEGAsync/Projects/Python/Text Editor/output.txt', "w"))
file
file.write(formated_text)
file.close()