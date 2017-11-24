import numpy as np
from sympy import symbols, pi
from model import Model
from chain import Chain
from scale import Scale


model = Model().make()
model.load_weights('model_weights.h5')

chain = Chain()
a1, a2, a3 = symbols('a1:4')
chain.link(1.0, a1, 0.0, 0.0)
chain.link(1.0, a2, 0.2, pi/2)
chain.link(1.0, a3, 0.1, 0.0)

angle_scale    = Scale([-np.pi/4, np.pi/4], [-0.5, 0.5])
position_scale = Scale([-10.0,    10.0   ], [-0.5, 0.5])

# Normalized position
p1 = position_scale.forward_scale(2.0)
p2 = position_scale.forward_scale(1.0)
p3 = position_scale.forward_scale(1.5)
p  = np.array([[p1, p2, p3]])

# Prediction
r = model.predict(p)

# Un-normalize angles
a1 = angle_scale.reverse_scale(r[0][0])
a2 = angle_scale.reverse_scale(r[0][1])
a3 = angle_scale.reverse_scale(r[0][2])
print([a1, a2, a3])

# Compute position with real transform based on angle
q = chain.forward({
    'a1': a1, 
    'a2': a2, 
    'a3': a3
})
print(q)




