import numpy as np
import csv
import os
import argparse

# ---------------------------
# Fourier grid / masks
# ---------------------------
def fftfreq2d(N):
    """Return kx, ky arrays for NxN periodic grid (values in [-0.5,0.5))."""
    fx = np.fft.fftfreq(N)
    fy = fx.copy()
    kx, ky = np.meshgrid(fx, fy, indexing='xy')
    return kx, ky

def make_sector_masks(N, eps=1e-12):
    """Create boolean masks for right-moving (kx>eps), left-moving (kx<-eps), and zero sector."""
    kx, ky = fftfreq2d(N)
    mask_R_bool = (kx > eps)
    mask_L_bool = (kx < -eps)
    mask_0_bool = np.logical_not(np.logical_or(mask_R_bool, mask_L_bool))
    # convert to complex masks so they multiply directly with complex FFT arrays
    mask_R = mask_R_bool.astype(np.complex128)
    mask_0 = mask_0_bool.astype(np.complex128)
    mask_L = mask_L_bool.astype(np.complex128)
    return mask_R, mask_0, mask_L

# ---------------------------
# Projections and modulation
# ---------------------------
def proj_channels_2d(u2d, mask_R, mask_0, mask_L):
    """Project field onto R, 0, L channels (time-domain outputs)."""
    U = np.fft.fft2(u2d)
    UR = U * mask_R
    U0 = U * mask_0
    UL = U * mask_L
    return np.fft.ifft2(UR), np.fft.ifft2(U0), np.fft.ifft2(UL)

def apply_modulation_2d(u2d, gammaR, gamma0, gammaL, mask_R, mask_0, mask_L):
    """Apply M = gammaR*P_R + gamma0*P_0 + gammaL*P_L in Fourier domain."""
    U = np.fft.fft2(u2d)
    U_mod = gammaR * (U * mask_R) + gamma0 * (U * mask_0) + gammaL * (U * mask_L)
    return np.fft.ifft2(U_mod)

# ---------------------------
# Shift operator (right in x-direction)
# ---------------------------
def shift_right_2d(u2d, shift=1):
    """Circular (periodic) right shift along x-axis (axis=1)."""
    return np.roll(u2d, shift, axis=1)

# ---------------------------
# Initial field creators
# ---------------------------
def create_initial_field(N, init_type="gaussian", sigma=1.0, kx0=0.0):
    """Create NxN initial complex field. init_type in {'gaussian','impulse','plane_wave'}."""
    field = np.zeros((N, N), dtype=np.complex128)
    cx = cy = N // 2
    if init_type == "gaussian":
        x = np.arange(N); y = np.arange(N)
        X, Y = np.meshgrid(x, y, indexing='xy')
        gauss = np.exp(-(((X - cx)**2 + (Y - cy)**2) / (2.0 * sigma**2)))
        field = gauss.astype(np.complex128)
    elif init_type == "impulse":
        field[cx, cy] = 1.0 + 0j
    elif init_type == "plane_wave":
        x = np.arange(N); y = np.arange(N)
        X, Y = np.meshgrid(x, y, indexing='xy')
        field = np.exp(2j * np.pi * (kx0 * X / N)).astype(np.complex128)
    else:
        raise ValueError(f"Unknown init_type: {init_type}")
    return field
    # --- PART 2: simulation, saving, CLI (copy this after part 1) ---

# ---------------------------
# Diagnostics
# ---------------------------
def center_of_mass_energy_weighted_2d(field):
    """Energy-weighted center-of-mass (periodic) -> returns (com_x, com_y) in [0,N)."""
    N = field.shape[0]
    weights = np.abs(field)**2
    total = weights.sum()
    if total < 1e-15:
        return float('nan'), float('nan')
    idx = np.arange(N)
    X, Y = np.meshgrid(idx, idx, indexing='xy')
    phx = np.sum(weights * np.exp(2j * np.pi * X / N))
    phy = np.sum(weights * np.exp(2j * np.pi * Y / N))
    com_x = (np.angle(phx) * N / (2.0 * np.pi)) % N
    com_y = (np.angle(phy) * N / (2.0 * np.pi)) % N
    return com_x, com_y

# ---------------------------
# Save helpers
# ---------------------------
def save_csv_field(history_real, outdir, prefix="field"):
    """Save history array shape (T,N,N) as flattened rows: timestep, v0...v_{N^2-1}."""
    os.makedirs(outdir, exist_ok=True)
    fn = os.path.join(outdir, f"{prefix}_history.csv")
    T, N, _ = history_real.shape
    with open(fn, "w", newline="") as f:
        w = csv.writer(f)
        header = ["timestep"] + [f"v{i}" for i in range(N*N)]
        w.writerow(header)
        for t in range(T):
            row = history_real[t].reshape(-1).tolist()
            w.writerow([t] + row)
    return fn

def save_csv_energies(energies_R, energies_0, energies_L, energies_total, com_x, com_y, outdir):
    os.makedirs(outdir, exist_ok=True)
    fn = os.path.join(outdir, "energies.csv")
    with open(fn, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["timestep","E_R","E_0","E_L","E_total","COM_x","COM_y"])
        for t in range(len(energies_total)):
            w.writerow([t,
                        float(energies_R[t]), float(energies_0[t]), float(energies_L[t]),
                        float(energies_total[t]), float(com_x[t]), float(com_y[t])])
    return fn

# ---------------------------
# Core runner
# ---------------------------
def run_simulation(N=64, steps=80, gammaR=1.0, gamma0=1.0, gammaL=0.0,
                   init_type="gaussian", sigma=1.0, kx0=0.0, eps=1e-12):
    """Run the 2D ROC one-way waveguide simulation and return results dict."""
    # masks
    mask_R, mask_0, mask_L = make_sector_masks(N, eps=eps)

    # initial field
    field = create_initial_field(N, init_type=init_type, sigma=sigma, kx0=kx0)

    # storage
    history_real = np.zeros((steps, N, N), dtype=float)
    energies_R = np.zeros(steps, dtype=float)
    energies_0 = np.zeros(steps, dtype=float)
    energies_L = np.zeros(steps, dtype=float)
    energies_total = np.zeros(steps, dtype=float)
    com_x = np.zeros(steps, dtype=float)
    com_y = np.zeros(steps, dtype=float)

    current = field.copy()

    for n in range(steps):
        history_real[n,:,:] = np.real(current)
        rR, r0, rL = proj_channels_2d(current, mask_R, mask_0, mask_L)
        eR = np.linalg.norm(rR)**2
        e0 = np.linalg.norm(r0)**2
        eL = np.linalg.norm(rL)**2
        etot = np.linalg.norm(current)**2
        energies_R[n] = eR
        energies_0[n] = e0
        energies_L[n] = eL
        energies_total[n] = etot
        cx, cy = center_of_mass_energy_weighted_2d(current)
        com_x[n] = cx; com_y[n] = cy

        # advance: U = S M
        modulated = apply_modulation_2d(current, gammaR, gamma0, gammaL, mask_R, mask_0, mask_L)
        current = shift_right_2d(modulated, shift=1)

    # predicted total energies from initial channel split under M^n (applies to seed)
    rR0, r00, rL0 = proj_channels_2d(field, mask_R, mask_0, mask_L)
    E_R0 = np.linalg.norm(rR0)**2
    E_00 = np.linalg.norm(r00)**2
    E_L0 = np.linalg.norm(rL0)**2
    predicted = np.zeros(steps, dtype=float)
    for n in range(steps):
        predicted[n] = (abs(gammaR)**2)**n * E_R0 + (abs(gamma0)**2)**n * E_00 + (abs(gammaL)**2)**n * E_L0

    return {
        'history_real': history_real,
        'energies_R': energies_R,
        'energies_0': energies_0,
        'energies_L': energies_L,
        'energies_total': energies_total,
        'com_x': com_x,
        'com_y': com_y,
        'predicted': predicted,
        'initial_field': field,
        'masks': (mask_R, mask_0, mask_L)
    }

# ---------------------------
# Save all results and metadata
# ---------------------------
def save_results(results: dict, outdir: str):
    os.makedirs(outdir, exist_ok=True)
    field_file = save_csv_field(results['history_real'], outdir, prefix="field")
    energies_file = save_csv_energies(results['energies_R'], results['energies_0'],
                                      results['energies_L'], results['energies_total'],
                                      results['com_x'], results['com_y'], outdir)
    pred_file = os.path.join(outdir, "predicted_total.csv")
    with open(pred_file, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["timestep","predicted_total_energy"])
        for i, val in enumerate(results['predicted']):
            w.writerow([i, float(val)])

    # metadata
    meta_file = os.path.join(outdir, "metadata.txt")
    with open(meta_file, "w") as f:
        f.write("ROC One-Way Waveguide Simulation\n")
        f.write("="*40 + "\n")
        f.write(f"Grid size (N): {results['history_real'].shape[1]}\n")
        f.write(f"Timesteps: {results['history_real'].shape[0]}\n")
        f.write(f"Initial total energy: {np.linalg.norm(results['initial_field'])**2}\n")
        f.write(f"Final total energy: {results['energies_total'][-1]}\n")
        # conservation error
        pred = results['predicted']
        meas = results['energies_total']
        max_err = float(np.max(np.abs(meas - pred)))
        f.write(f"Max energy conservation abs error: {max_err}\n")

    return {'field_file': field_file, 'energies_file': energies_file, 'predicted_file': pred_file, 'metadata_file': meta_file}

# ---------------------------
# CLI main
# ---------------------------
def main():
    parser = argparse.ArgumentParser(description="ROC one-way waveguide (2D) - numeric demo (no plotting)")
    parser.add_argument("--N", type=int, default=64, help="grid size (NxN)")
    parser.add_argument("--steps", type=int, default=80, help="timesteps")
    parser.add_argument("--gammaR", type=float, default=1.0, help="gamma right")
    parser.add_argument("--gamma0", type=float, default=1.0, help="gamma zero")
    parser.add_argument("--gammaL", type=float, default=0.0, help="gamma left (set 0 to block left)")
    parser.add_argument("--init", type=str, default="gaussian", choices=["gaussian","impulse","plane_wave"], help="initial field type")
    parser.add_argument("--sigma", type=float, default=1.0, help="Gaussian width")
    parser.add_argument("--kx0", type=float, default=0.0, help="plane-wave kx0 (if plane_wave)")
    parser.add_argument("--eps", type=float, default=1e-12, help="frequency threshold for sector masks")
    parser.add_argument("--outdir", type=str, default="roc_oneway_out", help="output directory")
    args = parser.parse_args()

    print("="*60)
    print("ROC One-Way Waveguide Simulation (2D)")
    print(f"Grid: {args.N}x{args.N}, steps: {args.steps}")
    print(f"gammaR={args.gammaR}, gamma0={args.gamma0}, gammaL={args.gammaL}")
    print(f"init={args.init}, sigma={args.sigma}, kx0={args.kx0}")
    print("="*60)

    results = run_simulation(N=args.N, steps=args.steps,
                             gammaR=args.gammaR, gamma0=args.gamma0, gammaL=args.gammaL,
                             init_type=args.init, sigma=args.sigma, kx0=args.kx0, eps=args.eps)

    saved = save_results(results, args.outdir)

    # validation
    pred = results['predicted']
    meas = results['energies_total']
    max_err = float(np.max(np.abs(meas - pred)))
    print("Files written:")
    for k,v in saved.items():
        print(f" - {k}: {v}")
    print(f"Max abs error (measured_total - predicted_total) = {max_err:.3e}")
    if max_err < 1e-8:
        print("Energy identity verified (within numerical precision).")
    else:
        print("Energy identity mismatch (check settings). Max err =", max_err)

if __name__ == "__main__":
    main()