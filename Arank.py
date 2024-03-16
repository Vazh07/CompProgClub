def rank(n,matches):
    teams = [f'T{i}' for i in range(1,int(n)+1)]
    for match in matches:
        w = teams.index(match[0])
        l = teams.index(match[1])
        if w>l:
            t1 = []
            for t in teams:
                if(t!=match[1]):
                    t1.append(t)
                    if(t==match[0]):
                        t1.append(match[1])
            teams = t1
    s = ""
    for t in teams:
        s="{} {}".format(s, t)
    print(s)
nm = input()
n,m = nm.split(' ')
matches=[]
for _ in range(int(m)):
    teams = input()
    matches.append(teams.split(' '))
rank(n,matches)
