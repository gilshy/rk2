"""counting IMT"""
weight = int(input('Type your weight: '))
height = int(input('Type your height: '))
imt = round(weight/(height**2), 5)
print(imt)