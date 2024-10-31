import numpy as np

def calcular_s3(S_in, DoP, signos):

  # S3 Modulo
  S_in[:,:,:,3,:] = np.sqrt(DoP**2 * S_in[:,:,:,0,:].astype(float)**2 - S_in[:,:,:,1,:].astype(float)**2 - S_in[:,:,:,2,:].astype(float)**2)

  # S3 Signo
  for i, signo in enumerate(signos):
    S_in[:,:,:,3,i] = signo * S_in[:,:,:,3,i]

  return S_in