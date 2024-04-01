<p align="center">
  <img width="500" height="200" src="https://i.imgur.com/IiYt3Wr.png">
</p>

MetaBin is a collection of Python scripts designed to perform GC content percentage against coverage binning, utilizing contigs.fasta and blast files to swiftly unveil the predominant organisms within a sample.  

---
*I am currently working on a pipeline version using nextflow.*

--- 

Here are the steps to follow:  
**1. Creation of a table from spades results in contigs.fasta**  
      Use the script tb_spades.py  
**2. Creation of a table with accession code from the blast file, then joining them with the table from 1**  
      Use the script ligne_acc_blast.py  
**3. Creation of a simple plot GC content percentage/coverage**  
      Use the script simple_plot.py  
**4. Creation of a plot with color and legend**  
      Use the script colored_leg_plot.py  
**5. Creation of a plot with specific accession code only**  
      Use the script specific_code_plot_cl.py  


*These scripts are a part of my bachelor thesis which was about studying microbiota communities involved in biogas production. You can found my thesis in the thesis folder.*
