import matplotlib.pyplot as plt

try:
    fhand = open("StudentExercise.csv")
except:
    print('File cannot be opened')
    exit()

next (fhand)
lst = []
for line in fhand:
    nums = line.split(',') #splits number by ','
    x_hrs = nums[0]  #gets the first number
    if x_hrs !='':   #makes sure it does not get empty
        lst.append(float(x_hrs))


# Function 1: avg
def average(lst):
    total = sum(lst)
    return total / len(lst)



# Function 2: Prop above avg
def prop_above(lst):
    avg = average(lst)
    count = 0

    for num in lst:
        if num > avg:
            count += 1

    return count / len(lst)
def median(lst):
    ls= lst.sort()
    x= len(lst)
    return lst[x // 2]
print(lst)
print("Average: {: .4f}".format(average(lst)))
print("Proportion above average: {0: .2%}".format(prop_above(lst)))
print("Median: {0: .2f}".format(median(lst)))

# We can set the number of bins with the *bins* keyword argument. 

plt.hist(lst,bins=7)

plt.ylabel('Counts')
plt.title('Frequency of Hours') 

plt.show()
