import numpy as np
import os 
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib

dataset_path = 'dataset_mp'
label_file = 'lavels_V3.txt'

files = []
for file in os.listdir(dataset_path):
    if file.endswith('.npy'):
        files.append(file)


x =[]
y =[]

labels = []

for index,file in enumerate(files):
    print(index,file)
    data  = np.load(os.path.join(dataset_path,file))
    x.extend(data)
    y.extend([index]*data.shape[0])
    label = file.split('.')[0]
    labels.append(label)
with open(label_file,'w') as file:
    for label in label:
        file.write(label+"\n")

scaler = StandardScaler()
x= scaler.fit_transform(x)


clf = SVC(kernel='liner',probability=True)
clf.fit(x,y)
model_filename = "svc_model_V3.pkl"
joblib.dump(clf,model_filename)
scaler_filename = "scaler_V3.pkl"
joblib.dump(scaler,scaler_filename)

print("model saved sucessfully")