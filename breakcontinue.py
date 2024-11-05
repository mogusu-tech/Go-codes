#Break Statement

num = 20
while num <= 25:
    print(num)
    if num == 23:
        break
    num += 1

#Continue statement
devices = ["laptop","phone","tablet"]
for device in devices:
    if device == "phone":
        continue
    print(device)