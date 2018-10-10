import gc #GarabageCollector

def getNumOfVE(file):
    f = file.readline().split(' ')
    return int(f[0]), int(f[1])

def count(file, v):
    c = [0 for x in range(v)]
    for x in file:
        x = x.split(' ')[:2]
        if x[0] != x[1]:
            c[ int(x[0])-1 ] = c[ int(x[0])-1 ]+1
            c[ int(x[1])-1 ] = c[ int(x[1])-1 ]+1
        else:
            c[ int(x[0])-1 ] = c[ int(x[0])-1 ]+1
    
    maxInd = 0
    maxVal = c[0]
    for x in range(1,len(c)):
        if maxVal < c[x]:
            maxVal = c[x]
            maxInd = x
    return maxInd+1

def searchMinV(file, v, listVisit, stack, typeE, discovery):
    min = 0
    for x in file:
        x = x.split(' ')[:2]
        if(int(x[0])==v):
            if min == 0  and (listVisit.count(int(x[1]))==0) and (stack.count(int(x[1]))==0):
                min=(int(x[1]))
            elif(min>int(x[1]) and (listVisit.count(int(x[1]))==0) and (stack.count(int(x[1]))==0)):
                min = int(x[1])
            if (int(x[1]) == int(x[0])) or not(int(x[1]) not in stack):
                typeE.append([int(x[0]), int(x[1]),"ret"])
                
        elif(int(x[0])>v):
            break
    return min

def searchMinVT(file, v, listVisit, stack):
    min = 0
    for x in file:
        x = x.split(' ')[:2]
        if(int(x[1])==v):
            if min == 0  and (listVisit.count(int(x[0]))==0) and (stack.count(int(x[0]))==0):
                min=(int(x[0]))
            elif(min>int(x[0]) and (listVisit.count(int(x[0]))==0) and (stack.count(int(x[0]))==0)):
                min = int(x[0])
    return min

def selectionSort(finalization):
    max = 0
    index = 0
    maxList=[]
    for x in range(len(finalization)):
        i=0
        while i<len(finalization):
            if i+1 not in maxList:
                if(max<finalization[i]):
                    index = i
                    max = finalization[i]
            i= i+1
        maxList.append(index+1)
        index = 0
        max=0
        
    return maxList

def typeE(listC, listF, file):
    file.close()
    file = open("grafos/G0.txt", "r")
    file.readline()
    fatherAux = 0
    for x in listC:
        for y in x:
            fatherAux = y-1
            for z in file:
                z = z.split(' ')[:2]
                
    return

def dfs(file, v, e, first, t, fU):
    typeA = []
    minConexIndice = 0
    conex = []
    father=[0 for x in range(v)]
    discovery = [0 for x in range(v)]
    finalization = [0 for x in range(v)]
    stack=[first]
    cont = 2
    discovery[first-1] = 1
    listVisit = []
    while 1:
        if(t):
            if(len(stack)==0 and len(listVisit)!=v):
                if(minConexIndice == 0):
                    conex.append(listVisit.copy())
                    minConexIndice = len(listVisit)
                else:
                    conex.append(listVisit[minConexIndice:].copy())
                    minConexIndice = len(listVisit)
                i=0
                while i<v:
                    if i+1 not in listVisit:
                        discovery[i] = cont
                        cont = cont+1
                        stack.append(i+1)
                        break
                    i=i+1
            aux = searchMinVT(file , stack[len(stack)-1], listVisit, stack)
        else:
            if(len(stack)==0 and len(listVisit)!=v):
                i=0
                while i<v:
                    if i not in listVisit:
                        stack[0] = i
                    i=i+1
            aux = searchMinV(file, stack[len(stack)-1], listVisit, stack, typeA, discovery)
        if aux == 0:
            finalization[stack[len(stack)-1]-1] = cont
            cont = cont +1
            listVisit.append(stack.pop())
        else:
            father[aux-1] = stack[len(stack)-1]
            discovery[aux-1] = cont
            cont = cont+1
            typeA.append([stack[len(stack)-1], aux, "arv"])
            first = aux
            stack.append(first)
        file.close()
        if(len(stack) == 0 and len(listVisit)==v):
            if(t):
                conex.append(listVisit[minConexIndice:].copy())
            break
        else:
            file = open("grafos/G0.txt", "r")
            file.readline()
    if t:
        typeE(conex, father, file)
    print(typeA)
    return selectionSort(finalization)

def main():
    gc.enable()
    file = open("grafos/G0.txt", "r")
    v,e = getNumOfVE(file)
    maxV = count(file,v)
    file.close()
    file = open("grafos/G0.txt", "r")
    file.readline()
    fU = []
    fU = dfs(file, v, e, maxV, False, fU)
    
    file.close()
    file = open("grafos/G0.txt", "r")
    file.readline()
    dfs (file, v, e, fU[0], True, fU)


    

if __name__ == '__main__':
    main()