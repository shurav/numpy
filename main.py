import numpy
heights = []
run = '1'
while(run =='1'):
    while True:
        try:
            height = float(input("Enter a height "))
            while(height<=0):
                height = float(input("Enter valid height "))
            heights.append(height)
            run = input("Wanna keep adding more heights? (Enter '1' if yes) ")
        except ValueError:
            print("invalid input")
        else:
            break;
heights = numpy.array(heights) # 5 6 7 [[[5], [6], [7] ], [[8], [9], [0]]]
for i in range(len(heights)):
    print(heights[i])
heightView = heights.copy()
heightView = heightView.reshape(2, 3, 1)
print(heightView)
