# ============================================================
#  DER PRIMZEIT–RIEMANN–OSZILLATOR – PSF-KONFORME NUMERIK
#  Autorin: Jeanette Leue
#  Version: 3.0 – Operator nach PSF + Plots
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh
from scipy.stats import linregress

# ------------------------------------------------------------
# 1. PRIMZAHLEN UND PRIMZEIT (EXAKT WIE IN DER THEORIE)
# ------------------------------------------------------------

def get_primes_upto(n_max):
    """
    Einfaches Sieb bis n_max.
    """
    is_prime = np.ones(n_max + 1, dtype=bool)
    is_prime[0:2] = False
    for i in range(2, int(n_max ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i * i:n_max+1:i] = False
    return np.nonzero(is_prime)[0]


def first_primes(N):
    """
    Liefert die ersten N Primzahlen.
    Heuristische Obergrenze: x ~ N log N.
    """
    if N <= 6:
        return np.array([2, 3, 5, 7, 11, 13][:N])

    n_max = int(N * (np.log(N) + np.log(np.log(N)) + 3))
    while True:
        primes = get_primes_upto(n_max)
        if len(primes) >= N:
            return primes[:N]
        n_max *= 2


def primetime(N):
    """
    Primzeit t_k = sum_{j<=k} log p_j
    mit p_j der j-ten Primzahl.
    """
    p = first_primes(N)
    t = np.cumsum(np.log(p))
    return t, p


# ------------------------------------------------------------
# 2. POTENTIAL V(t) – HIER KANNST DU DEINE FORMEL EINSETZEN
# ------------------------------------------------------------

def potential_V(t):
    """
    Platzhalter für V(t) = '(t) + (t).

    Aktuell: einfache Version, analog zu deiner alten Numerik:
        V(t) = 1 / log(t + 2)
    """
    return 1.0 / np.log(t + 2.0)


# ------------------------------------------------------------
# 3. KERNOPERATOR H0 – DISKRETE SYMMETRISCHE DIFFERENZ
# ------------------------------------------------------------

def build_H0_psf(t):
    """
    Diskrete Version von

        (H0 f)(t_k) = -i * (f(t_{k+1}) - f(t_{k-1})) / (t_{k+1} - t_{k-1})
                      + V(t_k) f(t_k)

    mit einfacher Randbehandlung für k=0 und k=N-1.
    """
    N = len(t)
    H0 = np.zeros((N, N), dtype=complex)
    V = potential_V(t)

    # Innenpunkte: symmetrische Differenz
    for k in range(1, N-1):
        dt = t[k+1] - t[k-1]
        H0[k, k+1] += -1j / dt
        H0[k, k-1] +=  1j / dt
        H0[k, k]   += V[k]

    # Randpunkte: nur Potential (oder später einseitige Ableitung, wenn du willst)
    H0[0, 0]   += V[0]
    H0[-1, -1] += V[-1]

    return H0


# ------------------------------------------------------------
# 4. ARITHMETISCHER STÖRTERM Hr – _p WIE IN DEINER NUMERIK
# ------------------------------------------------------------

def alpha_p(p, coupling, sigma):
    """
    Deine numerische Wahl:

        _p = coupling * log(p) * p^(-1/2 - sigma)
    """
    return coupling * (np.log(p) * p**(-0.5 - sigma))


def build_Hr_psf(t, primes, coupling=0.5, sigma=0.0, P_max=None):
    """
    Diskrete Version von

        (Hr f)(t_k) = _p _p f(t_k - log p)

    mit Trunkation auf p <= P_max (numerisch notwendig).
    """
    N = len(t)
    Hr = np.zeros((N, N), dtype=complex)

    if P_max is not None:
        primes = primes[primes <= P_max]

    for p in primes:
        a_p = alpha_p(p, coupling, sigma)
        log_p = np.log(p)

        for k in range(N):
            target = t[k] - log_p
            if target <= t[0]:
                continue
            j = np.searchsorted(t, target)
            if 0 < j < N:
                # symmetrische Kopplung als diskrete Realisierung
                Hr[k, j] += a_p
                Hr[j, k] += a_p

    return Hr


# ------------------------------------------------------------
# 5. GESAMTOPERATOR H = H0 + Hr (PSF-KONFORMER KERN)
# ------------------------------------------------------------

def build_operator_psf(N=200, coupling=0.5, sigma=0.0, P_max=None):
    """
    Baut den diskreten Operator H^{(N,P_max)}:

      - t_k = _{j<=k} log p_j
      - H0: symmetrische Differenz + V(t_k)
      - Hr: _p _p f(t_k - log p) mit _p wie in deiner Numerik.
    """
    t, primes = primetime(N)
    H0 = build_H0_psf(t)
    Hr = build_Hr_psf(t, primes, coupling=coupling, sigma=sigma, P_max=P_max)
    H = H0 + Hr
    return H, t, primes


# ------------------------------------------------------------
# 6. GUE-STATISTIK
# ------------------------------------------------------------

def gue_statistics_test(N=300, coupling=0.6, sigma=0.0, P_max=None):
    H, t, primes = build_operator_psf(N=N, coupling=coupling, sigma=sigma, P_max=P_max)
    evals, _ = eigh(H)
    lambdas = np.sort(evals.real)

    spacings = np.diff(lambdas)
    spacings = spacings[spacings > 0]
    s = spacings / np.mean(spacings)

    x = np.linspace(0, 4, 400)
    p_gue = (32 / np.pi**2) * x**2 * np.exp(-4 * x**2 / np.pi)
    p_poisson = np.exp(-x)

    plt.figure(figsize=(10, 6))
    plt.hist(s, bins=30, density=True, alpha=0.6, color='navy', label='Simulation')
    plt.plot(x, p_gue, 'r-', lw=2.5, label='GUE (Wigner-Surmise)')
    plt.plot(x, p_poisson, 'g--', lw=1.5, label='Poisson (Regularität)')
    plt.title("GUE-Statistik des Primzeit–Riemann–Oszillators (PSF-konform)")
    plt.xlabel("Normierter Abstand s")
    plt.ylabel("Wahrscheinlichkeitsdichte P(s)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("gue_statistics_psf.png")
    print("Plot gespeichert: gue_statistics_psf.png")


# ------------------------------------------------------------
# 7. WELLENFUNKTION
# ------------------------------------------------------------

def visualize_eigenfunction(N=400, coupling=0.6, sigma=0.0, idx=10, P_max=None):
    H, t, primes = build_operator_psf(N=N, coupling=coupling, sigma=sigma, P_max=P_max)
    evals, evecs = eigh(H)
    psi = evecs[:, idx]
    density = np.abs(psi)**2

    plt.figure(figsize=(12, 6))
    plt.plot(t, density, color="darkcyan", lw=1.5, label=r"$|\psi(t)|^2$")
    plt.fill_between(t, density, color="cyan", alpha=0.2)

    # Markiere ein paar log(p)-Positionen zur Orientierung
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        t_mark = np.log(p)  # du kannst auch kumulativ markieren, wenn du willst
        plt.axvline(t_mark, color="red", linestyle=":", alpha=0.3)

    plt.title("Eigenfunktion – arithmetische Quanten-Narben (PSF-konform)")
    plt.xlabel("Primzeit t")
    plt.ylabel("Aufenthaltswahrscheinlichkeit")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("wavefunction_scars_psf.png")
    print("Plot gespeichert: wavefunction_scars_psf.png")


# ------------------------------------------------------------
# 8. STABILITÄT DES SPEKTRUMS
# ------------------------------------------------------------

def stability_test(N=150, P_max=None):
    sigmas = [0.2, 0.1, 0.05, 0.01]
    plt.figure(figsize=(10, 6))
    colors = plt.cm.viridis(np.linspace(0, 1, len(sigmas)))

    for c, sigma in zip(colors, sigmas):
        H, t, primes = build_operator_psf(N=N, coupling=0.6*(1 - sigma), sigma=sigma, P_max=P_max)
        evals, _ = eigh(H)
        plt.plot(np.arange(40), evals.real[:40],
                 color=c, marker='o', ms=3, linestyle='-',
                 label=rf"$\sigma={sigma}$")

    plt.title("Stabilität des Spektrums (  0, PSF-konform)")
    plt.xlabel("Index n")
    plt.ylabel(r"Eigenwert $\lambda_n$")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("stability_sigma_psf.png")
    print("Plot gespeichert: stability_sigma_psf.png")


# ------------------------------------------------------------
# 9. GESAMTSPEKTRUM
# ------------------------------------------------------------

def spectrum_plot(N=300, coupling=0.5, sigma=0.0, P_max=None):
    H, t, primes = build_operator_psf(N=N, coupling=coupling, sigma=sigma, P_max=P_max)
    evals, _ = eigh(H)

    plt.figure(figsize=(10, 5))
    plt.plot(evals.real, '.', color="blue", alpha=0.7)
    plt.title("Gesamtspektrum des Operators H (PSF-konform)")
    plt.xlabel("Index n")
    plt.ylabel(r"Eigenwert $\lambda_n$")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("spectrum_H_psf.png")
    print("Plot gespeichert: spectrum_H_psf.png")


# ------------------------------------------------------------
# 10. NUMERISCHER „BEWEISBLOCK“ (EVIDENZ)
# ------------------------------------------------------------

def proof_check(P_max=None):
    """
    Numerische Evidenz:
      1) Stabilität der ersten Eigenwerte bei   0
      2) Vergleich der niedrigsten Eigenwerte mit den ersten Zeta-Nullstellen
         nach linearer Kalibrierung (kein formaler Beweis).
    """
    true_zeros = np.array([
        14.1347, 21.0220, 25.0108, 30.4248, 32.9350,
        37.5861, 40.9187, 43.3270, 48.0051, 49.7738
    ])

    sigmas = [0.2, 0.1, 0.05, 0.01, 0.001]
    results = []

    for s in sigmas:
        H, t, primes = build_operator_psf(N=200, coupling=0.5, sigma=s, P_max=P_max)
        evals = np.sort(np.linalg.eigvalsh(H))
        results.append(evals[:10])

    results = np.array(results)
    best_evals = results[-1]

    # Lineare Fits zur Skalenanpassung
    idx = np.arange(len(true_zeros))
    slope_true, intercept_true, *_ = linregress(idx, true_zeros)
    sim_subset = best_evals[:len(true_zeros)]
    slope_sim, intercept_sim, *_ = linregress(idx, sim_subset)

    calibrated_sim = (sim_subset - intercept_sim) * (slope_true / slope_sim) + intercept_true

    plt.figure(figsize=(12, 10))

    # (1) Stabilität
    plt.subplot(2, 1, 1)
    for i in range(5):
        plt.plot(sigmas, results[:, i], 'o-', label=rf'$\lambda_{{{i+1}}}$')
    plt.gca().invert_xaxis()
    plt.title("Evidenz 1: Stabilität (  0, PSF-konform)")
    plt.xlabel(r"$\sigma$")
    plt.ylabel("Eigenwerte")
    plt.legend()
    plt.grid(True)

    # (2) Vergleich Zeta-Nullstellen vs. Resonanzen
    plt.subplot(2, 1, 2)
    n = np.arange(1, 11)
    plt.scatter(n, true_zeros, c='red', s=100, marker='x', label='Zeta-Nullstellen')
    plt.scatter(n, calibrated_sim, c='blue', alpha=0.7, label='Resonanzen (skaliert)')
    for i in range(10):
        plt.plot([n[i], n[i]],
                 [true_zeros[i], calibrated_sim[i]], 'k--', alpha=0.3)

    plt.title("Evidenz 2: Kein offensichtliches Geister-Spektrum (PSF-konform)")
    plt.xlabel("Index n")
    plt.ylabel(r"$\gamma_n, \lambda_n$")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("proof_check_psf.png")
    print("Plot gespeichert: proof_check_psf.png")


# ------------------------------------------------------------
# 11. HAUPTPROGRAMM
# ------------------------------------------------------------

if __name__ == "__main__":
    print("Starte PSF-konforme Simulationen für 'Der Primzeit–Riemann–Oszillator' ...\n")

    # P_max kannst du variieren, z.B. 200, 500, None (alle Primzahlen, die in primetime(N) vorkommen)
    P_max = None

    gue_statistics_test(P_max=P_max)
    visualize_eigenfunction(P_max=P_max)
    stability_test(P_max=P_max)
    spectrum_plot(P_max=P_max)
    proof_check(P_max=P_max)

    print("\nAlle 5 Simulationen abgeschlossen.")
    print("Ergebnisse gespeichert im selben Ordner wie dieses Skript.\n")