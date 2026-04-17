import pandas as pd

# Years
years = [2025, 2024, 2023]

# All colleges
colleges = [
    "RVCE","BMSCE","MSRIT","DSCE","PESU","BIT","BNMIT","NMIT","CMRIT","SJBIT",
    "AIT","RVU","REVA","CMRU","NHCE","JSS","SDM","KLE","PDA","BIET",
    "GAT","EWIT","RNSIT","VVCE","SIT","TCE","AMC","JIT","SJB","SEA",
    "MVJ","KSIT","BGSIT","SMVIT","NIE","MITM","GEC","PESCE","ATME","DBIT"
]

branches = ["CSE","ECE"]

data = []

# ✅ STEP 1: Add your FIXED data
fixed_data = [
    (2025,"RVCE","CSE",1200),(2024,"RVCE","CSE",1500),(2023,"RVCE","CSE",1800),
    (2025,"RVCE","ECE",2500),(2024,"RVCE","ECE",2800),(2023,"RVCE","ECE",3200),

    (2025,"BMSCE","CSE",2000),(2024,"BMSCE","CSE",2300),(2023,"BMSCE","CSE",2600),
    (2025,"BMSCE","ECE",3500),(2024,"BMSCE","ECE",3900),(2023,"BMSCE","ECE",4200),

    (2025,"MSRIT","CSE",1800),(2024,"MSRIT","CSE",2100),(2023,"MSRIT","CSE",2500),
    (2025,"MSRIT","ECE",3000),(2024,"MSRIT","ECE",3400),(2023,"MSRIT","ECE",3700),

    (2025,"DSCE","CSE",4000),(2024,"DSCE","CSE",4500),(2023,"DSCE","CSE",5000),
    (2025,"DSCE","ECE",6000),(2024,"DSCE","ECE",6500),(2023,"DSCE","ECE",7000),

    (2025,"PESU","CSE",900),(2024,"PESU","CSE",1200),(2023,"PESU","CSE",1500),
    (2025,"PESU","ECE",2200),(2024,"PESU","ECE",2600),(2023,"PESU","ECE",3000),

    (2025,"BIT","CSE",3500),(2024,"BIT","CSE",3800),(2023,"BIT","CSE",4200),
    (2025,"BIT","ECE",5000),(2024,"BIT","ECE",5400),(2023,"BIT","ECE",5800),

    (2025,"BNMIT","CSE",7000),(2024,"BNMIT","CSE",7500),(2023,"BNMIT","CSE",8000),
    (2025,"BNMIT","ECE",9000),(2024,"BNMIT","ECE",9500),(2023,"BNMIT","ECE",10000),

    (2025,"NMIT","CSE",8500),(2024,"NMIT","CSE",9000),(2023,"NMIT","CSE",9500),
    (2025,"NMIT","ECE",11000),(2024,"NMIT","ECE",11500),(2023,"NMIT","ECE",12000),

    (2025,"CMRIT","CSE",9500),(2024,"CMRIT","CSE",10000),(2023,"CMRIT","CSE",10500),
    (2025,"CMRIT","ECE",12000),(2024,"CMRIT","ECE",12500),(2023,"CMRIT","ECE",13000),

    (2025,"SJBIT","CSE",12000),(2024,"SJBIT","CSE",12500),(2023,"SJBIT","CSE",13000),
    (2025,"SJBIT","ECE",14000),(2024,"SJBIT","ECE",14500),(2023,"SJBIT","ECE",15000),
]

for row in fixed_data:
    data.append({
        "Year": row[0],
        "College": row[1],
        "Course": row[2],
        "Cutoff": row[3]
    })

# ✅ STEP 2: Auto-generate remaining colleges
remaining_colleges = colleges[10:]

for i, college in enumerate(remaining_colleges):
    for j, branch in enumerate(branches):
        for k, year in enumerate(years):
            cutoff = 10000 + (i * 500) + (j * 2000) + (k * 300)

            data.append({
                "Year": year,
                "College": college,
                "Course": branch,
                "Cutoff": cutoff
            })

# Save CSV
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

print("✅ Perfect data.csv created!")
