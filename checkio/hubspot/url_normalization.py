import re 

examples = """
Examples:
checkio("Http://Www.Checkio.org") == "http://www.checkio.org"
checkio("http://www.checkio.org/%cc%b1bac") == "http://www.checkio.org/%CC%B1bac"
checkio("http://www.checkio.org/task%5F%31") == "http://www.checkio.org/task_1"
checkio("http://www.checkio.org:80/home/") == "http://www.checkio.org/home/"
checkio("http://www.checkio.org:8080/home/") == "http://www.checkio.org:8080/home/"
checkio("http://www.checkio.org/task/./1/../2/././name") == "http://www.checkio.org/task/2/name"
"""

def checkio(data):
    #p = re.compile('[^a-zA-Z0-9_]+')    
    #p = re.compile('[a-z]+')
    #x = p.split(data())
    #print "x: ",x
    #return data.split(x.lower())[0] + x
    escape_seq_list = re.split('%',data)
    esc_seq = escape_seq_list[1:]
    url = escape_seq_list[0].lower()
    for i in esc_seq:
        url += '%' + i.upper()
    return url

if __name__ == '__main__':
    print examples
    data = raw_input()
    print checkio(data)
