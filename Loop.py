
# i = 1
# while i <= 5:
#   print(i)
#   i += 1
#   if i > 5 :
#     print("finish")

# cars 
password = "ali issa"
word= ""
count= 0
limit= 3
out = False
while word != password and not(out):
    if count < limit:
        word=input("Enter password :")
        count += 1

    else:
        out = True
if out:
    print("out of try")
else:
    print("correct!")