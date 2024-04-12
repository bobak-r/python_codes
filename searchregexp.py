import re
Result= re.search(r"aza","plaza")
print(Result)
resulut=re.search(r"aza","maze")
print(resulut)
print(re.search(r"^x","xenon"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))