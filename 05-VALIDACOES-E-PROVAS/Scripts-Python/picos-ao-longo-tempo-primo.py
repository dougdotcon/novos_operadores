import math

# ~30 imaginäre Teile der ersten nichttrivialen Riemann-Nullstellen
zeros = [
    14.134725141, 21.022039639, 25.010857580,
    30.424876125, 32.935061588, 37.586178159,
    40.918719012, 43.327073281, 48.005150881,
    49.773832478, 52.970321478, 56.446247697,
    59.347044003, 60.831778525, 65.112544048,
    67.079810529, 69.546401711, 72.067157674,
    75.704690699, 77.144840069, 79.337375020,
    82.910380854, 84.735492981, 87.425274613,
    88.809111208, 92.491899271, 94.651344041,
    95.870634228, 98.831194218, 101.317851006,
]

def is_prime(n: int) -> bool:
    """Nur Hilfsfunktion zum Prüfen – nicht Teil der Theorie."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(n ** 0.5) + 1
    for k in range(3, r, 2):
        if n % k == 0:
            return False
    return True

def generate_primes(limit_count: int):
    """Erzeuge die ersten limit_count Primzahlen (einfach, nicht optimal)."""
    primes = []
    n = 2
    while len(primes) < limit_count:
        if is_prime(n):
            primes.append(n)
        n += 1
    return primes

def build_primetime(primes):
    """Primzeit: t_n = Sum_{k<=n} log p_k."""
    t_list = []
    s = 0.0
    for p in primes:
        s += math.log(p)
        t_list.append(s)
    return t_list

def Z_of_t(t: float) -> float:
    """Interferenzsignal Z(t) aus den Nullstellen auf der Primzeit-Achse."""
    s = 0.0
    for g in zeros:
        s += math.cos(g * t)
    return s

# -----------------------------------
# Parameter
# -----------------------------------
N_PRIMES = 150   # wie viele Primzahlen wir für die Primzeit nehmen
TOP_K = 40       # wie viele stärkste Zitter-Peaks wir anzeigen

# 1. Primzahlen & Primzeit
primes = generate_primes(N_PRIMES)
primetime = build_primetime(primes)

# 2. Z(t_n) entlang der Primzeit berechnen
values = []  # (Index n, prime p_n, t_n, Z(t_n))

for idx, (p, t) in enumerate(zip(primes, primetime), start=1):
    z = Z_of_t(t)
    values.append((idx, p, t, z))

# 3. Nach |Z| sortieren -> stärkstes Zittern zuerst
values.sort(key=lambda e: -abs(e[3]))

print(f"Top-{TOP_K} Zitter-Peaks entlang der Primzeit (n, p_n, t_n, Z(t_n)):\n")
for idx, p, t, z in values[:TOP_K]:
    print(f"n = {idx:3d},  p_n = {p:4d},  t_n ≈ {t:8.3f},  Z(t_n) ≈ {z:8.3f}")