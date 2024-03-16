def solve(board=[], n=0, k=0):
    has_sol = "yes"
    n = int(n)
    k = int(k)
    indx = 0
    opts = []
    while indx < n:
        options = list(range(1, n+1))
        for opt in board:
            try:
                del options[options.index(int(opt[indx]))]
            except ValueError:
                pass
        if options in opts:
            opts.append(options)
        else:
            opts.append(options[::-1])
        indx += 1
    #print(opts)
    for indx1 in range(k, n):
        options = list(range(1, n+1))
        for indx2, _ in enumerate(board[indx1]):
            selected = 0
            for opIndx, op in enumerate(opts[indx2]):
                if int(op) in options:
                    selected = op
                    del opts[indx2][opIndx]
            try:
                del options[options.index(selected)]
            except ValueError:
                pass
            board[indx1][indx2] = selected
            if selected == 0:
                has_sol = "no"
    #print(board)
    print(has_sol)
    if has_sol == 'yes':
        for row in board:
            c = ""
            for cell in row:
                c += f"{cell} "
            print(c)


#nk = input()
#n, k = nk.split(' ')
#board = [['-1'] * int(n) for _ in range(int(n))] #[['-1']*int(n)]*int(n)
#for i in range(int(k)):
#    board[i] = input().split(' ')
solve([['1','2','3','4'],['2','3','4','1'],['-1','-1','-1','-1'],['-1','-1','-1','-1']], 4, 2)
