st1=input("enter the string=")
st2=input("enter the string2=")
str1=st1.lower()
str2=st2.lower()
sorted_str1=sorted(str1)
sorted_str2=sorted(str2)
if(sorted_str1==sorted_str2):
	print("ENTERED STRINGS ARE ANAGRAMS")
else:
	print("ENTERED STRINGS ARE NOT ANAGRAMS") 


