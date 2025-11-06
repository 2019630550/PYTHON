import numpy as np

def gram_schmidt(vectors):
    vectors = np.array(vectors, dtype=float)
    n = len(vectors)
    ortonormales = []

    for i in range(n):
        v = vectors[i]
        for e in ortonormales:
            v -= np.dot(v, e) * e
        v = v / np.linalg.norm(v)
        ortonormales.append(v)
    return np.array(ortonormales)

u1 = [1, 1, 0]
u2 = [1, 0, 1]
u3 = [0, 1, 1]

vectors = [u1, u2, u3]
resultado = gram_schmidt(vectors)

print("Vectores ortonormales:")
for i, e in enumerate(resultado, 1):
    print(f"e{i} =  {e}")