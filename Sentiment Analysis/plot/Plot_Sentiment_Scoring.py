import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

data = pd.read_csv('Sentiment_Analysis_RussianPropaganda.csv', sep=',', header=0,  names=["index", "idx", "text", "blob_polarity",
                                                            "blob_subjectivity", "vader_score", "vader_sentiment"])
df_polarity = pd.DataFrame(data, columns=["blob_polarity"])
df_subject = pd.DataFrame(data, columns=["blob_subjectivity"])
df_score = pd.DataFrame(data, columns=["vader_score"])

df_polarity = df_polarity.sort_values(by=['blob_polarity'], ascending=True)
df_subject = df_subject.sort_values(by=['blob_subjectivity'], ascending=True)
df_score = df_score.sort_values(by=['vader_score'], ascending=True)
print(df_polarity)
print(df_subject)
print(df_score)

count_polarity = [0 for i in range(11)]
for i in df_score["vader_score"]:
    if -15 <= i < -10:
        count_polarity[1] = count_polarity[1] + 1
    elif -10 <= i < -5:
        count_polarity[2] = count_polarity[2] + 1
    elif -5 <= i < 0:
        count_polarity[3] = count_polarity[3] + 1
    elif 0 <= i < 5:
        count_polarity[4] = count_polarity[4] + 1
    elif 5 <= i < 10:
        count_polarity[5] = count_polarity[5] + 1
    elif 10 <= i < 15:
        count_polarity[6] = count_polarity[6] + 1
    elif 15 <= i < 20:
        count_polarity[7] = count_polarity[7] + 1
    elif 20 <= i < 25:
        count_polarity[8] = count_polarity[8] + 1
    elif 25 <= i < 30:
        count_polarity[9] = count_polarity[9] + 1
    elif 30 <= i <= 35:
        count_polarity[10] = count_polarity[10] + 1


sum_polarity = sum(count_polarity)
x_polarity = [-15 + i * 5 for i in range(11)]
y_polarity = [i/sum_polarity for i in count_polarity]
x_new = np.linspace(min(x_polarity), max(x_polarity), 100)
# y_new = np.linspace(min(y_polarity), max(y_polarity), 100)
x_smooth = np.linspace(min(x_new), max(x_new), 300)
power_smooth = make_interp_spline(x_polarity, y_polarity)(x_smooth)
ground_sub = 0 - min(power_smooth)
power_smooth_limited = [i + ground_sub for i in power_smooth]

x_bar = [-15 + i * 5 for i in range(11)]
y_bar = [1 for i in range(11)]

# BARkgrounds
for i in range(11):
    plt.bar(x=x_bar[i], height=y_bar[i], color=(1.0 - i*0.09, i*0.1, i*0.05), alpha=0.8, width=5)

plt.bar(x=-15, height=1.0, color=(0.6, 0, 0), alpha=1.0, width=0.2)
plt.bar(x=35, height=1.0, color=(0, 0.6, 0), alpha=1.0, width=0.2)

plt.plot(x_smooth, power_smooth_limited, '-', color=(0, 0, 1))  # Smoothed Line
# plt.plot(x_polarity, y_polarity, '-', color=(1, 0.9, 0))      # Original Line

for a in x_bar:
    plt.text(a, 1.0, "%d" % (-15) if a <= -15 else "%d~%d" % (a, a+5) if a < 35 else "%d" % 35,
             ha='center', va='bottom', fontsize=6, color=(0, 0, 1))


plt.xticks(x_bar, fontsize=8)
plt.title("News Sentiment Score")
plt.show()
