# Read me - DE

*Convertido de: Read me - DE.PDF*

---


## Página 1


Leuescher Integralrechner -- README
Jeanette Tabea Leue
2025-09-27
1 Überblick
Diese HTML-Anwendung berechnet bestimmte Integrale direkt im Browser. Keine
Installation, keine externen Bibliotheken. Zwei Modi: Classic (Trigonometrie in
Radiant) und Tick (laufzeitlich π-frei).
2 Eingaben
• Integrand f(x): sin, cos, tan, exp, log (ln), sqrt, abs, min, max, pow
.
• Grenzen a, b.
• Methode: Adaptive Simpson (Toleranz), Simpson (gerades N), Trapez
(Schritte N).
• Modus: classic oder tick. Im Tick-Modus ist ein Vollkreis in N Ticks
tabelliert.
3 Technik
• Quadratur: Trapezregel, Simpson, Adaptive Simpson.
• Tick-Trig: einmalige LUT-Initialisierung; zur Laufzeit π-frei via Lookup.
• Läuft vollständig lokal, transparent und reproduzierbar.
4 Beispiele
• exp(-x*x) auf [-2,2] (adaptive).
• sin(x)/(1+x*x) auf [0,8] (Simpson, Tick-Modus).
• sqrt(1-x*x) auf [0,1] (adaptive).
5 Hinweis
1


## Página 2


Entwickelt von mir,Jeanette Tabea Leue. Bitte zitieren als: Leue, J. T. (2025):
Leuescher Integralrechner.
2
