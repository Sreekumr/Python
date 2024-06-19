
import json

x = '{ "name": "sreekumar", "age": "22"}'

y = json.loads(x)

print(type(y))

z =json.dumps(y)

print(type(z))

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)