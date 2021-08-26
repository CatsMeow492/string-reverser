def spell(txt):
    txt = list(txt)
    if len(txt) == 0:
        return
    else:
        print(txt[-1])
        txt.pop(-1)
        spell(txt)
        
    

txt = input()
spell(txt)
