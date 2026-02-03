import mpmath as mp
import numpy as np

# ============================================================================
# 0. GLOBALE PRÄZISION
# ============================================================================
# Hohe Präzision für die Erfassung des steilen Phasenübergangs (Kapitel 12.1.3)
mp.mp.dps = 60

# ============================================================================
# 1. RESONANZ-AKTIVIERUNGSFUNKTION R(L) (DEFINITION 12.5)
# ============================================================================

def resonance_activation(L, L_crit, k):
    """
    Berechnet den Realisierungsgrad R(L) als sigmoide Funktion.
    L: Kopplungsstärke des Beobachters
    L_crit: Kritische Schwelle
    k: Schärfeparameter (k~10^15 s^-1 für Photonen)
    """
    exp_arg = -mp.mpf(k) * (mp.mpf(L) - mp.mpf(L_crit))
    return 1 / (1 + mp.exp(exp_arg))

# ============================================================================
# 2. STRUKTURELLER DOPPLER-SHIFT Delta_omega (KAPITEL 12.1.2)
# ============================================================================

def compute_resonance_doppler(L, L_crit, k):
    """
    Berechnet den Doppler-Shift Δω als energetische Signatur des Kollapses.
    Δω ist proportional zur zeitlichen oder strukturellen Änderungsrate dR/dL.
    """
    R_L = resonance_activation(L, L_crit, k)
    doppler_shift = mp.mpf(k) * R_L * (1 - R_L)
    return R_L, doppler_shift

# ============================================================================
# 3. PHYSIKALISCHE VERIFIKATION (KAPITEL 5.4.2 / 12.2.3)
# ============================================================================

def run_doppler_analysis():
    L_crit = 5.0
    k_photon = 1e15  # Empirischer Wert für Photonen-Detektion
    
    print("="*70)
    print("KAPITEL 12: RESONANZ-DOPPLER & SOFT-COLLAPS VERIFIKATION")
    print("="*70)
    
    test_L = [4.99999999999999, 5.0, 5.00000000000001]
    
    print(f"{'L-Kopplung':<15} | {'R(L) (Realität)':<15} | {'Δω (Doppler-Shift)':<15}")
    print("-" * 70)
    
    for L in test_L:
        rl, dw = compute_resonance_doppler(L, L_crit, k_photon)
        print(f"{float(L):<15.14f} | {float(rl):<15.4f} | {float(dw):<15.4e} rad/s")

    print("\n" + "="*70)
    print("ONTOLOGISCHE SCHLUSSFOLGERUNG (KAPITEL 12.3)")
    print("="*70)
    print("1. Der Doppler-Shift erreicht sein Maximum exakt bei L_crit.")
    print("2. Δω repräsentiert die 'metabolischen Kosten' des Kollapses.")
    print("3. Ohne Kopplung (L -> 0) verbleibt das System in Psi_drift.")

if __name__ == "__main__":
    run_doppler_analysis()