import random
name=input("enter name:")
date= input("enter DOB(dd-mm-yyyy):")
charac=input("enter a special character:")

def pw_gen_name(name):  #chooses 5 letters randomly in given name
    name="".join(random.sample(name,5))
    return name
 
def unit_digit(date):    #sums up last digit of date,month,year respectively to get unit digit
    date_digit= int(date[1]+date[4]+date[-1])
  # it again adds up result if sum is greater than 10
    while date_digit>=10:
        date_digit=sum(map(int,str(date_digit)))   #Convert date_digit to a string to extract individual digits, convert them to integers(list forms), and sum them 
    return date_digit
  
def gen_password(name,charac,date):  #generates password
    gen_name=pw_gen_name(name)
    gen_date=unit_digit(date)
    password=gen_name+charac+str(gen_date)  #date is converted to string to add
    return password

password=gen_password(name,charac,date)
print("random password: ",password)
