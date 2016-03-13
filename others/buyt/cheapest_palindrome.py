final = []
cases = int(raw_input())

def check_cost(costs, ip, cost):
    min_cost_var = min(costs, key=costs.get)    
    # import pdb; pdb.set_trace()
    s1 = list(ip[:len(ip)/2][::-1])
    s2 = list(ip[len(ip)/2:])

    if '/' in ip:
        while '/' in s1:
            ix = s1.index('/')
            if s2[ix] is not '/':
                s1[ix] = s2[ix]
                cost += costs[s1[ix]]
            else:
                s1[ix] = min_cost_var
                s2[ix] = s1[ix]
                cost += 2*costs[s1[ix]]

        while '/' in s2:
            ix = s2.index('/')
            s2[ix] = s1[ix]
            cost += costs[s2[ix]]

        if not ''.join(s1) == ''.join(s2):
            cost = -1
    else:
        if not s1 == s2:
            cost = -1

    return cost


for i in xrange(cases):
    cost = 0
    ip = raw_input()
    costs = { 'a':  int(raw_input()), 'b':  int(raw_input())}
    assert len(ip)%2 == 0
    assert 1 <= len(ip) <= 10000
    assert set(ip).issubset({'/', 'a', 'b'})
    assert 1 <= costs['a'] <= 100
    assert 1 <= costs['b'] <= 100
    cost = check_cost(costs, ip, cost)
    final.append(cost)

for i in xrange(len(final)):
    print final[i]
