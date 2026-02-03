# Rock-Wave-3D-Full.py
import numpy as np
import csv
import os
import argparse
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from scipy.ndimage import gaussian_filter

# ---------------------------
# 1. ROC Kernfunktionen (3D)
# ---------------------------
def fftfreq3d(N):
    """Return kx, ky, kz arrays for NxNxN periodic grid."""
    fx = np.fft.fftfreq(N)
    fy = fx.copy()
    fz = fx.copy()
    kx, ky, kz = np.meshgrid(fx, fy, fz, indexing='ij')
    return kx, ky, kz

def make_sector_masks_3d(N, v=(1,0,0), eps=1e-12):
    """ROC Partitionierung: Ω₊ = {k : k·v > ε}, Ω₀, Ω₋."""
    kx, ky, kz = fftfreq3d(N)
    k_dot_v = kx*v[0] + ky*v[1] + kz*v[2]
    
    mask_R = (k_dot_v > eps).astype(np.complex128)      # Vorwärts
    mask_L = (k_dot_v < -eps).astype(np.complex128)     # Rückwärts
    mask_0 = (~(mask_R.astype(bool) | mask_L.astype(bool))).astype(np.complex128)  # Neutral
    
    return mask_R, mask_0, mask_L

def proj_channels_3d(u3d, mask_R, mask_0, mask_L):
    """Theorem 2.2: F = P₊F + P₀F + P₋F"""
    U = np.fft.fftn(u3d)
    UR = np.fft.ifftn(U * mask_R)
    U0 = np.fft.ifftn(U * mask_0)
    UL = np.fft.ifftn(U * mask_L)
    return UR, U0, UL

def apply_modulation_3d(u3d, gammaR, gamma0, gammaL, mask_R, mask_0, mask_L):
    """Definition 3.1: M = γ₊P₊ + γ₀P₀ + γ₋P₋"""
    U = np.fft.fftn(u3d)
    U_mod = gammaR*(U*mask_R) + gamma0*(U*mask_0) + gammaL*(U*mask_L)
    return np.fft.ifftn(U_mod)

def shift_3d(u3d, v=(1,0,0), shift_amount=1):
    """Shift S_v entlang Richtung v."""
    shift_vec = [int(round(shift_amount * vi)) for vi in v]
    return np.roll(u3d, shift=shift_vec, axis=(0,1,2))

# ---------------------------
# 2. Plot-Funktionen für 3D
# ---------------------------
def plot_3d_slice(field_3d, title="3D Field Slice", save_path=None):
    """Plot XY-, XZ-, YZ-Schnitte durch 3D-Feld."""
    N = field_3d.shape[0]
    center = N // 2
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # XY-Schnitt (z = Mitte)
    im1 = axes[0,0].imshow(field_3d[:,:,center].real, cmap='RdBu', 
                          vmin=-np.abs(field_3d).max(), vmax=np.abs(field_3d).max())
    axes[0,0].set_title(f'XY-Schnitt (z={center})')
    axes[0,0].set_xlabel('x'); axes[0,0].set_ylabel('y')
    plt.colorbar(im1, ax=axes[0,0])
    
    # XZ-Schnitt (y = Mitte)
    im2 = axes[0,1].imshow(field_3d[:,center,:].real, cmap='RdBu',
                          vmin=-np.abs(field_3d).max(), vmax=np.abs(field_3d).max())
    axes[0,1].set_title(f'XZ-Schnitt (y={center})')
    axes[0,1].set_xlabel('z'); axes[0,1].set_ylabel('x')
    plt.colorbar(im2, ax=axes[0,1])
    
    # YZ-Schnitt (x = Mitte)
    im3 = axes[1,0].imshow(field_3d[center,:,:].real, cmap='RdBu',
                          vmin=-np.abs(field_3d).max(), vmax=np.abs(field_3d).max())
    axes[1,0].set_title(f'YZ-Schnitt (x={center})')
    axes[1,0].set_xlabel('z'); axes[1,0].set_ylabel('y')
    plt.colorbar(im3, ax=axes[1,0])
    
    # 3D Isosurface (einfache Darstellung)
    axes[1,1].remove()
    ax3d = fig.add_subplot(2, 2, 4, projection='3d')
    
    # Extrahiere Isosurface bei 50% des Maximums
    threshold = 0.5 * np.abs(field_3d).max()
    X, Y, Z = np.meshgrid(range(N), range(N), range(N), indexing='ij')
    
    mask = np.abs(field_3d.real) > threshold
    if mask.any():
        ax3d.scatter(X[mask], Y[mask], Z[mask], c=field_3d.real[mask], 
                    cmap='RdBu', s=1, alpha=0.6)
    
    ax3d.set_title('3D Isosurface (>50% max)')
    ax3d.set_xlabel('x'); ax3d.set_ylabel('y'); ax3d.set_zlabel('z')
    
    plt.suptitle(title, fontsize=14)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()

def plot_energy_evolution_3d(results, save_path=None):
    """Plot Energieverlauf und Schwerpunkt-Bewegung."""
    steps = len(results['energies_total'])
    
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    
    # 1. Energie-Kanäle
    axes[0,0].plot(results['energies_R'], 'r-', label='Vorwärts (R)', linewidth=2)
    axes[0,0].plot(results['energies_0'], 'g-', label='Neutral (0)', linewidth=2)
    axes[0,0].plot(results['energies_L'], 'b-', label='Rückwärts (L)', linewidth=2)
    axes[0,0].set_xlabel('Zeitschritt')
    axes[0,0].set_ylabel('Energie')
    axes[0,0].set_title('Energie pro Richtungskanal')
    axes[0,0].legend()
    axes[0,0].grid(True, alpha=0.3)
    
    # 2. Gesamtenergie vs Vorhersage
    axes[0,1].plot(results['energies_total'], 'k-', label='Simulation', linewidth=3)
    axes[0,1].plot(results['predicted'], 'r--', label='ROC Theorie', linewidth=2)
    axes[0,1].set_xlabel('Zeitschritt')
    axes[0,1].set_ylabel('Gesamtenergie')
    axes[0,1].set_title('Energieerhaltung: Simulation vs Theorie')
    axes[0,1].legend()
    axes[0,1].grid(True, alpha=0.3)
    
    # 3. Fehler
    error = results['energies_total'] - results['predicted']
    axes[0,2].plot(np.abs(error), 'r-', linewidth=2)
    axes[0,2].set_xlabel('Zeitschritt')
    axes[0,2].set_ylabel('Absoluter Fehler')
    axes[0,2].set_title(f'Energie-Fehler (max: {np.abs(error).max():.2e})')
    axes[0,2].grid(True, alpha=0.3)
    axes[0,2].set_yscale('log')
    
    # 4. Schwerpunkt-Bewegung 3D
    axes[1,0].plot(results['com_x'], 'b-', label='COM_x', linewidth=2)
    axes[1,0].plot(results['com_y'], 'r-', label='COM_y', linewidth=2)
    axes[1,0].plot(results['com_z'], 'g-', label='COM_z', linewidth=2)
    axes[1,0].set_xlabel('Zeitschritt')
    axes[1,0].set_ylabel('Schwerpunkt (Pixel)')
    axes[1,0].set_title('Schwerpunkt-Bewegung')
    axes[1,0].legend()
    axes[1,0].grid(True, alpha=0.3)
    
    # 5. 3D Trajektorie des Schwerpunkts
    ax3d = fig.add_subplot(2, 3, 5, projection='3d')
    ax3d.plot(results['com_x'], results['com_y'], results['com_z'], 
             'b-', linewidth=2, alpha=0.7)
    ax3d.scatter(results['com_x'][0], results['com_y'][0], results['com_z'][0], 
                c='green', s=100, label='Start', marker='o')
    ax3d.scatter(results['com_x'][-1], results['com_y'][-1], results['com_z'][-1], 
                c='red', s=100, label='Ende', marker='s')
    ax3d.set_xlabel('x'); ax3d.set_ylabel('y'); ax3d.set_zlabel('z')
    ax3d.set_title('3D Trajektorie des Schwerpunkts')
    ax3d.legend()
    
    # 6. Energieverteilung (Start vs Ende)
    axes[1,2].bar([0, 1, 2], 
                  [results['energies_R'][0], results['energies_0'][0], results['energies_L'][0]],
                  width=0.4, label='Anfang', alpha=0.7, color=['red', 'green', 'blue'])
    axes[1,2].bar([0.4, 1.4, 2.4], 
                  [results['energies_R'][-1], results['energies_0'][-1], results['energies_L'][-1]],
                  width=0.4, label='Ende', alpha=0.7, color=['red', 'green', 'blue'])
    axes[1,2].set_xticks([0.2, 1.2, 2.2])
    axes[1,2].set_xticklabels(['Vorwärts', 'Neutral', 'Rückwärts'])
    axes[1,2].set_ylabel('Energie')
    axes[1,2].set_title('Energieverteilung: Anfang vs Ende')
    axes[1,2].legend()
    
    plt.suptitle('ROC 3D Simulation - Analyse', fontsize=16)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()

def create_3d_animation(results, save_path=None, fps=10):
    """Erstelle Animation der 3D-Wellenausbreitung."""
    history = results['history_real']
    N = history.shape[1]
    center = N // 2
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Initial plots
    im1 = axes[0].imshow(history[0,:,:,center], cmap='RdBu',
                        vmin=-np.abs(history).max(), vmax=np.abs(history).max())
    axes[0].set_title(f'XY-Schnitt (z={center})')
    plt.colorbar(im1, ax=axes[0])
    
    im2 = axes[1].imshow(history[0,:,center,:], cmap='RdBu',
                        vmin=-np.abs(history).max(), vmax=np.abs(history).max())
    axes[1].set_title(f'XZ-Schnitt (y={center})')
    plt.colorbar(im2, ax=axes[1])
    
    im3 = axes[2].imshow(history[0,center,:,:], cmap='RdBu',
                        vmin=-np.abs(history).max(), vmax=np.abs(history).max())
    axes[2].set_title(f'YZ-Schnitt (x={center})')
    plt.colorbar(im3, ax=axes[2])
    
    def update(frame):
        im1.set_array(history[frame,:,:,center])
        im2.set_array(history[frame,:,center,:])
        im3.set_array(history[frame,center,:,:])
        
        axes[0].set_title(f'XY (z={center}) - Schritt {frame}')
        axes[1].set_title(f'XZ (y={center}) - Schritt {frame}')
        axes[2].set_title(f'YZ (x={center}) - Schritt {frame}')
        
        return im1, im2, im3
    
    anim = FuncAnimation(fig, update, frames=len(history), 
                        interval=1000/fps, blit=False)
    
    if save_path:
        anim.save(save_path, writer='ffmpeg', fps=fps)
        print(f"Animation gespeichert: {save_path}")
    
    plt.close()
    return anim

def plot_frequency_spectrum_3d(results, save_path=None):
    """Visualisiere Frequenzspektrum und ROC-Masken."""
    mask_R, mask_0, mask_L = results['masks']
    N = mask_R.shape[0]
    
    # Frequenzachsen
    kx = np.fft.fftshift(np.fft.fftfreq(N))
    ky = kx.copy()
    kz = kx.copy()
    
    # Extrahiere Schnitte
    center = N // 2
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # ROC-Masken visualisieren
    axes[0,0].imshow(mask_R.real[:,:,center], cmap='Reds', vmin=0, vmax=1)
    axes[0,0].set_title('ROC Maske: Vorwärts (R)')
    axes[0,0].set_xlabel('kx'); axes[0,0].set_ylabel('ky')
    
    axes[0,1].imshow(mask_0.real[:,:,center], cmap='Greens', vmin=0, vmax=1)
    axes[0,1].set_title('ROC Maske: Neutral (0)')
    axes[0,1].set_xlabel('kx'); axes[0,1].set_ylabel('ky')
    
    axes[0,2].imshow(mask_L.real[:,:,center], cmap='Blues', vmin=0, vmax=1)
    axes[0,2].set_title('ROC Maske: Rückwärts (L)')
    axes[0,2].set_xlabel('kx'); axes[0,2].set_ylabel('ky')
    
    # Frequenzspektrum des Start- und Endfelds
    fft_start = np.fft.fftshift(np.fft.fftn(results['initial_field']))
    fft_end = np.fft.fftshift(np.fft.fftn(
        results['history_real'][-1] + 1j*0  # Realteil als komplex
    ))
    
    axes[1,0].imshow(np.log10(np.abs(fft_start[:,:,center]) + 1e-10), 
                    cmap='viridis', aspect='auto')
    axes[1,0].set_title('Start: Log|FFT| (xy-Ebene)')
    axes[1,0].set_xlabel('kx'); axes[1,0].set_ylabel('ky')
    
    axes[1,1].imshow(np.log10(np.abs(fft_end[:,:,center]) + 1e-10), 
                    cmap='viridis', aspect='auto')
    axes[1,1].set_title('Ende: Log|FFT| (xy-Ebene)')
    axes[1,1].set_xlabel('kx'); axes[1,1].set_ylabel('ky')
    
    # Frequenz-Schnitt entlang Ausbreitungsrichtung
    kx_vals = kx
    if results['v'][0] != 0:  # Hauptrichtung in x
        fft_slice_start = fft_start[:, center, center]
        fft_slice_end = fft_end[:, center, center]
        axes[1,2].plot(kx_vals, np.abs(fft_slice_start), 'b-', label='Start', linewidth=2)
        axes[1,2].plot(kx_vals, np.abs(fft_slice_end), 'r-', label='Ende', linewidth=2)
        axes[1,2].set_xlabel('kx (Hauptrichtung)')
    axes[1,2].set_ylabel('|FFT|')
    axes[1,2].set_title('Frequenzspektrum (Schnitt)')
    axes[1,2].legend()
    axes[1,2].grid(True, alpha=0.3)
    
    plt.suptitle('ROC 3D Frequenzanalyse', fontsize=16)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()

# ---------------------------
# 3. Haupt-Simulation mit Plots
# ---------------------------
def run_and_plot_3d(N=32, steps=50, gammaR=1.0, gamma0=1.0, gammaL=0.0,
                    v=(1,0,0), init_type="gaussian", sigma=1.0, 
                    k0=(0,0,0), eps=1e-12, outdir="roc_3d_results"):
    """Führe 3D Simulation durch und erstelle alle Plots."""
    
    os.makedirs(outdir, exist_ok=True)
    
    print("="*60)
    print("ROC 3D Simulation mit Visualisierung")
    print(f"Grid: {N}³, Steps: {steps}, Direction: {v}")
    print("="*60)
    
    # 1. ROC-Masken
    mask_R, mask_0, mask_L = make_sector_masks_3d(N, v=v, eps=eps)
    
    # 2. Initialfeld
    x = y = z = np.arange(N)
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    cx = cy = cz = N // 2
    
    if init_type == "gaussian":
        field = np.exp(-(((X-cx)**2 + (Y-cy)**2 + (Z-cz)**2) / (2*sigma**2)))
        field = field.astype(np.complex128)
    elif init_type == "impulse":
        field = np.zeros((N, N, N), dtype=np.complex128)
        field[cx, cy, cz] = 1.0
    else:  # plane_wave
        field = np.exp(2j*np.pi*(k0[0]*X/N + k0[1]*Y/N + k0[2]*Z/N))
    
    # 3. Simulation
    history = np.zeros((steps, N, N, N), dtype=float)
    energies_R = np.zeros(steps)
    energies_0 = np.zeros(steps)
    energies_L = np.zeros(steps)
    energies_total = np.zeros(steps)
    com_x, com_y, com_z = np.zeros(steps), np.zeros(steps), np.zeros(steps)
    
    current = field.copy()
    
    for n in range(steps):
        history[n] = current.real
        
        # Energien
        UR, U0, UL = proj_channels_3d(current, mask_R, mask_0, mask_L)
        energies_R[n] = np.linalg.norm(UR.ravel())**2
        energies_0[n] = np.linalg.norm(U0.ravel())**2
        energies_L[n] = np.linalg.norm(UL.ravel())**2
        energies_total[n] = np.linalg.norm(current.ravel())**2
        
        # Schwerpunkt
        weights = np.abs(current)**2
        total = weights.sum()
        if total > 1e-15:
            com_x[n] = np.sum(weights * X) / total
            com_y[n] = np.sum(weights * Y) / total
            com_z[n] = np.sum(weights * Z) / total
        
        # Evolution: U = S_v M
        modulated = apply_modulation_3d(current, gammaR, gamma0, gammaL, 
                                       mask_R, mask_0, mask_L)
        current = shift_3d(modulated, v=v)
    
    # 4. Vorhersage (Theorem 3.3)
    UR0, U00, UL0 = proj_channels_3d(field, mask_R, mask_0, mask_L)
    E_R0 = np.linalg.norm(UR0.ravel())**2
    E_00 = np.linalg.norm(U00.ravel())**2
    E_L0 = np.linalg.norm(UL0.ravel())**2
    
    predicted = np.array([(abs(gammaR)**2)**n * E_R0 + 
                         (abs(gamma0)**2)**n * E_00 + 
                         (abs(gammaL)**2)**n * E_L0 
                         for n in range(steps)])
    
    results = {
        'history_real': history,
        'energies_R': energies_R, 'energies_0': energies_0, 'energies_L': energies_L,
        'energies_total': energies_total, 'predicted': predicted,
        'com_x': com_x, 'com_y': com_y, 'com_z': com_z,
        'initial_field': field, 'masks': (mask_R, mask_0, mask_L),
        'v': v, 'N': N, 'steps': steps
    }
    
    # 5. Plots erstellen
    print("\nErstelle Visualisierungen...")
    
    # Start- und Endzustand
    plot_3d_slice(field.real, title="3D Startzustand", 
                  save_path=os.path.join(outdir, "start_state.png"))
    plot_3d_slice(history[-1], title="3D Endzustand", 
                  save_path=os.path.join(outdir, "end_state.png"))
    
    # Energieanalyse
    plot_energy_evolution_3d(results, 
                            save_path=os.path.join(outdir, "energy_analysis.png"))
    
    # Frequenzanalyse
    plot_frequency_spectrum_3d(results, 
                              save_path=os.path.join(outdir, "frequency_analysis.png"))
    
    # Animation
    anim_path = os.path.join(outdir, "wave_propagation.mp4")
    create_3d_animation(results, save_path=anim_path, fps=5)
    
    # 6. Metadaten speichern
    with open(os.path.join(outdir, "simulation_info.txt"), "w") as f:
        f.write(f"ROC 3D Simulation Results\n")
        f.write(f"N: {N}\n")
        f.write(f"Steps: {steps}\n")
        f.write(f"Direction v: {v}\n")
        f.write(f"γ_R, γ_0, γ_L: {gammaR}, {gamma0}, {gammaL}\n")
        f.write(f"Initial type: {init_type}\n")
        f.write(f"\nEnergy Conservation:\n")
        f.write(f"  Max error: {np.abs(energies_total - predicted).max():.2e}\n")
        f.write(f"  Mean error: {np.abs(energies_total - predicted).mean():.2e}\n")
        f.write(f"\nFinal Energies:\n")
        f.write(f"  Forward (R): {energies_R[-1]:.6e}\n")
        f.write(f"  Neutral (0): {energies_0[-1]:.6e}\n")
        f.write(f"  Backward (L): {energies_L[-1]:.6e}\n")
        f.write(f"  Total: {energies_total[-1]:.6e}\n")
    
    print("\n" + "="*60)
    print("Alle Plots gespeichert in:", outdir)
    print("Dateien:")
    print(f"  start_state.png        - 3D Startzustand")
    print(f"  end_state.png          - 3D Endzustand")
    print(f"  energy_analysis.png    - Energieverlauf")
    print(f"  frequency_analysis.png - Frequenzspektrum")
    print(f"  wave_propagation.mp4   - Animierte Ausbreitung")
    print(f"  simulation_info.txt    - Parameter und Ergebnisse")
    print("="*60)
    
    return results

# ---------------------------
# 4. Kommandozeilen-Schnittstelle
# ---------------------------
def main():
    parser = argparse.ArgumentParser(description="ROC 3D Simulation mit vollständiger Visualisierung")
    
    parser.add_argument("--N", type=int, default=32, help="Grid size (N×N×N)")
    parser.add_argument("--steps", type=int, default=50, help="Number of timesteps")
    parser.add_argument("--gammaR", type=float, default=1.0, help="γ for forward channel")
    parser.add_argument("--gamma0", type=float, default=1.0, help="γ for neutral channel")
    parser.add_argument("--gammaL", type=float, default=0.0, help="γ for backward channel")
    
    parser.add_argument("--vx", type=float, default=1.0, help="x-direction")
    parser.add_argument("--vy", type=float, default=0.0, help="y-direction")
    parser.add_argument("--vz", type=float, default=0.0, help="z-direction")
    
    parser.add_argument("--init", type=str, default="gaussian", 
                        choices=["gaussian", "impulse", "plane_wave"])
    parser.add_argument("--sigma", type=float, default=1.0, help="Gaussian width")
    parser.add_argument("--kx", type=float, default=0.0, help="Plane wave kx")
    parser.add_argument("--ky", type=float, default=0.0, help="Plane wave ky")
    parser.add_argument("--kz", type=float, default=0.0, help="Plane wave kz")
    
    parser.add_argument("--eps", type=float, default=1e-12, help="Frequency threshold ε")
    parser.add_argument("--outdir", type=str, default="roc_3d_full_results", 
                       help="Output directory")
    
    args = parser.parse_args()
    
    # Normiere Richtungsvektor
    v_norm = np.sqrt(args.vx**2 + args.vy**2 + args.vz**2)
    v = (args.vx/v_norm, args.vy/v_norm, args.vz/v_norm) if v_norm > 0 else (1,0,0)
    
    # Führe Simulation mit Plots aus
    results = run_and_plot_3d(
        N=args.N, steps=args.steps,
        gammaR=args.gammaR, gamma0=args.gamma0, gammaL=args.gammaL,
        v=v,
        init_type=args.init, sigma=args.sigma, k0=(args.kx, args.ky, args.kz),
        eps=args.eps,
        outdir=args.outdir
    )

if __name__ == "__main__":
    main()