import csv

a = []
with open('./enjoySport.csv', 'r') as csvfile:
    for row in csv.reader(csvfile):
        a.append(row)

num_attribute = len(a[0]) - 1
print("Number of attributes : ", num_attribute)

print("Number of training instances : ", len(a))
print("Training set : ")
for row in a:
    print(row)

hypothesis = ['0']*num_attribute
print("\nThe initial hypothesis is : ", hypothesis)

for i in range(0, len(a)):
    if a[i][num_attribute] == 'yes':
        for j in range(0, num_attribute):
            if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
    print("Hypothesis for training instance {} : ".format(i+1), hypothesis)

print("The Maximally specific hypothesis for the training instance is : ", hypothesis)
