ages = {
  "Matheus": 25,
  "Bob": 21,
  "João Miguel": 9
}

print("People and their ages:")
for n, a in ages.items():
  print(n, ":", a)
  
ages["Diana"] = 28
ages["João Miguel"] = 10

print("Updated dictionary:", ages)