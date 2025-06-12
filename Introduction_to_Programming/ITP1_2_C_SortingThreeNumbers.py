a, b, c = map(int, input().split( ))
number = [a, b, c]
number.sort()
print(*number) #*number指解包，直接一个一个打印数据，print(number)会输出[1, 2, 3]