import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer

# loading the data
data_set = pd.read_csv("spambase.data")


# descretizing the data
dis = KBinsDiscretizer(n_bins=5, encode="ordinal", strategy="uniform")
data_set = dis.fit_transform(data_set)

print(data_set[100][57])

# splitibf the data for training(70%) and testing(30%)
from sklearn.model_selection import train_test_split
train_data, test_data = train_test_split(data_set, test_size = 0.30)


# applying algorithms 4.1 and 4.3 on training data

# initial hypothesis
list1 = []
for x in range(0, 57):
    list1.append([])
    list1[x].append(train_data[0][x])


for x in range(0, len(train_data)):
    for y in range(0, 57):
        if train_data[x][y] not in list1[y]:
            list1[y].append(train_data[x][y])

#obtained hypothesis
print(list1)

# testig the hypothesis on test set and measuring accuracy
n = 0
for x in range(0, len(test_data)):
    c = 0
    for y in range(0, 57):
        if test_data[x][y] in list1[y]:
            c = c + 1
    if c == 57 and test_data[x][57] != 4:
        n = n + 1

    if c != 57 and test_data[x][57] == 4:
        n = n + 1

print("Accuracy :"+str((n/len(test_data)*100)))


