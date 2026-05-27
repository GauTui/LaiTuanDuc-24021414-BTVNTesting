def decision(age,income,creditScore,employment):

  #invalid input
  if not (18<= game <=65):
    return "Invalid Input"
  if not (5.0 <= income<= 500.0):
    return "Invalid Input"
  if not  (300<= creditScore <= 850):
    return "Invalid Input"
  if employment not in ['C','F']:
    return "Invalid Input"

  #risk
  if 300<= creditScore <= 500:
    risk = high
  elif 501 <= creditScore <= 700:
    risk = medium
  else :
    risk = "low"

  if risk = "high":
  return "Reject"
  if income < 15:
    if employment == 'C' and risk == "low":
      return "Manual Review"
    else:
      return "Reject"

  if employment == 'C':
    return "Approve"
  else:
    return "Manual Review"

Test_case = [
  (17,20.0,750,'C',"Invalid Input"),
  (66,20.0,750,'C',"Invalid Input"),
  (30,4.9,750,'C',"Invalid Input"),
  (30,500.1,750,'C',"Invalid Input"),
  (30,20.0,299,'C',"Invalid Input"),
  (30,20.0,851,'C',"Invalid Input"),
  (30,20.0,750,'X',"Invalid Input"),
  
  (18,5.0,300,'C',"Reject"),
  (65,500.0,850,'C',"Approve"),
  
  (30,20.0,450,'C',"Reject"),
  (30,10.0,650,'F',"Reject"),
  (30,10.0,750,'C',"Manual Review"),
  (30,20.0,650,'C',"Approve"),
  (30,20.0,750,'F',"Manual Review"),
  
  (30,14.9,750,'C',"Manual Review"),
  (30,15.0,750,'C',"Approve"),
  (30,15.1,750,'C',"Approve"),
  
  (30,20.0,500,'C',"Reject"),
  (30,20.0,501,'C',"Approve"),
  (30,20.0,700,'C',"Approve"),
  (30,20.0,701,'C',"Approve"),
]

passed = 0


for i, tc in enumerate(Test_case, start =1):
  age,income,score,employment,expected = tc

  result = decision(age, income,score,employment)
  if result == expected: 
    print(f"TC{i} : Pass")
    passed +=1
  else:
    print(f"TC{i} Failed | expected = {expected}, got = {result}")
print(f"\nPassed {pased}/{len(Test_case)} test case")

  
