import statistics as stats
scores = [
    75, 72, 72, 61, 60, 80, 70, 95, 79, 79,
    65, 54, 57, 57, 63, 80, 37, 84, 93, 57,
    68, 70, 53, 63, 51, 62, 82, 75, 73, 74,
    69, 55, 79, 61, 66, 22, 59, 78, 85, 52,
    74, 66, 41, 83, 51, 55, 71, 65, 57, 54,
    90, 59, 74, 69, 69, 50, 91, 58, 62, 81,
    74, 75, 64, 60, 72, 82, 67, 68, 61, 65,
    82, 85, 77, 69, 65, 52, 88, 55, 54, 71,
    76, 79, 52, 64, 70, 74, 74, 73, 63, 59,
    100, 91, 74, 66, 99, 64, 71, 54, 71, 87
]

mean = stats.mean(scores)
median = stats.median(scores)
mode = stats.mode(scores)
std_dev = stats.stdev(scores)

high_outlier = mean + 2*std_dev
low_outlier = mean - 2*std_dev
h_outlier = []
l_outlier = []

for i in scores:
    if i >= high_outlier:
        h_outlier.append(i)
    elif i <= low_outlier:
        l_outlier.append(i)
    else:
        pass

print(f"Mean = {mean} \nMedian = {median} \nMode = {mode} \nStandard Deviation = {std_dev}")
print(f"Low outliers: {l_outlier}")
print(f"High outliers: {h_outlier}")