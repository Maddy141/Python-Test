# Kaun Banega Carorpati
qst=["Longest river","largest country","my fav colour","iron man of india","sharpest mamel"]
ans=["nile","russia","blue","sardar patel","human"]
for i in range(len(qst)):
    print(qst[i])
    user_ans=input("Enter your ans")
    if(user_ans==ans[i]):
        print("You won 100rs")
    else:
        print("Better luck next time")
 