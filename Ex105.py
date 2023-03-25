def notas(*num, sit=False):
    """
    Recebe várias notas de alunos e retorna um dicionário com as seguintes informações:
    - Quantidade de notas;
    - A maior nota;
    - A menor nota; 
    - A média da turma; 
    - A situação (opcional)
    """
    notas = {}
    notas['total'] = len(num)
    notas['maior'] = max(num)
    notas['menor'] = min(num)
    notas['media'] = sum(num)/len(num)
    if sit == True:
        if notas['media'] < 3:
            notas['situação'] = 'RUIM'
        elif 3 <= notas['media'] < 6:
            notas['situação'] = 'REGULAR'
        elif 6 <= notas['media'] < 8:
            notas['situação'] = 'BOA'
        else:
            notas['situação'] = 'EXCELENTE'
    return notas

resp = notas(5.0, 8.5, 10, sit=True)
print(resp)
print('-'*30)
help(notas)