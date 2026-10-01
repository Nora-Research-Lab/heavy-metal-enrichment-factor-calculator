![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Heavy Metal Enrichment Factor Calculator
 
*For environmental geoscientists and soil quality analysts: enter metal concentration in soil and a background reference to instantly compute the enrichment factor (EF) and contamination classification.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Environmental Geoscience
 
**Inputs:**
- Dropdown to select a heavy metal element: Pb, Cd, Hg, As, Cu, Zn, Cr, Ni, or 'Other'. If an element is selected, its crustal average concentration (mg/kg) is auto-loaded as the default background value (from a hardcoded lookup table). If 'Other' is selected, the background input is enabled and must be entered manually.
- Numeric input 'Metal concentration in sample (mg/kg)' – user-entered, must be > 0.
- Numeric input 'Background/Reference concentration (mg/kg)' – pre-filled with crustal value for the chosen element, but user can overwrite.
- A 'Calculate' button.

**Core logic:**
1. Read sample concentration C_sample and background concentration C_bg.
2. Compute enrichment factor: EF = C_sample / C_bg.
3. Classify EF according to standard thresholds:
   - EF < 1: 'No enrichment'
   - 1 ≤ EF < 3: 'Minor enrichment'
   - 3 ≤ EF < 5: 'Moderate enrichment'
   - 5 ≤ EF < 10: 'Moderately severe enrichment'
   - 10 ≤ EF < 25: 'Severe enrichment'
   - EF ≥ 25: 'Very severe enrichment'
4. Assign a color for classification display (green to dark red).

**Outputs:**
- Large centered number showing EF rounded to 2 decimals.
- Text classification with colored badge.
- A simple horizontal bar plot (matplotlib) showing the EF value on a scale from 0 to 30, with class boundary markers. The plot is rendered as a Gradio Plot component.

**Gradio UI:**
- gr.Blocks with a title and simple instructions.
- Two columns: left column contains the element dropdown and the two numeric inputs (side by side).
- Button centered below.
- Output area: row with EF number and classification badge on the left, plot on the right.
- Clean, professional look with minimal clutter.

**AI/ML:** None required; purely deterministic calculations.
 
## Run it
 
```bash
docker build -t heavy-metal-enrichment-factor-calculator .
docker run -p 7860:7860 heavy-metal-enrichment-factor-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-10-01.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
