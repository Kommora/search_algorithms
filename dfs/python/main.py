import gc

def fileToDict(path):
    file = open(path, "r")
    g = {'ini':file.readline().replace('\r','').replace('\n','').split(' ')}
    for x in file:
        x = x.split(' ')[:2]
        if not g.get(int(x[0])):
            g[int(x[0])] = []
        g.get(int(x[0])).append(int(x[1]))
    file.close()
    return g

def graphToTranpost(g):
    gT = {'ini':g['ini']}
    for x,y in g.items():
        if x != 'ini':
            for z in y:
                if not gT.get(z):
                    gT[z] = []
                gT.get(z).append(x)
    return gT

def selFirst(g):
    min = [0 for x in range(int(g['ini'][0]))]
    for x,y in g.items():
        if x != 'ini':
            min[x-1] = min[x-1]+len(y)
            for z in y:
                if z != x:
                    min[z-1] = min[z-1]+1
    maxInd = 0
    maxVal = min[0]
    for x in range(1,len(min)):
        if maxVal < min[x]:
            maxVal = min[x]
            maxInd = x
    return maxInd

def next(g, gray, black, first, discovery, edge):
    minLabel = 0
    if g.get(first):
        for x in g[first]:
            if x == first:
                edge.append([x,x,'ret'])
            elif x in gray and [first, x,'ret'] not in edge:
                edge.append([first, x,'ret'])
            elif x in black and [first, x, 'arv'] not in edge and [first, x, 'avan'] not in edge and [first, x, 'ret'] not in edge and [first, x, 'cruz'] not in edge:
                if discovery[x-1] < discovery[first-1]:
                    edge.append([first, x,'avan'])
                else:
                    edge.append([first, x,'cruz'])
            if minLabel==0 and (x not in gray) and (x not in black):
                minLabel = x
            elif minLabel>x and (x not in gray) and (x not in black):
                minLabel = x
    return minLabel

def topologicSort(finalization):
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

def dfs(g, first, t, topologic):
    discovery = [0 for x in range(int(g['ini'][0]))]
    finalization = [0 for x in range(int(g['ini'][0]))]
    conex = []
    gray = []
    black = []
    edge = []
    time = 0
    lastIndex = 0
    while 1:

        if (first not in gray) and (first not in black) and first != 0:
            time = time +1
            discovery[first-1] = time
            gray.append(first)
            aux = next(g, gray, black, first, discovery, edge)
            if aux != 0:
                edge.append([first, aux, 'arv'])
            first = aux
        if first == 0:
            first = gray.pop()
            black.append(first)
            time = time +1
            finalization[first-1] = time
            if len(gray)==0 and len(black)==int(g['ini'][0]):
                if t:
                    conex.append(black[lastIndex:])
                break
            elif len(gray)==0 and len(black)!=int(g['ini'][0]):
                if t:
                    if lastIndex == 0:
                        conex.append(black[lastIndex:])
                        lastIndex = len(black)
                    else:
                        conex.append(black[lastIndex:])
                        lastIndex = len(black)
                    for x in topologic:
                        if x not in black:
                            first = x
                            time = time +1
                            discovery[first-1] = time
                            gray.append(first)
                            break
                else:
                    for x,y in g.items():
                        if x != 'ini' and (x not in black):
                            first = x
                            time = time +1
                            discovery[first-1] = time
                            gray.append(first)
                            break
            first = next(g, gray, black, gray[len(gray)-1], discovery, edge)
            if first != 0:
                edge.append([gray[len(gray)-1], first, 'arv'])
    if t:
        print(conex)
        print()
    else:
        print(discovery)
        print(finalization)
        print(edge)
    return topologicSort(finalization)


def main():
    gc.enable()
    for x in range(55):
        g = fileToDict("grafos/G"+str(x)+".txt")
        topologic = dfs(g, selFirst(g)+1, False, [])
        gT = graphToTranpost(g)
        dfs(gT, selFirst(g)+1, True, topologic)

    return

if __name__ == '__main__':
    main()