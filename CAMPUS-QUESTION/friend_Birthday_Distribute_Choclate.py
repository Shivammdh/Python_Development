'''Mr.Shivam birthday in next month . This time he is planing to
invite N number of friend. he want to distribute chocolate all
of his friend and go to a shop.he is by packet of chocolates
 which packet has M nuber of chocolates. Your task wil be to help
 Mr. shivam to by equal number of chocolate  which can distribute all
 friend to equal number of chocolates.
  input: testcase: 2
  N=12 M=13
  N=12 M=12
  Output: NO
          YES
  '''
t=int(input())
for i in range(t):
    n=int(input())
    m=int(input())
    if (m % n == 0):
        print("Yes")
    else:
        print("No")
