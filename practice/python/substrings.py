def generate_substrings(ip):
    ip_len = len(ip)
    return set([ip[i:j+1] for i in range(ip_len) for j in range(i,ip_len)])

