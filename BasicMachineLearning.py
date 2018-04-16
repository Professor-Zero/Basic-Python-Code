#Using scikit library, Machine learning
#Source: http://scikit-learn.org/stable/tutorial/basic/tutorial.html
#Source: https://www.youtube.com/watch?v=cKxRvEZd3Mw

import sklearn
from sklearn import tree

#holds information of different vehicles about their features
#each box holds weight of vehicle, number of wheels, highest speed.
#       #pounds, #wheels, #speedlimit
features =  [[33000,12,60], [4000, 4, 100], [400, 2, 100]]
labels =    ["Truck",            "Car",     "Motorcycle"]

#a decision tree is used to help decide the computer
#with the data you given it already.
classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(features, labels)

#now the machine trys and predicts with the data I give it and determines what kind of vehicle it is.
print('If the vehicle weights 3500lb, has 4 wheels, and 80 mph.')
print('The computer predicts it\'s a',classifier.predict([[3500, 4, 80]]))

print()

print('If the vehicle weights 25000lb, has 10 wheels, and 70 mph.')
print('The computer predicts it\'s a',classifier.predict([[25000, 10, 70]]))