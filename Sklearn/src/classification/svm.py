from sklearn import svm
X = [[0, 0], [1, 1]]
y = [1, 1]
clf = svm.SVC()
svc = clf.fit(X, y)  
print(svc)
result = clf.predict([[1, 1]])
print(result)
# get support vectors
print(clf.support_vectors_)
# get indices of support vectors
print(clf.support_)
# get number of support vectors for each class
print(clf.n_support_) 