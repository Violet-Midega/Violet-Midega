username=str(input("enter username:"))
pwd=int(input("enter password:"))
login = ["BSCIT-05-0247/2020",123]
if username in login and pwd in login:
  print("log in succefull")
else:
  print("log is not successfull")