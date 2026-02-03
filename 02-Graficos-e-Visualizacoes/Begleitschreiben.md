# Begleitschreiben

*Convertido de: Begleitschreiben.PDF*

---


## Página 1


Erklärungen zu den Plots
(Begleitdokument zum ZIP)
Autor: Jeanette Tabea Leue Datum: 21.08.2025
Hinweis. Dieses Dokument beschreibt die Abbildungen im ZIP. Alle Plots wurden aus den hochgeladenen
Daten/Notebooks erzeugt. Kurze Legenden erklären Zweck, Methode und Aussage jeder Graﬁk.
Inhalt (Kategorien)
• Riemann/Hardy–Z: Nullstellen, Dichten, Riemann–Siegel
• Primzahlen/„Primwelle“: Dichte, Log-Periodik, Spektren
• Resonanz/Kopplung: Hüllkurven, Pulsantrieb, Skalierungen
• Optik/Phase: Fernfeld-Proﬁle, Phasenverzögerung, Zentroid
• Kosmo-Skalen: T(z), z(a), normierte Expansionsfunktion
Riemann/Hardy–Z
Hardy-Z-Funktion Z(t) für s=12+it (0–50). Vertikale Hilfslinien markieren bekannte Nullstellen. Zweck:
Visualisiert Wechsel der Vorzeichen und die Wellenstruktur nahe den Nullstellen.
Riemann-Siegel-Evaluation von Z(t) (0–200) mit markierten Nullen. Vergleich mit bekannter Nullstellenliste
zeigt korrekte Lage (Validierung der Implementierung).
Abstände Δtn zwischen aufeinanderfolgenden Nullstellen und Mittelwert. Aussage: Fluktuierende lokale
Dichte um den bekannten asymptotischen Trend.
N(T) beobachtet vs. Riemann–von–Mangoldt-Asymptotik. Aussage: Stufenfunktion der Zählung folgt der
asymptotischen Kurve eng.
Lokale Frequenz 1/Δt vs. (1/(2π))ln(T/2π). Aussage: Trend deckt sich; lokale Streuung sichtbar (typisch).
Primzahlen und „Primwelle“
Primdichte ρ(x): Baseline 1/logx und gedämpfte Modelle (α). Aussage: Dämpfung glättet Oszillationen,
Mitteltrend bleibt.
„Primwelle“ – Spektrogramm (Fensteranalyse). Aussage: keine dominanten stabilen Linien; breit verteilte
Energie (schematisch/diagnostisch).
Spektralsignatur in u=lnr: Peak nahe 1/(2π) (oder 1 je nach Normierung). Aussage: Log-periodische
Struktur messbar (Modell-Indiz).
Resonanz, Kopplung und Dynamik
Gekoppelte Oszillatoren: resonante Pulsfolge vs. oﬀ-resonant. Aussage: Resonanz pumpt Energie sichtbar;
Oﬀ-Res bleibt klein.
Hüllkurvenvergleich: resonant vs. oﬀ-resonant (normiert). Aussage: Langsam ansteigende Energie unter
Resonanz, Referenz bleibt niedrig.
Kopplungs-Scan (κ): größere Kopplung erhöht Übertrag trotz Detuning. Aussage: Skalenabhängigkeit der
Energieübertragung.
Lineare Kopplung:
PhaseRMS
∝
Anregungsamplitude A (Hexaprim-Pulsfolge).
Aussage:
Fast
lineare
Regression über den getesteten Bereich.
Optische Proﬁle und Phaseneﬀekte
Fernfeld-Schnitt (ohne zusätzliche Phase). Aussage: Referenzproﬁl, dient als Basis für Vergleich.
Fernfeld-Schnitt mit Phasenmodulation
φ0=1. Aussage: Proﬁl bleibt formähnlich; (hier) Verschiebung
gering/nicht sichtbar.
Fernfeld-Schnitt mit stärkerer Modulation φ0=3. Aussage: Vergleich zur Referenz für Zentroid/Peak-Analyse.
Zentroid/Peak-Bestimmung der 1D-Proﬁle. Aussage: („Technische“) Auswertungslinie für Lageverschiebung.


## Página 2


Phasenverzögerung Δφ(b) durch Dichteglocke (Gauss-Proﬁl). Aussage: Maximale Verzögerung nahe Zentrum,
seitlich abfallend.
Phasenverzögerung für verschiedene Breiten σ. Aussage: Größere σ ⇒breiteres, höheres Verzögerungsproﬁl.
Kosmologische Skalen (Hilfsplots)
CMB-Temperatur T(z)=T0(1+z): Skalenrelation (didaktischer Plot).
Redshift vs. Skalenfaktor a: z=1a-1 (Normierung/Interpretation).
Normierte Expansionsfunktion
1/E(a) (schematisch).
Aussage: Verlauf
zur Orientierung,
keine direkte
Ableitung.
Weitere Darstellungen
Re/Imζ(0.5+it) als Wellenverlauf (0–50). Aussage: Phasenlage und Koinzidenz der Nullen von Re/Im nahe
kritischer Linie.
3D-Darstellung mehrerer „Zeta-Wellen“ vs. t (schematisch, informativ).
Reproduzierbarkeit
Die Plots lassen sich aus den im ZIP enthaltenen Notebooks/Skripten generieren. Wo „schematisch“ vermerkt
ist, dient die Graﬁk der Illustration eines Modells oder einer Messgröße; alle übrigen stammen aus direkter
Berechnung (Hardy–Z/Riemann–Siegel, Nullstellendichten, Kopplungs-Simulationen).
Kontakt:
