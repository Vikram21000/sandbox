import pandas as pd
import statistics as stats

scores = pd.read_csv(r"C:\Users\vikra\Downloads\school_scores.csv")
def main():
    percent_score()
    scores = scores.drop(columns=["Score", "Max Score"])
    print(scores)

def percent_score():
    percentage = []
    for _, j in scores.iterrows():
        percent = (j["Score"]/j["Max Score"]) * 100
        percentage.append(round(percent,2))
    scores["Percentage score"] = percentage

def global_mean():
    global_mean = stats.mean(scores["Percentage score"])
    return global_mean

def global_sd():
    global_sd = stats.stdev(scores["Percentage score"])
    return global_sd

def local_zscore():
    n_zscore = []
    c_zscore = []
    for _, j in scores.iterrows():
        if j["School"] == "Netherhall":
            print("Netherhall")
        else:
            print("Coleridge")

local_zscore()