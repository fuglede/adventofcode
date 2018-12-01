import pandas as pd

df = pd.read_csv('input', header=None, sep='\s+')


def is_valid(row):
    return (row[0] + row[1] > row[2]) and (row[1] + row[2] > row[0]) and (row[2] + row[0] > row[1])


# Part one
print(df.apply(is_valid, axis=1).sum())


# Part two
print(pd.DataFrame(df.values.T.reshape(len(df), 3)).apply(is_valid, axis=1).sum())
