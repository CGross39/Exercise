import matplotlib.pyplot as plt

try:
    fhand = open("StudentExercise.csv")
except:
    print('File cannot be opened')
    exit()

next (fhand)
lst = []
for line in fhand:
    nums = line.split(',')
    x_hrs = nums[0]
    if x_hrs !='':
        lst.append(float(x_hrs))
    
avg = sum(lst)/len(lst)
print(avg)



# We can set the number of bins with the *bins* keyword argument. 

plt.hist(lst,bins=7)

plt.ylabel('Counts')
plt.title('Frequency of Hours') 

plt.show()
