x=input("Enter student's name: ")
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
if x==("Ahmad") :
  s1.remove("Ahmad")
  y=sum(s1)
  print (x ,y)
elif x=="Sami":
  s2.remove("Sami")
  z=sum(s2)
  print(x,z)
elif x=="Faris":
  s3.remove("Faris")
  v=sum(s3)
  print(x,v)
else:
  print("Student is not recorded 0")
