import scipy.optimize as optimize
#     x   , y , c
c = [-30, -90, 200]
A_ub= [
    # x ,  y ,  c
    [0.25, 0.5, 0 ],
    [0.5, 1/3,  0 ],
    [0,   1/8, -1 ],
]
b_ub = [
    2.5,
    4,
    0.5,
]
bnd = [(0, float("inf")),  # Bounds of x
        (0, float("inf")),
        (0, float("inf"))
        ]

opt = optimize.linprog(c=c, A_ub=A_ub, b_ub=b_ub,
               bounds=bnd,
               method="simplex")

# res = optimize.linprog(c=c, A_ub=A_ub ,method='simplex')

print(opt)
print('here')