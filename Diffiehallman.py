def is_prim_root(g, p):
    residues = set(pow(g, i, p) for i in range(1, p))
    return len(residues) == p - 1
def find_prim_root(p):
    for g in range(2, p):
        if is_prim_root(g, p):
            return g
p=int(input("Enter a prime number: "))
g=find_prim_root(p)
if g is not None:
    print(f"The primitive root of {p} is: {g}")
else:
    print(f"No primitive root found for {p}.")
ap=int(input("enter the private key of a :"))
bp=int(input("enter the private key of b :"))
pua=(g**ap)%p
print("Pulbic key of A is :",pua)
pub=(g**bp)%p
print("Pulbic key of B is :",pub)
sa=(pub*ap)%p #sb=(pua*bp)%p
print("Secret key is :",sa)