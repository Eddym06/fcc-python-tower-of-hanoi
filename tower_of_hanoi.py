def hanoi_solver(n):
    # Inicializar las 3 varillas
    A = list(range(n, 0, -1))
    B = []
    C = []
    
   
    moves = [f"{A} {B} {C}"]
    
    def move(disks, source, target, auxiliary):
        if disks > 0:
            # Mover n-1 discos de origen a auxiliar
            move(disks - 1, source, auxiliary, target)
            
            # Mover el disco actual de origen a destino
            target.append(source.pop())
            moves.append(f"{A} {B} {C}")
            
            # Mover n-1 discos de auxiliar a destino
            move(disks - 1, auxiliary, target, source)

    # Iniciar recursión
    move(n, A, C, B)
    
   
    return "\n".join(moves)
