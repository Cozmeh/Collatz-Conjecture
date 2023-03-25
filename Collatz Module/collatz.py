import matplotlib.pyplot as plot
import random
from sys import exit

#Exceptions
class InvalidNumberException(Exception):
    "Raised when a number <= 1 Or the number is Negative"
    pass

# Main function
def Main(num):
    global seq
    global StoppingTime
    global StepsList
    global even
    global odd
    global evp
    global odp

    seq = []
    StoppingTime = 0
    StepsList = []
    even = 0
    odd = 0
    evp = 0
    odp = 0


    try:
        if num < 1:
            raise InvalidNumberException
        else:
            while num > 1:
                StoppingTime += 1
                seq.append(num)
                if num % 2 == 0:
                    num = num / 2
                    even += 1
                else:
                    num = 3 * num + 1
                    odd += 1
                StepsList.append(StoppingTime)
            evp = even/StoppingTime*100
            odp = odd/StoppingTime*100

    except InvalidNumberException:
        print("Exception Occured : Invalid Number")

# Sequence function
def Sequence(num):
    try:
        if num < 1:
            raise InvalidNumberException
        else:
            print("sequence of", num)
            Step = 0
            while num > 1:
                Step += 1
                if num % 2 == 0:
                    num = num / 2
                else:
                    num = 3 * num + 1
                print(Step ," | ", int(num))
    except InvalidNumberException:
        print("Exception Occured : Invalid Number")

#Custom Exception
def ErrorCheck(num):
    try:
        if num <= 1:
            raise InvalidNumberException
        else:
            Main(num)
    except InvalidNumberException:
        print("Exception Occured : Invalid Number ")
        exit(0)
        

# Sequence list function
def SequenceList(num):
    ErrorCheck(num)
    return seq

# Steps function
def StopTime(num):
    ErrorCheck(num)
    return StoppingTime

# Max function
def Max(num):
    ErrorCheck(num)
    return max(seq)

# Even steps function
def EvenSteps(num):
    ErrorCheck(num)
    return even

# Odd steps function
def OddSteps(num):
    ErrorCheck(num)
    return odd

# Even steps % function
def EvenStepsPercent(num):
    ErrorCheck(num)
    return evp

# Odd steps % function
def OddStepsPercent(num):
    ErrorCheck(num)
    return odp

# Graph function
def Stoptime_ValueG(num):
    ErrorCheck(num)
    plot.xlabel('Stoptime')
    plot.ylabel('Sequence value')
    plot.title('Stoptime VS Sequence value')
    plot.plot(StepsList, seq, color="Black", linewidth='1',)
    plot.grid()
    plot.show()


def Stoptime_ValueRG(Start,End):
    if Start >= End:
        print("Exception Occured : Invalid Number")
    else:
        plot.xlabel('Stoptime(s)')
        plot.ylabel('Sequence value(s)')
        plot.title('Stoptime(s) VS Sequence value(s)')
        while Start <= End:
            ErrorCheck(Start)
            color = ["black","red","blue","green","purple"]
            plot.plot(StepsList, seq, color=random.choice(color), linewidth='1',)
            Start += 1
        plot.grid()
        plot.show()

def Startvalue_StoptimeRG(Start,End):
    if Start >= End :
        print("first value should be less than end value")
    else:
        plot.xlabel('Startvalue(s)')
        plot.ylabel('StopTime(s)')
        plot.title('Startvalue(s) VS Stoptime(s)')
        NumList = []
        StoptimeList = []
        for i in range(Start,End):
            ErrorCheck(i)
            NumList.append(i)
            StoptimeList.append(StoppingTime)   
        color = ["black","red","blue","green","purple"]
        plot.plot(NumList, StoptimeList, color=random.choice(color), linewidth='0',marker='.')
        plot.grid()
        plot.show()
        


def Startvalue_MaxRG(Start,End,YaxisLimit = 0,color = None):
    if(YaxisLimit == 0):
        YaxisLimit = End
    if Start >= End :
        print("first value should be less than end value")
    else:
        plot.xlabel('Startvalue(s)')
        plot.ylabel('Max of Starvalue(s)')
        plot.title('Startvalue VS Maximums')
        NumList = []
        MaxList = []
        for i in range(Start,End):
            ErrorCheck(i)
            NumList.append(i)
            MaxList.append(max(seq))   
        if(color == None):
            col = ["black","red","blue","green","purple"]
            plot.plot(NumList, MaxList, color=random.choice(col), linewidth='0',marker='.')
        else:
            plot.plot(NumList, MaxList, color=color, linewidth='0',marker='.')
        plot.ylim(0,YaxisLimit)
        plot.grid()
        plot.show()



