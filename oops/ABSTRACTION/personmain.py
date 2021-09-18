from personal import PersonalBanking
po=PersonalBanking()
print("-"*40)
print("ACCOUNT DETAILS ")
print("-"*40)

#print("Accunt number is:{}".format(po.__acno))
print("Accunt holder name is:{}".format(po.cname))
print("balence is:{}".format(po.bal))
print("pin is:{}".format(po.pin))
print("city is:{}".format(po.city))
print("branch is:{}".format(po.branch))