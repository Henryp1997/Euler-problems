# generate pascal's triangle divided by 10 (allows python to calculate all numbers without overflowing)
row_0 = [0.1] + [0 for i in range(99)]

rows = [row_0]
for i in range(1, 101):
    row = [0.1]
    for j in range(1, 101):
        try:
            row.append(rows[i - 1][j - 1] + rows[i - 1][j])
        except:
            print(i)
    rows.append(row)

all_rows_together = []
for row in rows:
    for i in row:
        all_rows_together.append(i)

num = [i for i in all_rows_together if i > 100_000]

print(len(num))