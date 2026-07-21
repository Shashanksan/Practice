import numpy as np

np.random.seed(42)
marks = np.random.randint(50, 100, (5, 5))
avg_marks = np.mean(marks, axis=1)
subject_avg = np.mean(marks, axis=0)
class_avg = np.mean(avg_marks)
above_class_avg = avg_marks > class_avg
std_dev = np.std(marks, axis=1)
consistent = std_dev < 12
top_student = np.argmax(avg_marks)
lowest_student = np.argmin(avg_marks)
normalized_marks = (marks - marks.min()) / (marks.max() - marks.min())
performance_score = avg_marks / std_dev
performance_rank = np.argsort(performance_score)[::-1]
print("Student Marks:\n", marks)
print("\nAverage Marks:", avg_marks)
print("Subject Average:", subject_avg)
print("Students Above Class Average:", above_class_avg)
print("Consistent Students:", consistent)

print("\nTop Student Index:", top_student)
print("Lowest Scorer Index:", lowest_student)

print("\nNormalized Marks:\n", normalized_marks)

print("\nPerformance Score:", performance_score)
print("Performance Rank:", performance_rank)