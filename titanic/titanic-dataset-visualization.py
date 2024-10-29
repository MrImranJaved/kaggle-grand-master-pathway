# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace 'train.csv' with the path to your file)
train_data = pd.read_csv('/kaggle/input/data-science-day1-titanic/DSB_Day1_Titanic_train.csv')

# Calculate survival rates by passenger class
survival_rates_by_class = train_data.groupby('Pclass')['Survived'].mean()

# Plot survival rates by passenger class
plt.figure(figsize=(8, 6))
survival_rates_by_class.plot(kind='bar', color='orange')
plt.title('Survival Rates by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.xticks(rotation=0)
plt.show()
