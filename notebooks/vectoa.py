import numpy as np

def vectoa(Xg,Yg,X,Y,U,V,corrlenx,corrleny,err,b=0):
    '''
    Vectoa is a vectorial objective analysis function.
    It interpolates a velocity field (U and V, east and north velocity components)
    into a streamfunction field (dimension MxN) solving the Laplace equation:
        $nabla^{2}Psi=0$.
   ======================================================================
    Input:
        Xg & Yg - Grid of of interpolation points (i.e. LON & LAT grid)
        X & Y - Arrays of observation points
        U & V - Arrays of observed east and north components of velocity
        corrlen & err - Correlation length scales (in x and y) and error for a
                    gaussian streamfunction covariance function (floats)
        b - Constant value that forces a correction in the data mean value.
            Unless it is defined, b=0 by default.
   ======================================================================
    Output:
        PSI - Streamfuction field matrix with MxN dimension.
              The dimension of the output is always the same of XC & YC
   ======================================================================
    PYTHON VERSION by:
       Iury Sousa and Hélio Almeida - 30 May 2016
       Laboratório de Dinâmica Oceânica - IOUSP
   ======================================================================'''
   # making sure that the input variables aren't changed
    xc,yc,x,y,u,v=Xg.copy(),Yg.copy(),X.copy(),Y.copy(),U.copy(),V.copy()

    corrlen = corrleny
    xc = xc*( corrleny*1./corrlenx)
    x = x*(corrleny*1./corrlenx)

    n = len(x)
    # Joins all the values of velocity (u then v) in one column-wise array.
    # Being u and v dimension len(u)=y, then uv.shape = (2*y,1)
    uv=np.array([np.hstack((u,v))]).T    #data entered row-wise


    # CALCULATING angles and distance

    # pp is a join of two matrix calculating the distance between every point of observation and all others like the
    # example below
    # len(y) = M -> pp[0].shape = MxM being:

    #    pp[0][i] = y-y[i]
    pp = -np.tile(y,(n,1)).T+np.tile(y,(n,1)),-np.tile(x,(n,1)).T+np.tile(x,(n,1))

    #
    t = []
    for ii,jj in zip(pp[0].ravel(),pp[1].ravel()):
        t.append(np.math.atan2(ii,jj))
    t = np.array(t)
    t.shape = pp[0].shape
    # t end up to be angles and d2 the distances between every observation point and all the others
    d2=((np.tile(x,(n,1)).T-np.tile(x,(n,1)))**2+(np.tile(y,(n,1)).T-np.tile(y,(n,1)))**2)



    lambd = 1/(corrlen**2)
    bmo=b*err/lambd
    R=np.exp(-lambd*d2)        #%longitudinal
    S=R*(1-2*lambd*d2)+bmo #%transverse
    R=R+bmo

    A=np.zeros((2*n,2*n))

    A[0:n,0:n]=(np.cos(t)**2)*(R-S)+S
    A[0:n,n:2*n]=np.cos(t)*np.sin(t)*(R-S)
    A[n:2*n,0:n]=A[0:n,n:2*n]
    A[n:2*n,n:2*n]=(np.sin(t)**2)*(R-S)+S
    A=A+err*np.eye(A.shape[0])

    # angles and distances
    nv1,nv2 =xc.shape
    nv=nv1*nv2


    xc = xc.T.ravel()
    yc = yc.T.ravel()


    #% the same idea of pp but this time for interpolation points
    ppc = -np.tile(yc,(n,1)).T+np.tile(y,(nv,1)),-np.tile(xc,(n,1)).T+np.tile(x,(nv,1))
    tc = []
    for ii,jj in zip(ppc[0].ravel(),ppc[1].ravel()):
        tc.append(np.math.atan2(ii,jj))
    tc = np.array(tc)
    tc.shape = ppc[0].shape
    d2=((np.tile(xc,(n,1)).T-np.tile(x,(nv,1)))**2+(np.tile(yc,(n,1)).T-np.tile(y,(nv,1)))**2)
    R=np.exp(-lambd*d2)+bmo;


    P=np.zeros((nv,2*n))
    # streamfunction-velocity covariance
    P[:,0:n]=np.sin(tc)*np.sqrt(d2)*R;
    P[:,n:2*n]=-np.cos(tc)*np.sqrt(d2)*R;

    PSI=np.dot(P,np.linalg.solve(A,uv))   # solvi the linear system
    PSI=PSI.reshape(nv2,nv1).T

    return PSI
