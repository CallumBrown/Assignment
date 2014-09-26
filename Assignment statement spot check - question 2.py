#Callum Brown
#23-09-14
#Assignment statement spot check - question 2

weight = int(input("Please enter the weight in grams: "))
remainder=weight

hundered = weight//100
remainder = hundered%weight
fifty = remainder//50
remainder1 = fifty%weight
ten = remainder1//10
remainder2 = ten%weight
five = remainder2//5
remainder3 = five%weight
two = remainder3//2
remainder4 = two%weight
one = remainder4//1
remainder5 = one%weight

print("""You need {0} 100 gram weight(s),
     {1} 50 gram weight(s),
     {2} 10 gram weight(s),
     {3} 5 gram weight(s),
     {4} 2 gram weight(s)
     {5} 1 gram weight(s)""".format(hundered,fifty,ten,five,two,one))
