def heapify(i,x,N):
    l=2*i
    r=l+1
    curr=i
    try:
        if(l<N and x[l]<x[curr]):
            curr=l
    except:
        print("ERROR",l,N,curr)
    if(r<N and x[r]<x[curr]):
        curr=r
    if(i!=curr):
        x[i],x[curr]=x[curr],x[i]
        heapify(curr,x,N)

def make(x,N):
    tmp=(N-1)//2
    for i in range(tmp,0,-1):
        heapify(i,x,N)

def extractmin(x,N):
    tmp=x[1]
    x[1]=x[-1]
    x.pop()
    heapify(1,x,N)
    return tmp

def KNN(test,k=25):
    import pickle
    from numpy.linalg import norm as no
    from numpy import array
    data=open("django_data","rb")
    x=pickle.load(data)
    data.close()
    data=open("django_y","rb")
    y=pickle.load(data)
    data.close()
    test=array(test)
    dis=[-1]
    for i in range(len(x)):
        dis.append([no(test-x[i]),i])
    N=len(dis)
    make(dis,N)
    k_nn=[]
    for i in range(k):
        k_nn.append(extractmin(dis,N))
        N=len(dis)
    for i in range(k):
        k_nn[i]=y[k_nn[i][1]]
    if(k_nn.count(0)>=(k-k//2)):
        return False
    else:
        return True
