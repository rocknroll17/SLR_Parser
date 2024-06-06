import pandas as pd

# 엑셀 파일 읽기
df = pd.read_excel('table.xlsx')

# 원하는 특정 위치 조회 (예: A1 셀)
value = df.iat[1, 0]
print(value)
action = []
goto = []
for i in range(1, 150):
    if pd.isna(df.iat[i, 0]):
        break
    value = int(df.iat[i, 0])
    action_row = []
    goto_row = []
    for j in range(1, 23):
        key = df.iat[0, j]
        value = df.iat[i, j]
        if pd.isna(value):
            continue
        value = value.replace("s", "S").replace("r", "R").replace("acc", "ACC")
        action_row.append((key, value))
    for j in range(23, 39):
        key = df.iat[0, j]
        value = df.iat[i, j]
        if pd.isna(value):
            continue
        goto_row.append((key, value))
    action.append(action_row)
    goto.append(goto_row)


results = []

for i in range(len(action)):
    action_str = '"ACTION":{' + ','.join([f'"{key}":"{value}"' for key, value in action[i]]) + '}'
    goto_str = '"GOTO":{' + ','.join([f'"{key}":{value}' for key, value in goto[i]]) + '}'
    result_str = f'{{{action_str}, {goto_str}}}'
    results.append(result_str)
final_output = '[\n' + ',\n'.join(results) + '\n]'
print(final_output)