import sympy as sp

# variabel
x1, x2, x3, x4,z = sp.symbols('x1 x2 x3 x4,z')

# fungsi minn
eq0 = 1.5*x1 + 2.5*x2 - 0*x3 - 0*x4 - z
minn = 9999999
#  batasan
eq1 = sp.Eq(x1 + 3*x2 - x3 - 3,0)
eq2 = sp.Eq(x1 + x2 - x4 - 2,0)

#kasus 1 x1 = x2 = 0
x3_val = sp.solve(eq1.subs({x1 : 0,x2 : 0}),x3)[0]
x4_val = sp.solve(eq2.subs({x1 : 0,x2 : 0}),x4)[0]
if x3_val >=0  and x4_val >= 0 :
    kas1_val = sp.solve(eq0.subs({x1 : 0,x2 : 0, x3 : x3_val,x4 : x4_val}),z,check=False)[0]
    minn = min(minn,kas1_val)
    print(f"kasus 1 : {kas1_val}" )
else:
        print("solusi tidak feasible")


#kasus 2 x1 = x3 = 0
x2_val = sp.solve(eq1.subs({x1 : 0,x3 : 0}),x2)[0]
x4_val = sp.solve(eq2.subs({x1 : 0,x2 : x2_val}),x4)[0]
if x2_val >=0  and x4_val >= 0 :
    kas2_val = sp.solve(eq0.subs({x1 : 0,x2 : x2_val, x3 : 0,x4 : x4_val}),z,check=False)[0]
    minn = min(minn,kas2_val)
    print(f"kasus 2 : {kas2_val}" )
else:
        print("solusi tidak feasible")


#kasus 3 x1 = x4 = 0
x2_val = sp.solve(eq2.subs({x1 : 0,x4 : 0}),x2)[0]
x3_val = sp.solve(eq1.subs({x1 : 0,x2 : x2_val}),x3)[0]
if x2_val >=0 and x3_val >= 0 :
    kas3_val = sp.solve(eq0.subs({x1 : 0,x2 : x2_val, x3 : x3_val,x4 : 0}),z,check=False)[0]
    minn = min(minn,kas3_val)
    print(f"kasus 3 : {kas3_val}" )
else:
        print("solusi tidak feasible")

#kasus 4 x2 = x3 = 0
x1_val = sp.solve(eq1.subs({x2 : 0,x3 : 0}),x1)[0]
x4_val = sp.solve(eq2.subs({x1 : x1_val,x2 : 0}),x4)[0]
if x1_val >=0 and x4_val >= 0 :
    kas4_val = sp.solve(eq0.subs({x1 : x1_val,x2 : 0, x3 : x3_val,x4 : 0}),z,check=False)[0]
    minn = min(minn,kas4_val)
    print(f"kasus 4 : {kas4_val}" )
else:
        print("solusi tidak feasible")

#kasus 5 x2 = x4 = 0
x1_val = sp.solve(eq2.subs({x2 : 0,x4 : 0}),x1)[0]
x3_val = sp.solve(eq1.subs({x1 : x1_val,x2 : 0}),x3)[0]
if x1_val >=0 and x3_val >= 0 :
    kas5_val = sp.solve(eq0.subs({x1 : x1_val,x2 : 0, x3 : x3_val,x4 : 0}),z,check=False)[0]
    minn = min(minn,kas5_val)
    print(f"kasus 5 : {kas5_val}" )
else:
        print("solusi tidak feasible")


#kasus 6 x3 = x4 = 0
x1_val = sp.solve(eq1.subs({x3 : 0}),x1)[0]
x2_val = sp.solve(eq2.subs({x4 :0, x1 :x1_val}),x2)[0]
x1_val = sp.solve(eq1.subs({x3 : 0,x2 :x2_val}),x1)[0]

if x1_val >=0 and x2_val >= 0 :
    kas6_val = sp.solve(eq0.subs({x1 : x1_val,x2 :x2_val, x3 : 0 ,x4 : 0}),z,check=False)[0]
    minn = min(minn,kas6_val)
    print(f"kasus 6 : {kas6_val}" )
else:
        print("solusi tidak feasible")


print(f"maksimal value yang dapat diperolwh adalah : {minn}")

