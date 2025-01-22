from sympy import Matrix, Rational

def escalonar_matriz(matriz):
    """
    Função para escalonar uma matriz usando eliminação de Gauss
    
    Args:
        matriz: Lista de listas ou matriz SymPy
        
    Returns:
        Matriz escalonada na forma de matriz SymPy
    """
    # Converter para matriz SymPy se não for
    if not isinstance(matriz, Matrix):
        matriz = Matrix(matriz)
    
    # Obter dimensões
    m, n = matriz.shape
    
    # Converter elementos para racionais para evitar erros de ponto flutuante
    matriz = matriz.applyfunc(lambda x: Rational(x) if isinstance(x, (int, float)) else x)
    
    # Aplicar eliminação de Gauss
    return matriz.rref()[0]

def produto_interno(u_col, matriz_produto_interno, v_col):
    """
    Função para calcular o produto interno entre dois vetores dados uma matriz produto interno
    
    Args:
        u_col: vetor coluna ou lista
        matriz_produto_interno: lista de listas ou matriz SymPy
        v_col: vetor coluna ou lista
    Returns:
        Produto interno (escalar) usando matriz produto interno
    """
    # Garantir que u_col e v_col sejam vetores coluna
    if not isinstance(u_col, Matrix):
        u_col = Matrix(u_col if isinstance(u_col[0], list) else [[elem] for elem in u_col])
    if not isinstance(v_col, Matrix):
        v_col = Matrix(v_col if isinstance(v_col[0], list) else [[elem] for elem in v_col])
    
    # Garantir que matriz_produto_interno seja uma matriz
    if not isinstance(matriz_produto_interno, Matrix):
        matriz_produto_interno = Matrix(matriz_produto_interno)

    return u_col.T * matriz_produto_interno * v_col

# Exemplo de uso:
def escalonar_matriz_dada():
    # Criar uma matriz exemplo
    A = Matrix([
        [-4, 6, 4, 16],
        [4, -4, 3, 13],
        [3, 5, -1, 32]
    ])
    print("Matriz original:")
    print(A)
     
    print("\nMatriz escalonada:")
    print(escalonar_matriz(A))

"""
Questao Considere o espaço R3
 com o produto interno definido pela matriz
101,020,102

Combine cada vetor v
 com um outro vetor ortogonal a v
"""
def achar_vetores_ortogonais_pelo_produto_interno():
    Matriz_produto_interno = Matrix([[1,0,1],
                                [0,2,0],
                                 [1,0,2]])
    vetores_1 = [[0,1,2], [1,0,0], [0,0,1], [1,1,1]]
    vetores_2 = [[0,0,1],[3,0,-2], [1,0,-1], [1,2,3], [2,0,-1]]

    for vec1 in vetores_1:
        for vec2 in vetores_2:
            resultado = produto_interno(vec1, Matriz_produto_interno, vec2)
            if resultado[0] == 0:
                {
                    print(vec1, "é ortogonal a", vec2)
                }

achar_vetores_ortogonais_pelo_produto_interno()
