<p align="center">
  <img width="500" height="200" src="https://i.imgur.com/IiYt3Wr.png">
</p>

MetaBin is a collection of Python scripts designed to perform GC content percentage against coverage binning, utilizing contigs.fasta and blast files to swiftly unveil the predominant organisms within a sample.

---

**These scripts are a part of my 6 months work in sweden (SLU) and my bachelor thesis (Binning step - see workflow below) which was about studying microbiota communities involved in biogas production by analyzing biological data (DNA) to improve biogas production** - *You can found my thesis in the thesis folder.*

### What is it Biogas ?

Biogas is a renewable energy source produced through the decomposition of organic matter in the absence of oxygen. It mainly consists of 50-70% methane (CH₄) and 30-50% carbon dioxide (CO₂), with small amounts of other gases. Biogas can be used to generate electricity, heat, or as a fuel, providing a way to repurpose organic waste while reducing greenhouse gas emissions.

#### Biogas plant input/output

<p align="center">
    <img width="570" height="700" src="https://imgur.com/xzEd3wS.png">
</p>


### What was the purpose of my bachelor thesis ?

This project aims to analyze biological data (dna) from biogas reactors to identify key factors (organisms) influencing the production process and therefore optimizing biogas production which is a major challenge in the development of renewable energy.

### What tools did I used and what was my workflow ?

<p align="center">
    <img width="620" height="700" src="https://i.imgur.com/24PcAou.png">
</p>

### What are the results ?

I was able to identify organisms that are involved in biogas production :

- I have highlighted three main organisms involved in biogas formation within the samples. These are: *Limnochorda pilosa*, *Methanoculleus bourgensis* and
*Methanogenic chikugoensis*. 
- Some others were involved in the biogas process by synchronisms like *Thermacetogenium phaeum*, this means that they work in coordination creating the right conditions for *Methanoculleus bourgensis* to produce methane efficiently.
- Others are interested in precursor steps of methanogenesis like *Defluviitoga tunisiensis*.

#### Exemple of GC content percentage against coverage binning graph (made with python scripts)
<p align="center">
    <img width="700" height="580" src="https://i.imgur.com/QdssSWY.png">
</p>

### Perspective

With more data, I could have gone one step further with optimization of living condition of those organisms to improve biogas production.

---
### How to use the scripts :

Here are the steps to follow:  

**1. Creation of a table from spades results in contigs.fasta**  
      Use the script tb_spades.py  
**2. Creation of a table with accession code from the blast file, then joining them with the table from 1**  
      Use the script extract_blast_line.py  
**3. Creation of a simple plot GC content percentage/coverage**  
      Use the script simple_plot.py  
**4. Creation of a plot with color and legend**  
      Use the script colored_leg_plot.py  
**5. Creation of a plot with specific accession code only**  
      Use the script specific_code_plot_cl.py  

---
*I am currently working on a pipeline version using nextflow.*

--- 

