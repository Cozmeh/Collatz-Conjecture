# this takes the max value of given number(N) and then the max value(taken from previous run) is fed back 
# into the algorithm as (N) and so on ..


count = 0
def maxAsN(MaxNum):
    steps = 0
    seq = []
    global count
    while MaxNum > 1 :
        steps += 1
        if MaxNum % 2 == 0:
                MaxNum = MaxNum / 2
        else:
            MaxNum = 3 * MaxNum + 1
        print(steps, " | ",MaxNum)
        seq.append(int(MaxNum))
    else:
        if len(seq) < 1:
            print("The End")
            print("The total steps of recursive max : ", count)
        else: 
            count += 1
            print("The next number : ", max(seq))
            maxAsN(max(seq))


while True:   
    num = int(input("\nEnter a number : "))
    maxAsN(num)