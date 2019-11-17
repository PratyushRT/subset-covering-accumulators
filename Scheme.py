import math
from math import pow
import hashlib

d=input()
X= input().split(' ')
d=int(d)

def powi(n, m):
    return(int(pow(n, m)))

def sib(x):
    if x%2==0:
        y=x+1
    else:
        y=x-1
    return(y)

def child(x):
    y=[2*x, 2*x+1]
    return(y)

def parent(x):
    y=x/2
    return(y)

def present(x, y):
    if x in y:
        return(True)
    else:
        return(False)

def sum2series(x):
    y=0
    for i in range(1,x+1):
        y+=powi(2, i)
    return(y)

def all_leaf_nodes(x, d):
    
    print(x)
    i= d-int(math.floor(math.log(x, 2)))
    leaf_nodes=[]
    for j in range(powi(2, i)):
        leaf_nodes.append(x*powi(2, i)+ j)
    return(leaf_nodes)
            
        




def Sij(d, X):

    cvr=[]
    Y=[]



    for i in range(powi(2, d), powi(2, d+1)):
        if i not in X:
            Y.append(i)

    X=Y


    for i in range(len(X)):

        x=X[i]
        
        if present(sib(x), X)  :

            for j in range(d):
                for k in range(len(all_leaf_nodes(parent(parent(x)), d))):
                               if all_leaf_nodes(parent(parent(x)), d)[k] not in X:
                                   cvr.append([parent(parent(x)), sib(parent(x)) ])
                                       
                                   break
                               else:
                                   if k==len(all_leaf_nodes(parent(parent(x)), d))-1:
                                       x=parent(x)
                                   

            
        else:
            cvr.append([parent(x), sib(x)])

    final=[]   ## list of i, j pairs

    for i in range(len(cvr)):
        if cvr[i] not in final:
            final.append(cvr[i])
            

   

    list_nodes=[]   ## list of s_ij's

    for j in range(len(final)):
        list_nodes.append([x for x in all_leaf_nodes(final[j][0], d) if x not in all_leaf_nodes(final[j][1], d)])



    return(list_nodes)

def hashed(d):
    hashed=[0]*(powi(2, d+1))

    for j in range(powi(2, d), powi(2, d+1)):
            hasher= hashlib.sha256()
            hasher.update(str(j))
            hashed[j]=hasher.digest()

    for i in range(d-1, -1, -1):
        for j in range(powi(2, i), powi(2, i+1)):
            
            hasher= hashlib.sha256()
            hasher.update(hashed[child(j)[0]]+ hashed[child(j)[1]] )
            hashed[j]=hasher.digest()
    return(hashed)
    

def Acc(d, X):
    
            
    mem=[]
    non_mem=[]
    
    for j in range(len(CVR(d, X))):
        mem.append(CVR(d, X)[j][0])      
        non_mem.append(CVR(d, X)[j][1])

##        mem.append(hashed(d)[CVR(d, X)[j][0]])      
##        non_mem.append(hashed(d)[CVR(d, X)[j][1]])

    return("members:", mem, "non members:", non_mem)

def CVR(d, X):

    cvr=[]
    Y=[]



    for i in range(powi(2, d), powi(2, d+1)):
        if i not in X:
            Y.append(i)

    X=Y


    for i in range(len(X)):

        x=X[i]
        
        if sib(x) in X   :

            for j in range(d):
                for k in range(len(all_leaf_nodes(parent(parent(x)), d))):
                               if all_leaf_nodes(parent(parent(x)), d)[k] not in X:
                                   cvr.append([parent(parent(x)), sib(parent(x)) ])
                                       
                                   break
                               else:
                                   if k==len(all_leaf_nodes(parent(parent(x)), d))-1:
                                       x=parent(x)
                                   

            
        else:
            cvr.append([parent(x), sib(x)])

    final=[]   ## list of i, j pairs

    for i in range(len(cvr)):
        if cvr[i] not in final:
            final.append(cvr[i])
            

   

    list_nodes=[]   ## list of s_ij's

    for j in range(len(final)):
        list_nodes.append([x for x in all_leaf_nodes(final[j][0], d) if x not in all_leaf_nodes(final[j][1], d)])



    return(final)


def Sijlist(d, X):

    cvr=[]
    Y=[]



    for i in range(powi(2, d), powi(2, d+1)):
        if i not in X:
            Y.append(i)

    X=Y
    Sijlist=[0]*(powi(2, d+1) )

    for i in range(len(X)):

        x=X[i]
        y=x
        if sib(x) in X  :
            
            
            for j in range(d):
                for k in range(len(all_leaf_nodes(parent(parent(x)), d))):
                               if all_leaf_nodes(parent(parent(x)), d)[k] not in X:
                                   cvr.append([parent(parent(x)), sib(parent(x)) ])
                                   Sijlist[y]= parent(x)
                                   break
                               else:
                                   if k==len(all_leaf_nodes(parent(parent(x)), d))-1:
                                       x=parent(x)
                                   

            
        else:
            cvr.append([parent(x), sib(x)])
            Sijlist[y]= sib(x)

    Y=[]



    for i in range(powi(2, d), powi(2, d+1)):
        if i not in X:
            Y.append(i)

    X=Y
    
    for i in range(powi(2, d), powi(2, d+1)):
        if Sijlist[i]==0:
            for k in range(len(all_Tj(d, X))):
               
                    if i in all_Tj(d, X)[k]:
                        Sijlist[i]=all_Tj(d, X)[k][0]


    
    return(Sijlist)
    

 


def all_Tj(d, X):
    Tj=[]
    
    
    for i in range(len(CVR(d, X))):
        k=all_leaf_nodes(CVR(d, X)[i][1], d)
        k.insert(0, CVR(d, X)[i][1])
        Tj.append(k)
        
    
    return(Tj)        

def WitGen(x, X, d):
    witx=[]
    for k in range(len(Sij(d, X))):
        ##member
        if x in Sij(d, X)[k]:
            j=Acc(d, X)[3][k]
            
            witx.append(sib(x))
            while sib(x)>j:
                x=parent(x)
                witx.append(sib(x))

            break
            

        else:
            ifbreak=False
            for i in range(len(all_Tj(d, X))):
                
                if x==all_Tj(d, X)[i][0]:
                    ##non-member j itself
                    witx.append(x)
                    break

                #non member a member of Tj
                
                    
                if len(witx)==0 and x in all_Tj(d, X)[i] :
                    j= all_Tj(d, X)[i][0]
                    y=x
                    while y>j:
                        witx.append(sib(y))
                        y=parent(x)
    witx_final=[]                        
                
    for i in range(len(witx)):
        if witx[i] not in witx_final:
            witx_final.append(witx[i])
    
    return(witx_final)
                    
                    
print(Acc(d,X))
                    

k_desc=[k]              
for i in range(levels):
    for j in range(0, powi(2, i), -1):
        curr=[]
        curr.append(child(k_desc[-(j+1)])[0]
        curr.append(child(k_desc[-(j+1)])[1]

        


