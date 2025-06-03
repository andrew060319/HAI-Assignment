import numpy as np
x=np.array([[1.0,2.0],[1.5,1.8],[5.0,8.0],
            [6.0,9.0],[1.0,0.6],[9.0,11.0]
            [8.0,2.0],[10.0,2.0],[9.0,3.0]
            ])
y=np.array(['A','A','B','B','A','B','B','B','B'])

np.random.seed(42)
indices=np.random.permutation(len(x))
split=int(0.7*len(x))

train_idx=indices[:split]
val_idx=indices[split:]

x_train,y_train=x[train_idx], y[train_idx]
x_val,y_val=x