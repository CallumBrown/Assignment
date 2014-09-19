#Callum Brown
#19-09-14
#Money counter

amount = int(input("please enter an amount of money: "))
twenty = amount // 20
remainder = amount % 20
ten = remainder //10
remainder2= remainder % 10
five = remainder2 //5
remainder3 = remainder2 % 5
two = remainder3 // 2
remainder4 = remainder3 % 2
one = remainder4 // 1
remainder5 = remainder4 % 1

print("""The answer is :
      {0} twenty pound note(s),
      {1} ten pound note(s),
      {2} five pound note(s),
      {3} two pound coin(s),
      {4} pound coin(s).""".format(twenty,ten,five,two,one))



