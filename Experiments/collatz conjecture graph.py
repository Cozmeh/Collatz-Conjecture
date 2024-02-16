import matplotlib.pyplot as plt

print("Try 63728127")
number = float(input('Any positive integer:'))
seq = []
count = 0
c_list = []
even = 0
odd = 0
if number < 1:
    print("Enter a positive integer")

else:
    while number > 1:
        count += 1
        seq.append(number)
        if number % 2 == 0:
            number = number / 2
            even += 1
        else:
            number = 3 * number + 1
            odd += 1

        print(number, ":", count)
        
        c_list.append(count)
        

    evp = even/count*100
    odp = odd/count*100

    print()
    print("Sequence   :", seq)
    print()
    print("Steps      :", count)
    print()
    print("Maximum    :", max(seq))
    print()
    print("Even steps :", even)
    print()
    print("odd steps  :", odd)
    print()
    print("Even and odd percentage resp :",
          round(evp), "%", "and", round(odp), "%")
    print()
    print("Even steps percentage:", evp, "%")
    print()
    print("Odd steps percentage :", odp, "%")

plt.xlabel('Number of steps')
plt.ylabel('Sequence values')
plt.plot(c_list, seq, color="green", linewidth='1',)
plt.title('Collatz conjecture')
plt.grid()
plt.show()
