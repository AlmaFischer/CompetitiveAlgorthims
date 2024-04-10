class vec:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x = x2 - x1
        self.y = y2 - y1
        self.z = z2 - z1
def dot_prod(v1, v2):
    print((v1.x * v2.x) + (v1.y * v2.y) + (v1.z * v2.z))
    return (v1.x * v2.x) + (v1.y * v2.y) + (v1.z * v2.z)
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
ab = vec(*a, *b)
bc = vec(*b, *c)
cd = vec(*c, *d)
if dot_prod(ab,bc)==0 and dot_prod(bc,cd)==0:
    print("Valid")
else:
    print("Invalid")

