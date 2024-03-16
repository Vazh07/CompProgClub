board = [[1,2,3,4],[2,3,4,1],[-1,-1,-1,-1],[-1,-1,-1,-1]]
options = [[3,4],[1,4],[1,2],[2,3]]
colibri = [[3,6,4],[9,2,6],[4,6,3]]


def check_position():
    pass


def sodoku_aux(options, i1, opts):
    if len(options)==0:
        return opts
    for opt in options[0]:
        if(i1==0):
            opts.append([])
        opts[-1].append(opt)
        sodoku_aux(options[1:],i1+1,opts)
    return opts

def sodoku(board, options, n, k):
    return sodoku_aux(options,0, [])


def max_colibri(flores, f_anterior):
    pass

def max_colibri(colibri):
    pass


def max_marimba_aux(num_teclas, val_teclas, indx):
    if num_teclas <= 0 or indx >= len(val_teclas):
        return 0# Caso Base
    lo_tomo = val_teclas[indx] + max_marimba_aux(num_teclas-1, val_teclas, indx+1)
    no_lo_tomo = max_marimba_aux(num_teclas, val_teclas, indx+1)
    return max(lo_tomo, no_lo_tomo)


def max_marimba(num_teclas, val_teclas):
    return max_marimba_aux(num_teclas, val_teclas,0)

print(sodoku(board,options,4,2))
#for b in sodoku(board,options,4,2):
#    print(b)
max_colibri(colibri)
# max_marimba(5,[-2, 1, -3, 4, -1])
# max_marimba(8,[-2, 1, -3, 4, -1, 2, 1, -5])
