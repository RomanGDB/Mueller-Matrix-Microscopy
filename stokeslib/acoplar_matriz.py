import numpy as np

def acoplar_matriz(M):

  M1_show = M[:,:,:,0,0].copy()
  M2_show = M[:,:,:,1,0].copy()
  M3_show = M[:,:,:,2,0].copy()

  N = M.shape[4]

  for i in range(1, N):
    M1_show = np.append(M1_show, M[:,:,:,0,i], axis=1)
    M2_show = np.append(M2_show, M[:,:,:,1,i], axis=1)
    M3_show = np.append(M3_show, M[:,:,:,2,i], axis=1)

  M_show = np.append(M1_show, M2_show, axis = 0)
  M_show = np.append(M_show, M3_show, axis = 0)
  
  return M_show
