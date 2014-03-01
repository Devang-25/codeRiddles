def checkio(data):
    try:
        if len(data)>=2:
            return data.pop()+checkio(data)
        else:
            return data.pop()
    except:
        pass

if __name__=='__main__':
    # input comma-separated elements into array (optional: '[]')
    data = raw_input().split(',')
    data[0] = data[0].lstrip('[')
    data[-1] = data[-1].rstrip(']') 

    data = map(int, data) # checks and converts list of strings into integers
    print checkio(data)
        

"""
List of forbidden words:
sum
import
for
while
reduce
"""
