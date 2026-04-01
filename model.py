import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import logisticregression
from sklearn.metrics import accuracy_score 

# load and prepare data
url = "https://raw.githubusercontent.com/dsrscientiest/dataset1/master/student-mat.csv"
df = pd.read_csv(url, sep=':')
X = df[['stuytime', 'absences', 'G1', 'G2']]
y = (df['G3'] > 10).astype(int)

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegressionn()
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predicions))
