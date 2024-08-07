data = list(map(int, input().split()))

result = [] 
for i in data:
    if i != -999:
        result.append(i)

print(max(result), min(result))