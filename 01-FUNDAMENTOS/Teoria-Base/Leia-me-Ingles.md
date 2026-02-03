# Read me - ENG

*Convertido de: Read me - ENG.PDF*

---


## Página 1


Leue Integral Calculator -- README
Jeanette Tabea Leue
2025-09-27
1 Overview
This
HTML
app
evaluates
deﬁnite
integrals
directly
in
the
browser.
No
installation, no external libraries. Two modes: Classic (radian trig) and Tick (π
-free at runtime).
2 Inputs
• Integrand f(x) supports: sin, cos, tan, exp, log (ln), sqrt, abs, min,
max, pow.
• Bounds a, b.
• Method: Adaptive Simpson (tolerance), Simpson (even N), Trapezoid
(steps N).
• Mode: classic or tick. In tick-mode one full turn is tabulated into N
ticks.
3 Technique
• Quadrature: trapezoid, Simpson, adaptive Simpson.
• Tick trig: single LUT initialization; π-free lookup at runtime.
• Fully local, transparent, and reproducible.
4 Examples
• exp(-x*x) on [-2,2] (adaptive).
• sin(x)/(1+x*x) on [0,8] (Simpson, tick-mode).
• sqrt(1-x*x) on [0,1] (adaptive).
5 Note
1


## Página 2


Developed by myself, Jeanette Tabea Leue. Please cite as: Leue, J. T. (2025):
Leue Integral Calculator.
2
