data = open('diamond.txt').read()
print("%s %s %s" % (len(data.splitlines()), \
                    len(data.split()), len(data)))
