def findJudge( n: int, trust: list[list[int]]) -> int:
  
  trustor = [0]*(n+1) # who trust
  trustee = [0]*(n+1) # who get trust
  for i in trust:
    trustor[i[0]] += 1
    trustee[i[1]] += 1
    print(trustee)
  town_judge = trustee.index(max(trustee))
  if n == 1 and not trust:
    print(1)
  elif (trustee[town_judge] == (n-1)) and not(trustor[town_judge]):
    print(town_judge)
  else :
    print(-1)

findJudge(3, [[1,2],[2,3]])

# submission link: https://leetcode.com/problems/find-the-town-judge/submissions/1999552393