# 🌀 LEUE - Matemática de Ressonância de Leue

**Autora:** Jeanette Tabea Leue  
**Período:** Setembro 2025 - Fevereiro 2026

---

## 📖 Sobre Este Repositório

Este repositório contém a **Matemática de Ressonância de Leue** (*Leuesche Mathematik der Resonanz*), um framework matemático unificado que propõe soluções para os **7 Problemas do Milênio** através de uma abordagem baseada em ressonância, operadores e números primos.

---

## 📁 Estrutura do Repositório

```
LEUE/
├── 01-FUNDAMENTOS/
│   ├── Teoria-Base/          → Documentos fundamentais da teoria
│   └── Volumes-Completos/    → Os 7 volumes + 3 anexos completos
│
├── 02-PROBLEMAS-MILENIO/
│   ├── Riemann/              → Hipótese de Riemann ⭐
│   ├── Yang-Mills/           → Mass Gap de Yang-Mills ⭐
│   ├── Navier-Stokes/        → Equações de Navier-Stokes
│   ├── Hodge/                → Conjectura de Hodge
│   ├── Birch-Swinnerton-Dyer/→ Conjectura BSD
│   ├── Poincare/             → Conjectura de Poincaré
│   └── P-vs-NP/              → Problema P vs NP
│
├── 03-FRAMEWORK-MATEMATICO/
│   ├── ROC-Calculo-Operador-Ressonante/  → Cálculo de operadores
│   ├── LMC-Coeficientes-Modulacao/       → Coeficientes de Leue
│   ├── ROA-Arquitetura-Operador/         → Arquitetura de estabilidade
│   └── AMRD-Dinamica-Ressonancia/        → Dinâmica modulada
│
├── 04-FERRAMENTAS-INTERATIVAS/  → Calculadoras e visualizadores HTML
│
├── 05-VALIDACOES-E-PROVAS/
│   ├── Scripts-Python/       → Códigos de validação
│   └── Resultados/           → Provas e resultados numéricos
│
├── 06-VISUALIZACOES/
│   ├── Graficos-Riemann/     → Gráficos da função Zeta
│   ├── Graficos-Primos/      → Visualizações de primos
│   └── Diagramas-Estruturais/→ Diagramas do framework
│
└── 99-ARQUIVOS-SECUNDARIOS/  → Screenshots e arquivos auxiliares
```

---

## 🎯 Componentes Principais

### Δ-Operator (Operador Delta)
Gerador determinístico de candidatos a primos usando resíduos de roda e sequências de lacunas periódicas.

### Primwelle (Onda Prima)
Operador auto-adjunto H cujo espectro coincide com os zeros não-triviais de ζ(s):
$$H\psi_n = t_n\psi_n, \quad \zeta(\tfrac{1}{2} + it_n) = 0$$

### ROC - Resonant Operator Calculus
Decomposição em canais de estabilidade via projetores:
$$I = P_+ + P_0 + P_-$$

### LMC - Leue Modulation Coefficients
Coeficientes derivados de curvas elípticas que induzem condutividade modulada:
$$\sigma(x) = \sigma_0 (1 + \beta \cdot t(x)), \quad |t(x)| \leq 1$$

### ROA - Resonant Operator Architecture
Hamiltoniano com gap espectral garantido:
$$H = M + K, \quad \gamma_1 > 0$$

---

## 📚 Como Começar

### 1️⃣ Iniciantes
Leia os fundamentos em ordem:
1. [01-Guia-de-Leitura.md](01-FUNDAMENTOS/Teoria-Base/01-Guia-de-Leitura.md)
2. [02-Guia-Rapido.md](01-FUNDAMENTOS/Teoria-Base/02-Guia-Rapido.md)
3. [03-Matematica-de-Ressonancia-Leue.md](01-FUNDAMENTOS/Teoria-Base/03-Matematica-de-Ressonancia-Leue.md)

### 2️⃣ Problemas do Milênio
Cada problema tem sua própria pasta com documentação e provas:
- **Riemann**: A solução mais desenvolvida, com oscilador e validações
- **Yang-Mills**: Framework completo ROC/LMC/ROA para o Mass Gap

### 3️⃣ Explorar Interativamente
Abra os arquivos HTML em `04-FERRAMENTAS-INTERATIVAS/`:
- `calculadora-integral.html` - Calculador de integrais
- `Batimento-Cardiaco-dos-Primos.html` - Visualização do oscilador
- `Girassol-Primo-V5.html` - Padrão girassol dos primos

### 4️⃣ Validar com Código
Execute os scripts Python em `05-VALIDACOES-E-PROVAS/Scripts-Python/`

---

## 📊 Problemas do Milênio Abordados

| Problema | Status | Pasta |
|----------|--------|-------|
| Hipótese de Riemann | ⭐ Desenvolvido | `02-PROBLEMAS-MILENIO/Riemann/` |
| Yang-Mills Mass Gap | ⭐ Desenvolvido | `02-PROBLEMAS-MILENIO/Yang-Mills/` |
| Navier-Stokes | 📄 Documentado | `02-PROBLEMAS-MILENIO/Navier-Stokes/` |
| Conjectura de Hodge | 📄 Documentado | `02-PROBLEMAS-MILENIO/Hodge/` |
| BSD | 📄 Documentado | `02-PROBLEMAS-MILENIO/Birch-Swinnerton-Dyer/` |
| Poincaré | 📄 Documentado | `02-PROBLEMAS-MILENIO/Poincare/` |
| P vs NP | 📄 Documentado | `02-PROBLEMAS-MILENIO/P-vs-NP/` |

---

## 🔗 Citação

> Leue, J. T. (2025-2026). *Leuesche Mathematik der Resonanz: Eine operatorielle Strategie zur Riemannschen Vermutung und den Millennium-Problemen.*

---

*Última atualização: Fevereiro de 2026*
