import pandas as pd

mydataset = {
  'student': ["shivam sharma", "salman khan", "prathmesh","ayushi chandra"],
  'Roll No': ["0105CA193D53", "0105CA193D47", "0105CA193D43","0105CA193D14"]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
