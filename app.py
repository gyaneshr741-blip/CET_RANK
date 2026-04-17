import pandas as pd

# Years
years = [2025, 2024, 2023]

# 40 Colleges
colleges = [
    "RVCE","BMSCE","MSRIT","DSCE","PESU","BIT","BNMIT","NMIT","CMRIT","SJBIT",
    "AIT","RVU","REVA","CMRU","NHCE","JSS","SDM","KLE","PDA","BIET",
    "GAT","EWIT","RNSIT","VVCE","SIT","TCE","AMC","JIT","SJB","SEA",
    "MVJ","KSIT","BGSIT","SMVIT","NIE","MITM","GEC","PESCE","ATME","DBIT"
]

# Branches
branches = ["CSE","ECE","ME","CIVIL","AI","DS"]

data = []

# Generate data
for i, college in enumerate(colleges):
    for j, branch in enumerate(branches):
        for k, year in enumerate(years):
            cutoff = 1000 + (i * 500) + (j * 700) + (k * 300)

            data.append({
                "Year": year,
                "College": college,
                "Course": branch,
                "Cutoff": cutoff
            })

# Convert to CSV
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

print("✅ data.csv created successfully!")
