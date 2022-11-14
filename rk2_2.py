"""counting IMT"""
with open('stdin.txt',"r+", encoding="utf-8") as inp,  open('stdout.txt', "r+", encoding="utf-8") as out:
    input_file = inp.read()
    output_file = out.read()
out = open('stdout.txt',"r+", encoding="utf-8")
weight_height = input_file.split('\n')
weight = int(weight_height[0])
height = int(weight_height[1])
imt = round(weight/(height**2), 5)
out.write(str(imt))
inp.close()
out.close()
