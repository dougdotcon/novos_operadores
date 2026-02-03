# Read me - DE

*Convertido de: Read me - DE.PDF*

---


## Página 1


Leuesches Primzahlsystem -- README
Jeanette Tabea Leue
2025-09-27
1 Überblick
Dieses Projekt enthält zwei HTML-Programme, die das Leuesche Primzahlsystem
im Browser zeigen. Beide Dateien laufen direkt, ohne Installation und ohne
Server.
2 PrimeSystemApp_DeltaWheel.html
2.1 Inhalt
Rechner für Primzahlen im Δ-Operator-System.
2.2 Funktionen
• Eingabe als Zahl (z.B. 5) oder Index (p[3] = 5).
• Nächste oder vorherige Primzahl.
• Nächstgelegene Primzahl.
• Index-Arithmetik:
– A⊕B=p[n(A)+n(B)]
– A⊖B=p[n(A)-n(B)]
– A⊗B=p[n(A)⋅n(B)]
– A⊘B=p[⌊n(A)/n(B)⌋]
– Ak=p[(n(A))k]
• Suche: nächste Primzahl ≥N.
2.3 Technik
• Primzahlerkennung nur über Δ-Operator mit Wheel (30, 210).
• Keine Siebe, keine Vorberechnungen, kein Miller--Rabin.
• Division nur bis
n entlang der Restklassen.
1


## Página 2


3 PrimScanLive.html
3.1 Inhalt
Live-Scanner für Primzahlen mit Anzeige von π(x) und θ(x).
3.2 Funktionen
• Mehrere Web-Worker prüfen Zahlenblöcke parallel.
• Live-Anzeige: Anzahl Primzahlen, Summen, letzte Primzahl.
• Wahl zwischen Wheel 30 und Wheel 210.
3.3 Technik
• Nutzt denselben Δ-Operator, memoryless.
• Keine Siebe, keine Caches.
4 Hinweis
Diese Arbeit wurde von mir Jeanette Tabea Leue entwickelt. Ich zeigt eine
praktische Umsetzung des Leueschen Δ-Operators:
deterministisch, erzeugend,
transparent im Code überprüfbar.
Bitte zitieren als:
Leue, J. T. (2025): Leuesches Primzahlsystem -- Δ-Operator Apps. Zenodo.
DOI: _____
2
