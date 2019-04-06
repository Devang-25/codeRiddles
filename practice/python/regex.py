import re
import string

ip = """# ..because rest of the output near the end contains arbitrary RGBA values\n# which is obviously because those boxes in 50 shades of gray don't fully"""

pat = r"[{}]".format(string.punctuation)

print(ip)
print
print(re.sub(pat, '', ip))
