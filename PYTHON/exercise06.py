import numpy as np

# Generate fixed random data
np.random.seed(42)

bp = np.random.randint(110, 150, (7, 5))
hr = np.random.randint(60, 110, (7, 5))
spo2 = np.random.randint(90, 100, (7, 5))

# Calculate averages
avg_bp = np.mean(bp, axis=0)
avg_hr = np.mean(hr, axis=0)
avg_spo2 = np.mean(spo2, axis=0)

# Calculate standard deviations
std_bp = np.std(bp, axis=0)
std_hr = np.std(hr, axis=0)

# Risk conditions
high_bp = avg_bp > 130
low_oxygen = avg_spo2 < 95
abnormal_hr = (avg_hr < 60) | (avg_hr > 100)
unstable_vitals = (std_bp > 10) | (std_hr > 15)

# Calculate risk score
risk_score = (
    high_bp.astype(int)
    + low_oxygen.astype(int)
    + abnormal_hr.astype(int)
    + unstable_vitals.astype(int)
)

# Classification
classification = []

for score in risk_score:
    if score <= 1:
        classification.append("Normal")
    elif score == 2:
        classification.append("Moderate Risk")
    else:
        classification.append("Critical")

# Find most critical patient
most_critical = np.argmax(risk_score)

# Output
print("Average BP:", avg_bp)
print("Average HR:", avg_hr)
print("Average SpO2:", avg_spo2)
print("Risk Score:", risk_score)
print("Classification:", classification)
print("Most Critical Patient Index:", most_critical)