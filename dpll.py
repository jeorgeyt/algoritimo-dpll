def leitura_do_arquivo():
    clausulas=[]
    with open('arquivo4.cnf','r') as file:#leitura do arquivo cnf
        for linha in file:#vai ler linha por linha do arquivo
            if linha.startswith('c') or linha.startswith('p'):#verifica se começa com c ou p 
                continue
            clausula=[]
            for x in linha.split():
                if x == '0':
                     break
                if x.startswith('-'):
                    clausula.append(-int(x[1:]))
                else:
                    clausula.append(int(x))

            clausulas.append(clausula)#adiciona a lista na lista maior
    return clausulas #retorna a lista 

#função recursiva onde vou verificar cada clausula e retornar seus valores verdades 
def dpll(clausulas,dicionario={}): #passa como parametros a lista clausulas e um dicionario
    
    if all(len(clausula) == 0 and any(literal in dicionario for literal in clausula) for clausula in clausulas):
        return dicionario#all verifica se cada elemento da lista tem valor verdade
        
    
    if any(len(clausula) == 0 for clausula in clausulas):#any verififica se ao menos um literal em uma clausula ja esta atribuido a o dicionario
        return False
    
    literal = next((l1 for l1 in clausulas[0] if l1 not in dicionario and -l1 not in dicionario), None)#next me garante que vai rodas em todos os literais
    
    if literal is None:
        return dicionario
    
    dicionario_true = dicionario.copy()
    dicionario_true[abs(literal)] = True#vai me dar um valor absoluto onde se tem um literal negativo e vai me dar um literal positivo
    clausulas_true = [[l2 for l2 in clausula if l2 != -literal]for clausula in clausulas if literal not in clausula]
    resultado_true=dpll(clausulas_true,dicionario_true)
    
    if resultado_true:
        return resultado_true
    
    dicionario_falso = dicionario.copy()
    dicionario_falso[abs(literal)] = False
    clausulas_falso = [[l2 for l2 in clausula if l2 != literal]for clausula in clausulas if -literal not in clausula]
    return dpll(clausulas_falso,dicionario_falso)

def main():
    clausulas=leitura_do_arquivo()
    print(clausulas)
    resultado=dpll(clausulas)
    if resultado:
        print("Sat.")
    else:
        print("unsat.")
main()
