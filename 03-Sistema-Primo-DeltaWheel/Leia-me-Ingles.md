# Read me - ENG

*Convertido de: Read me - ENG.PDF*

---


## Página 1


Leue Prime System -- README
Jeanette Tabea Leue
2025-09-27
1 Overview
This project provides two HTML applications implementing the Leue Prime
System. Both programs run directly in the browser, without installation or
external libraries. All prime number calculations are based only on the Δ
-operator with wheel residues. No sieves, no precomputation, no Miller--Rabin
tests.
2 PrimeSystemApp_DeltaWheel.html
2.1 Content
Calculator for primes in the Δ-operator system.
2.2 Functions
• Input as value (e.g. 5) or as index (p[3] = 5).
• Next / previous / nearest prime.
• Prime index arithmetic:
– A⊕B=p[n(A)+n(B)]
– A⊖B=p[n(A)-n(B)]
– A⊗B=p[n(A)⋅n(B)]
– A⊘B=p[⌊n(A)/n(B)⌋]
– Ak=p[(n(A))k]
• Search for next prime ≥N.
2.3 Technique
Trial division along wheel gaps (30, 210) up to
n. No sieves, no caches, no
probabilistic tests.
1


## Página 2


3 PrimScanLive.html
3.1 Content
Live scanner for primes with real-time display of π(x) and θ(x).
3.2 Functions
• Parallel scanning using multiple web workers.
• Live display: prime count, Chebyshev sum, last found prime.
• Choice between wheel 30 and wheel 210.
3.3 Technique
Uses the same Δ-operator, stateless, purely generative.
4 About
Developed by myself, Jeanette Tabea Leue. These applications demonstrate for
the
ﬁrst
time
a
working
implementation
of
the
Δ-operator:
deterministic,
generative, and fully transparent in source code.
Please cite as:
Leue, J. T. (2025): Leue Prime System -- Δ-Operator Apps. Zenodo. DOI: _
____
2
