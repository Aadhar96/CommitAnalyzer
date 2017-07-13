def kmeans(data,clus,lo):
    from random import sample
    from numpy import inf
    ch=sample(range(len(data)),clus)
    c=[[] for i in range(clus)]
    for i in range(len(data)):
        tmp=0
        mi=inf
        for j in range(clus):
            tmp1=((data[i][0]-data[ch[j]][0])**2+(data[i][0]-data[ch[j]][0])**2)**0.5
            if(tmp<mi):
                mi=tmp1
                tmp=j
        c[tmp].append(i)
    n=[]
    for i in range(len(c)):
        sum=array([0,0])
        for j in c[i]:
            sum[0]+=data[j][0]
            sum[1]+=data[j][1]
        if(len(c[i])!=0):
            n.append([sum[0]/len(c[i]),sum[1]/len(c[i])])
        else:
            n.append([data[ch[i]][0],data[ch[i]][1]])
    return [c,ch]
    lo=0
    while True:
        lo+=1
        if(lo>9):
            return c
            break
        ch=n.copy()
        d=[[] for i in range(clus)]
        for i in range(len(data)):
            tmp=0
            mi=inf
            for j in range(clus):
                tmp1=((data[i][0]-ch[j][0])**2+(data[i][0]-ch[j][1])**2)**0.5
                if(tmp<mi):
                    mi=tmp1
                    tmp=j
            d[tmp].append(i)
        n=[]
        for i in range(len(c)):
            sum=array([0,0])
            for j in d[i]:
                sum[0]+=data[j][0]
                sum[1]+=data[j][1]
            if(len(d[i])!=0):
                n.append([sum[0]/len(d[i]),sum[1]/len(d[i])])
            else:
                n.append([ch[i][0],ch[i][1]])
        print(c)
        if(c==d):
            return n
            break
        else:
            c=d.copy()

def soc(data,h1,h2,h3):
    from sklearn import cluster
    import numpy as np
    from random import uniform as u
    from numpy.linalg import norm
    data=np.array(data)
    mi=data.min(axis=0)
    ma=data.max(axis=0)
    n=h1
    n1=h2
    it=h3
    init=[]
    velo=[]
    kmeans=cluster.KMeans(n_clusters=n1)
    kmeans.fit(data)
    c=len(data[0])
    for i in range(n):
        for k in range(n1):
            tmp=[]
            tmp1=[]
            for j in range(c):
                tmp.append(u(mi[j],ma[j]))
                tmp1.append(u(0,1))
            init.append(tmp)
            velo.append(tmp1)
    for i in range(len(kmeans.cluster_centers_)):
        init[i-n1]=kmeans.cluster_centers_[i]
    init=np.array(init)
    velo=np.array(velo)
    mii=0
    pbest=np.array([np.ndarray([n1,c]) for i in range(n)])
    pb=np.array([np.inf for i in range(n)])
    gbest=np.array([np.ndarray([n1,c])])
    gb=np.inf
    c1=2
    c2=1.5
    for k in range(it):
        for l in range(n):
            clus={}
            for i in data:
                mic=10**100
                for j in range(n1):
                    tmp=norm(i-init[l*n1+j])
                    if(tmp<mic):
                        mii=j
                        mic=tmp
                clus.update({tuple(i):mii})
            sum=0
            for m in set(clus.values()):
                tmp1=[k for (k,v) in clus.items() if v==m]
                for x in tmp1:
                    sum+=norm(np.array(x)-init[l*n1+m])/len(tmp1)
            if(set(range(n1))-set(clus.values())):
                sum=sum*10
            sum=sum/n1
            if(sum<pb[l]):
                pb[l]=sum
                pbest[l]=init[l*n1:(l+1)*n1]
            if(sum<gb):
                gb=sum
                gbest[0]=init[l*n1:(l+1)*n1]
            velo[l*n1:(l+1)*n1]=velo[l*n1:(l+1)*n1]+c1*u(0,1)*(pbest[l]-init[l*n1:(l+1)*n1])+c2*u(0,1)*(gbest[0]-init[l*n1:(l+1)*n1])
            init[l*n1:(l+1)*n1]=init[l*n1:(l+1)*n1]+velo[l*n1:(l+1)*n1]
    clus={}
    for i in data:
        mic=10**100
        for j in range(n1):
            tmp=norm(i-gbest[0][j])
            if(tmp<mic):
                mii=j
                mic=tmp
        clus.update({tuple(i):mii})
    return [clus,gbest]
