def repetido_consecutivo(*args):
    aux = 0
    for n in args:
        if aux != 0:
            print(f"Actual {n} <=====> anterior {args[aux-1]}")
        if aux == 0:
            aux += 1
            continue
        elif aux != 0 and n == args[aux-1] and n == 0:
            return True
        
        aux +=1
    return False   
            

print(repetido_consecutivo(6,0,5,1,0,3,0))