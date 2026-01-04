import pandas as pd
import sys
infile = sys.argv[1]
outfile = sys.argv[2]

df = pd.read_csv(infile, sep="\t")
counts = (
        df
        .groupby(["GO", "sample"])
        .size()
        .reset_index(name="counts")
)
matrix=counts.pivot(
        index="GO",
        columns="sample",
        values="count"
).fillna(0).astype(int)

matrix.to_csv(outfile, sep="\t")
