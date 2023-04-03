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
    if -2.0 <= i < -1.6:
        count_polarity[1] = count_polarity[1] + 1
    elif -1.6 <= i < -1.2:
        count_polarity[2] = count_polarity[2] + 1
    elif -1.2 <= i < -0.8:
        count_polarity[3] = count_polarity[3] + 1
    elif -0.8 <= i < -0.4:
        count_polarity[4] = count_polarity[4] + 1
    elif -0.4 <= i < 0:
        count_polarity[5] = count_polarity[5] + 1
    elif 0 <= i < 0.4:
        count_polarity[6] = count_polarity[6] + 1
    elif 0.4 <= i < 0.8:
        count_polarity[7] = count_polarity[7] + 1
    elif 0.8 <= i < 1.2:
        count_polarity[8] = count_polarity[8] + 1
    elif 1.2 <= i < 1.6:
        count_polarity[9] = count_polarity[9] + 1
    elif 1.6 <= i <= 2.0:
        count_polarity[10] = count_polarity[10] + 1


sum_polarity = sum(count_polarity)
x_polarity = [-2.0 + i * 0.4 for i in range(11)]
y_polarity = [i/sum_polarity for i in count_polarity]
x_new = np.linspace(min(x_polarity), max(x_polarity), 100)
# y_new = np.linspace(min(y_polarity), max(y_polarity), 100)
x_smooth = np.linspace(min(x_new), max(x_new), 300)
power_smooth = make_interp_spline(x_polarity, y_polarity)(x_smooth)
ground_sub = 0 - min(power_smooth)
power_smooth_limited = [i + ground_sub for i in power_smooth]

x_bar = [-2.0 + i * 0.4 for i in range(11)]
y_bar = [1 for i in range(11)]

# BARkgrounds
for i in range(11):
    plt.bar(x=x_bar[i], height=y_bar[i], color=(1.0 - i*0.09, i*0.1, i*0.05), alpha=0.8, width=0.4)

plt.bar(x=-2.0, height=1.0, color=(0.6, 0, 0), alpha=1.0, width=0.05)
plt.bar(x=2, height=1.0, color=(0, 0.6, 0), alpha=1.0, width=0.05)

plt.plot(x_smooth, power_smooth_limited, '-', color=(0, 0, 1))  # Smoothed Line
# plt.plot(x_polarity, y_polarity, '-', color=(1, 0.9, 0))      # Original Line

for a in x_bar:
    plt.text(a, 1.0, "%.1f" % (-2.0) if a <= -2.0 else "%.1f~%.1f" % (a, a+0.4) if a < 2.0 else "%.1f" % 2.0,
             ha='center', va='bottom', fontsize=6, color=(0, 0, 1))


plt.xticks(x_bar, fontsize=8)
plt.title("News Sentiment Score")
plt.show()
