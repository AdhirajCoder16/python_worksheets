import numpy as np
names = ['Arin', 'Aditya', 'Chirag', 'Gurleen', 'Kunal']
scores = np.array([[85, 78, 92, 88], [79, 82, 74, 90], [90, 85, 89, 92], [66, 75, 80, 78], [70, 68, 75, 85]])
total_marks = np.sum(scores, axis=1)
avg_marks = np.mean(scores, axis=1)
subject_performance = np.mean(scores, axis=0)
top_performer = names[np.argmax(total_marks)]
bottom_performer = names[np.argmin(total_marks)]
passing_percent = np.sum(np.all(scores >= 35, axis=1)) / len(names) * 100
print(total_marks)
print(avg_marks)
print(subject_performance)
print(top_performer)
print(bottom_performer)
print(passing_percent)