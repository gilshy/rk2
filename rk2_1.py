"""counting IMT"""
if __name__ == "__main__":
    weight = int(input('Type your weight: '))
    height = int(input('Type your height: '))
    imt = round(weight/(height**2), 5)
    print(imt)
