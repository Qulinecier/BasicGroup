# Basic Group

## Contents

- Cyclic Group: $C_n$
    - element of cyclic group require two parameters: $i$ and $n$, where $i$ represent the index on the generator and $n$ is the order of $C$
    - eg. $C_n = \{g^0, g^1, \dots, g^{n-1}\}$

- Symmetric Group: $S_n$
    - element of $S_n$ require two parameters: the cycles and order $n$ of the group
    - eg. $(1~2)(3~4) \in S_5$ are written as `Sym([(1, 2), (3, 4)], 5)`
    - If `cycles = False`, the element can be also written as a form of bijection from `[1, ..., n]` to a new list.

- Dihedral Group: $D_{2n}$
    - element of $D_n$ require two parameters: $n$ from $D_{2n}$ and element written in rotations and symmetry
    - eg. $\rho^2\sigma\in D_{8}$ is `Dihedral("rrs", 4)`
- Direct Product: $G \times H$
    - support groups above
- Automorphism: generates Aut, Inn from a group written in a list.

## Install
In wins,
```powershell
python -m pip install .\BasicGroup\
```
or
```cmd
pip install BasicGroup
```