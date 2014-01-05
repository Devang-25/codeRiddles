checkio=eval("su"+"m") #simple yet genius one-liner!!

# --------------------------
# To make it I/O interactive
data = raw_input().split(',')
data[0] = data[0].lstrip('[')
data[-1] = data[-1].rstrip(']')
data = map(int, data)
print checkio(data)
