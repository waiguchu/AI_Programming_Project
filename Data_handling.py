import pandas as pd
from sklearn.model_selectionimport train_test_split

# Load dataset
url = "https://raw.githubusercontent.com/dsrscientist/dataset1/master/student-mat.csv"
df = pd.read_csv(url, ssep=';')

# preview data
print(df.head())
print(df.shape)
# select features and target
x = df[['studytime','absences','G1','G2']]
y = df['G3']
 #split data
X_train, X_test, y_train, y_test = train_test__split(X, y, test_size=0.2, random_state=42)

                 
