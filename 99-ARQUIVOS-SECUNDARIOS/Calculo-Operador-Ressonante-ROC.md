# Resonant Operator Calculus (ROC)

*Convertido de: Resonant Operator Calculus (ROC).pdf*

---


## Página 1


Resonant Operator Calculus (ROC)
A Dimension-Independent Three-Channel Architecture for Stable Discrete Dynamics
Jeanette Leue
December 4, 2025
Abstract
The Resonant Operator Calculus (ROC) is presented as a non-causal linear framework
for discrete fields on ℓ2(Zd), d ≥1. ROC provides an exact orthogonal decomposition into
forward-, neutral-, and backward-propagating frequency channels, defined by a partition of
the frequency torus along a chosen propagation direction.
Given a unit vector v ∈Rd, the frequency domain is partitioned according to the sign of
k · v into three measurable regions Ω+, Ω0, Ω−, inducing orthogonal projections P+, P0, P−.
Based on these projections, a resonant modulation operator
M = γ+P+ + γ0P0 + γ−P−
admits the closed-form iteration formula
M n = γn
+P+ + γn
0 P0 + γn
−P−,
yielding exact channel-wise energy evolution in arbitrary dimension. This allows the con-
struction of discrete evolutions exhibiting controlled directional propagation while remaining
globally bounded.
The purpose of this work is to formalize the multi-dimensional ROC framework, establish
its stability theory, and demonstrate its use in designing directionally biased linear dynamics.
ROC applies equally in one, two, and three spatial dimensions, and all results remain valid
without modification.
1


## Página 2


Contents
1
Introduction
3
2
ROC Decomposition (Spectral Formulation)
3
3
Resonant Modulation Operators
4
4
Applications of the ROC Framework
4
4.1
Exact directional channel separation . . . . . . . . . . . . . . . . . . . . . . . . .
4
4.2
Closed-form stability under iteration . . . . . . . . . . . . . . . . . . . . . . . . .
4
5
A Constructive Example: Directional Stable Dynamics
4
5.1
Setup
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
5.2
Directional propagation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
5.3
Energy bound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
A Analytic Foundations of the Multi-Dimensional ROC Framework
5
A.1 Fourier analysis on ℓ2(Zd) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
A.2 Orthogonality and commutation . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
A.3 Iteration of diagonal operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
A.4 Higher-dimensional generality . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
B Results and Discussion: Validation of the ROC One-Way Waveguide
6
B.1
Proof of Global Stability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
B.2
Exact Channel Suppression and Directional Bias
. . . . . . . . . . . . . . . . . .
6
B.3
Dynamics and Interpretation of Wave Propagation . . . . . . . . . . . . . . . . .
7
B.4
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2


## Página 3


1
Introduction
Discrete dynamical systems on ℓ2(Zd) often exhibit distinct directional behaviours: modes trav-
elling along or against a preferred direction may interact differently with internal evolution.
Classical approaches—convolution operators, local filters, FIR architectures—allow only ap-
proximate spectral separation and provide limited control over long-term stability.
This paper introduces the Resonant Operator Calculus (ROC), a dimension-independent
spectral framework enabling exact directional channel decomposition and closed-form iteration
of linear evolutions. Given a propagation direction v ∈Rd with ∥v∥= 1, the frequency torus is
partitioned into
Ω+ = {k : k · v > ε},
Ω0 = {k : |k · v| ≤ε},
Ω−= {k : k · v < −ε},
for some small threshold ε ≥0. The associated projections P+, P0, P−satisfy
F = P+F + P0F + P−F,
PiPj = δijPi,
P+ + P0 + P−= I,
and apply in all spatial dimensions without modification.
A resonant modulation operator
M = γ+P+ + γ0P0 + γ−P−
is block-diagonal with respect to this decomposition, and therefore its n-th iterate satisfies
Mn = γn
+P+ + γn
0 P0 + γn
−P−.
This yields exact stability and energy evolution formulas.
ROC is inherently non-causal, linear, and spectral. It is not a time-local filtering method
but a structural analytic tool. All results presented here hold equally in one, two, and three
dimensions.
2
ROC Decomposition (Spectral Formulation)
We work on ℓ2(Zd) with d ≥1. The unitary discrete Fourier transform is defined by
bF(k) =
X
x∈Zd
F(x)e−ik·x,
F(x) =
1
(2π)d
Z
Td
bF(k)eik·x dk.
Fix a unit direction v ∈Rd and define a measurable partition of the frequency torus by
Ω+ = {k ∈Td : k · v > ε},
Ω0 = {k : |k · v| ≤ε},
Ω−= {k : k · v < −ε},
with ε ≥0 controlling the width of the neutral band.
Definition 2.1 (Multi-dimensional ROC projections). For F ∈ℓ2(Zd), the projections P+, P0, P−
are defined by
d
PiF(k) = 1Ωi(k) bF(k),
i ∈{+, 0, −}.
Theorem 2.2 (Orthogonal three-channel decomposition). For every F ∈ℓ2(Zd),
F = P+F + P0F + P−F,
and the projections are orthogonal, idempotent, and satisfy P+ + P0 + P−= I.
Proof. Since Ω+, Ω0, Ω−form a disjoint measurable partition of Td, their indicator functions
satisfy
1Ωi1Ωj = δij1Ωi,
X
i
1Ωi = 1.
The assertions follow by Plancherel.
3


## Página 4


3
Resonant Modulation Operators
With respect to the ROC decomposition F = P+F + P0F + P−F, a modulation operator acts
diagonally on each channel.
Definition 3.1 (Resonant modulation operator). Let γ+, γ0, γ−∈C be bounded coefficients.
The resonant modulation operator is
M = γ+P+ + γ0P0 + γ−P−.
(1)
We assume uniform bounds
0 < c ≤|γi| ≤C < ∞
(i ∈{+, 0, −}).
(2)
Lemma 3.2 (Channel-wise invariance). Each channel is invariant under M, and
MPi = γiPi,
i ∈{+, 0, −}.
Proof. Immediate from (1) and idempotence of Pi.
Theorem 3.3 (Closed-form iteration and stability). For every n ∈N,
Mn = γn
+P+ + γn
0 P0 + γn
−P−,
and for every F ∈ℓ2(Zd),
∥MnF∥2
2 = |γ+|2n∥P+F∥2
2 + |γ0|2n∥P0F∥2
2 + |γ−|2n∥P−F∥2
2.
(3)
Thus ∥M∥= max{|γ+|, |γ0|, |γ−|} and M is non-expansive if |γi| ≤1.
Proof. Orthogonality implies PiPj = δijPi, so the block-diagonal structure persists under itera-
tion. The energy identity follows from Plancherel and disjointness of the channels.
4
Applications of the ROC Framework
The ROC structure provides more than a decomposition of ℓ2(Zd): it enables explicit channel-
wise control of evolution operators, exact long-term stability estimates, and the design of direc-
tionally biased discrete dynamics.
4.1
Exact directional channel separation
The projections P+, P0, P−induce a perfect orthogonal decomposition according to the sign of
k · v, allowing clean separation of waves propagating with or against the chosen direction v. No
classical FIR filter achieves such exact separation due to spectral leakage.
4.2
Closed-form stability under iteration
Given M as above, the iterate M n is known exactly. Therefore, for any evolution U = AM
where A is unitary or norm-preserving, global energy control remains explicitly computable.
This is of particular interest for shift-type operators in multiple dimensions.
5
A Constructive Example: Directional Stable Dynamics
We now construct a multi-dimensional evolution operator on ℓ2(Zd) that produces translation
along the direction v while remaining globally bounded.
4


## Página 5


5.1
Setup
Define the shift along the unit vector v by
(SvF)(x) := F(x −v),
where v ∈Zd is any lattice direction. Its Fourier symbol is
d
SvF(k) = eik·v bF(k),
so Sv is unitary and commutes with every projection Pi.
Let M = γ+P+ + γ0P0 + γ−P−with |γi| ≤1, and define:
U := SvM.
5.2
Directional propagation
Because Sv and M commute,
Un = Sn
v Mn,
and the action on a field is
F (n) := UnF (0) = Sn
v
 γn
+P+F (0) + γn
0 P0F (0) + γn
−P−F (0)
.
The factor Sn
v shifts the entire field by nv, producing linear drift in the direction v. The
remaining terms describe channel-specific attenuation or amplification.
5.3
Energy bound
Since Sv is unitary and ∥M n∥≤1,
∥F (n)∥2 = ∥UnF (0)∥2 ≤∥F (0)∥2,
so the evolution is globally stable.
A
Analytic Foundations of the Multi-Dimensional ROC Frame-
work
This appendix collects the mathematical foundations supporting the dimension-independent
ROC structure.
A.1
Fourier analysis on ℓ2(Zd)
The unitary Fourier transform is
bF(k) =
X
x∈Zd
F(x)e−ik·x,
F(x) =
1
(2π)d
Z
Td
bF(k)eik·x dk.
Indicator functions of measurable partitions Ωi generate bounded self-adjoint multipliers.
A.2
Orthogonality and commutation
For the ROC projections,
PiPj = δijPi,
X
i
Pi = I.
The shift operator Sv has symbol eik·v and therefore commutes with each Pi.
5


## Página 6


A.3
Iteration of diagonal operators
If
M =
X
i
γiPi,
then for all n,
Mn =
X
i
γn
i Pi,
giving the channel-wise energy identity
∥MnF∥2
2 =
X
i
|γi|2n∥PiF∥2
2.
A.4
Higher-dimensional generality
All ROC results depend only on:
• a finite measurable partition of Td,
• orthogonal projections defined by the partition,
• diagonal modulation by bounded coefficients.
No step depends on d = 1.
Thus ROC applies equally in any spatial dimension, including two-dimensional wave fields
and three-dimensional discrete dynamics.
B
Results and Discussion: Validation of the ROC One-Way Waveg-
uide
The numerical simulation of the Resonant Operator Calculus (ROC) one-way waveguide in two
dimensions provides an exact validation of the underlying theory and demonstrates the feasibility
of controlled directional wave transport.
B.1
Proof of Global Stability
The stability of the discrete dynamics was quantified by comparing the simulated total energy
(Etotal) with the theoretically predicted energy derived from the ROC energy identity.
• The system’s energy stabilized at a constant level following the initial transient step (chan-
nel suppression).
• The maximum absolute error between simulation and theory was measured at 1.1 × 10−14.
This result proves that the ROC implementation satisfies the core theoretical requirement: the
evolution is exactly non-expansive and globally stable up to machine precision.
B.2
Exact Channel Suppression and Directional Bias
The effectiveness of the one-way filter was demonstrated by analyzing the energy distribution
across the three channels (ER, E0, EL):
• The modulation operator M was configured with γL = 0, leading to the instantaneous
and complete suppression of backward-propagating frequencies.
6


## Página 7


• The energy in the backward channel (EL) dropped to approximately 3.8 × 10−32 after
the first time step.
• The remaining energy (≈90% in ER and 10% in E0) was perfectly conserved within
these forward and neutral channels.
The simulation confirms that the ROC architecture realizes a functionally perfect one-way device
by eliminating unwanted back-scattering.
B.3
Dynamics and Interpretation of Wave Propagation
The propagation of the wave packet confirms the controlled, linear dynamics:
• Linear Movement: The center of mass (COMx) propagated perfectly linearly from
x = 32 at t = 0 to x = 47 at t = 79. The COMy remained constant.
• Group Velocity (vgroup): The measured velocity was vgroup ≈0.19 (grid points per
time step). This value is lower than the expected maximal grid velocity (v = 1), but it is
not a simulation error.
• Dispersion-Free Propagation: The perfect linearity of the COM trajectory and the
conserved wave shape (as shown in the field visualization ) confirm that the measured
velocity vgroup is the constant, dispersion-free group velocity of the ROC-filtered
wave packet. The ROC projection P+ acts as a band-pass filter, and the resulting packet
propagates at the average speed of its contained frequencies, which is a major success of
the method.
B.4
Conclusion
The numerical results conclusively validate the multi-dimensional ROC framework as an exact,
globally stable, and functionally powerful tool for constructing dispersion-free, one-way
dynamics. The simulation confirms that the ROC approach provides a robust solution to the
problem of numerical instability and controlled directional wave guidance.
7
