# Collatz Conjecture
This is a Python module that provides various functions related to the Collatz Conjecture.

## Index
- [Observations](https://github.com/Cozmeh/Collatz-Conjecture/edit/main/README.md#observations)
- [Installation](https://github.com/Cozmeh/Collatz-Conjecture/edit/main/README.md#installation)
- [How to use the module?](https://github.com/Cozmeh/Collatz-Conjecture/edit/main/README.md#how-to-use-the-module-) 
- [Example usage and graphs](https://github.com/Cozmeh/Collatz-Conjecture/edit/main/README.md#example-usage-and-graphs)
- [Note](https://github.com/Cozmeh/Collatz-Conjecture/edit/main/README.md#note)

## What is the Collatz Conjecture?
The Collatz Conjecture, also known as the **`3n + 1 problem or the Hailstone sequence`**, is a famous mathematical problem that has fascinated mathematicians for decades. It is a simple problem to state, but despite numerous efforts, it remains unsolved to this day.
The conjecture states that for any positive integer n, the following sequence will always eventually reach 1:

- If n is even, divide it by 2.
- If n is odd, multiply it by 3 and add 1.

```
For example, let's start with n = 6:

6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```
> As you can see, the sequence eventually reaches 1. The conjecture suggests that this is true for all starting values of n.

### Observations
The sequence can be quite long before reaching 1. Additionally, there are some starting values that produce very long sequences before eventually reaching 1. For example, the starting value of 27 produces a sequence of 111 steps before eventually reaching 1.
```
less than 10 is 9, which has 19 steps,
less than 100 is 97, which has 118 steps,
less than 1,000 is 871, which has 178 steps,
less than 10,000 is 6171, which has 261 steps,
less than 100,000 is 77031, which has 350 steps,
less than 1 million is 837799, which has 524 steps,
less than 10 million is 8400511, which has 685 steps,
less than 100 million is 63728127, which has 949 steps,
less than 1 billion is 670617279, which has 986 steps,
less than 10 billion is 9780657631, which has 1132 steps,
and
less than 100 billion is 75128138247, which has 1228 steps.
```
## Installation
To use this module, simply copy and paste the `"collatz.py"` file into the `"site-packages"` directory of your Python installation. On Windows, this directory is usually located at `"C:\PythonXX\Lib\site-packages"` (replace "XX" with your Python version). or use it in the same directory

## How to use the module ?
To use the module, simply import it by typing `import collatz`. 

The following functions are available:
- `Sequence(num)` : Prints the sequence for the given num.
- `SequenceList(num)` : Returns a list containing the sequence for the given num.
- `StopTime(num)`: Returns the number of steps taken for an integer num to reach 1.
- `Max(num)` : Returns the maximum value in the sequence for the given num.
- `EvenSteps(num)` : Returns the number of even steps taken for an integer num to reach 1.
- `OddSteps(num)` : Returns the number of odd steps taken for an integer num to reach 1.
- `EvenStepsPercent(num)` : Returns the percentage of even steps taken for an integer num to reach 1.
- `OddStepsPercent(num)` : Returns the percentage of odd steps taken for an integer num to reach 1.
- `Stoptime_ValueG(num)` : Displays a graph of the sequence values against the number of steps taken for an integer num to reach 1.
- `Stoptime_ValueRG(Start,End)` : Displays a graph of the sequence values against the number of steps taken for integers from Start to End to reach 1.
- `Startvalue_StoptimeRG(Start,End)` : Displays a graph of the starting values against the number of steps taken to reach 1 for integers from Start to End.
- `Startvalue_MaxRG(Start,End,YaxisLimit,color)` : Displays a graph of the starting values against the maximum values in the sequences for integers from Start to End. 
   - `YaxisLimit` and `color` are optional parameters.

## Example usage and graphs
```py
import collatz as collatz 

# Print the sequence for the number 6
collatz.Sequence(6)

# Calculate the stopping time for the number 27
print(collatz.StopTime(27))

# Displays a graph of the sequence values against the number of steps taken for an integer num to reach 1.
collatz.Stoptime_ValueG(27)

# Display a graph of the sequence values against the number of steps taken for the numbers from 1 to 10
collatz.Stoptime_ValueRG(2, 10)

# Displays a graph of the starting values against the number of steps taken to reach 1 for integers from Start to End.
collatz.Startvalue_StoptimeRG(5,1000)

# Display a graph of the starting values against the maximum values in the sequences for the numbers from 1 to 100, with the y-axis limit set to 1000 and color to blue
collatz.Startvalue_MaxRG(2, 1000, 1000, "blue")
```
![1st](https://user-images.githubusercontent.com/117145297/227715223-79c196c0-e9ba-41eb-b894-abb69d2d6226.png)
![2nd](https://user-images.githubusercontent.com/117145297/227715227-54a21c04-df58-4be8-82b3-1aa36f4e1248.png)
![3rd](https://user-images.githubusercontent.com/117145297/227715229-55b748ce-9444-41f7-95d1-33799ac4e314.png)
![4th](https://user-images.githubusercontent.com/117145297/227715230-be4cf339-4d7d-4a6e-9b0b-696d085e9dea.png)

> You can even create `Custom` graphs by using the matplotlib.pyplot
```py
import collatz as collatz 
# X and Y values as a list 
Xval = [1,5,12,66]
Yval = [12,53,65,7]
# Using pyplot function inside of collatz module 
collatz.plot.xlabel('X-axis')
collatz.plot.ylabel('Y-axis')
collatz.plot.plot(Xval,Yval, color='black',linewidth='1',marker='.')
collatz.plot.show()
```
![custom](https://user-images.githubusercontent.com/117145297/227715711-1ddcae79-3d41-46b3-9265-125e2403f375.png)

### Note 
- Incase of any problem, Please create an `Issue`
- Feel free to `Contribute` if you are interested!
