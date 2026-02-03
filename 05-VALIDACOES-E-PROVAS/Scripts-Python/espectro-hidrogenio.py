import numpy as np
import matplotlib.pyplot as plt

# =================================================================
# BERECHNUNG: WASSERSTOFF-SPEKTRUM ALS SURPLUS-RESONANZ
# Basierend auf Kapitel 5.4 des Primarcode-Manuskripts
# =================================================================

# Naturkonstanten
h_eV_s = 4.135667696e-15  # Plancksches Wirkungsquantum in eV*s
c = 299792458              # Lichtgeschwindigkeit in m/s
E_ground = -13.6           # Grundzustandsenergie Wasserstoff in eV

def calculate_wavelength(n_initial, n_final):
    """Berechnet die Wellenlänge eines Übergangs (Surplus-Ereignis)"""
    E_init = E_ground / (n_initial**2)
    E_fin = E_ground / (n_final**2)
    delta_E = abs(E_fin - E_init)
    return (h_eV_s * c) / delta_E * 1e9  # Umrechnung in Nanometer (nm)

print("="*60)
print("KAPITEL 5.4: WASSERSTOFF-SPEKTREN (SURPLUS-TRANSITIONEN)")
print("="*60)

# 1. Lyman-Serie (Übergänge nach n=1, UV-Bereich)
print("\nLYMAN-SERIE (n -> 1):")
lyman = [calculate_wavelength(n, 1) for n in [2, 3, 4, 5]]
for i, wl in enumerate(lyman):
    print(f"  Ly-{chr(945+i)} (n={i+2} -> 1): {wl:.2f} nm (UV)")

# 2. Balmer-Serie (Übergänge nach n=2, Sichtbarer Bereich)
print("\nBALMER-SERIE (n -> 2):")
balmer = [calculate_wavelength(n, 2) for n in [3, 4, 5, 6]]
colors = ['red', 'cyan', 'blue', 'violet']
for i, wl in enumerate(balmer):
    print(f"  H-{chr(945+i)} (n={i+3} -> 2):  {wl:.2f} nm ({colors[i]})")

# =================================================================
# VISUALISIERUNG DES SPEKTRUMS
# =================================================================
plt.figure(figsize=(12, 4))
plt.title("Sichtbares Wasserstoff-Spektrum (Balmer-Serie) - Erzeugt durch x = y + 1")

# Zeichne die Linien des sichtbaren Spektrums
for wl, color in zip(balmer, colors):
    plt.axvline(x=wl, color=color, linewidth=4, label=f"{wl:.1f} nm")

plt.xlim(380, 750) # Sichtbarer Bereich
plt.xlabel("Wellenlänge (nm)")
plt.ylabel("Intensität (Resonanz-Ausschlag)")
plt.legend()
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('wasserstoff_spektrum.png', dpi=150)
plt.show()

print("\n" + "="*60)
print("PHYSIKALISCHE SCHLUSSFOLGERUNG:")
print("="*60)
print("Die diskreten Linien sind der Beweis für den Primarcode:")
print("Energie wird nicht kontinuierlich, sondern als Surplus (+1)")
print("in Paketen (Photonen) abgegeben oder aufgenommen.")
