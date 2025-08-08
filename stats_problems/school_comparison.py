import pandas as pd
import statistics as stats

scores = pd.read_csv(r"C:\Users\vikra\Downloads\school_scores.csv")

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

def zscore():
    global combined
    nhl = scores[scores["School"] == "Netherhall"].copy()
    nhl_mean = nhl["Score"].mean()
    nhl_stdev = nhl["Score"].std()
    nhl["Z-score"] = (nhl["Score"] - nhl_mean) / nhl_stdev

    col = scores[scores["School"] == "Coleridge"].copy()
    col_mean = col["Score"].mean()
    col_stdev = col["Score"].std()
    col["Z-score"] = (col["Score"] - col_mean) / col_stdev
    
    combined = pd.concat([nhl, col])
    #print(combined)
    
zscore()

def norm_score():
    norm_score = []
    for _, j in combined.iterrows():
        normscore = global_mean() + global_sd() * j["Z-score"]
        norm_score.append(round(normscore, 2))
    combined["Normalised score"] = norm_score
    newcombined = combined.drop(["Score", "Max Score", "Z-score"], axis=1)
    sort_newcombined = newcombined.sort_values(by="Normalised score", ascending=False)
    print(sort_newcombined)
    sort_newcombined.to_csv("NormScores.csv")
norm_score()