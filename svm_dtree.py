import pickle
from sklearn import svm
from sklearn import tree
import warnings
warnings.filterwarnings("ignore")
with open("django_data","rb") as f:
    x=pickle.load(f)
with open("django_y","rb") as f:
    y=pickle.load(f)
train_x=x[:8000]+x[9000:]
train_y=y[:8000]+y[9000:]
test_x=x[8000:9000]
test_y=y[8000:9000]

classifier=svm.SVC(kernel='rbf')
dtree=tree.DecisionTreeClassifier(criterion='gini')

classifier.fit(train_x,train_y)
dtree.fit(train_x,train_y)

ans1=[]
ans2=[]

for i in test_x:
    ans1.append(classifier.predict(i)[0])
    ans2.append(dtree.predict(i)[0])

acc1=0
acc2=0

for i in range(len(test_y)):
    if(test_y[i]==ans1[i]):
        acc1+=1
    if(test_y[i]==ans2[i]):
        acc2+=1

print('SVM Accuracy:',acc1/len(test_y)*100)
print('Decision Tree Accuracy:',acc2/len(test_y)*100)
