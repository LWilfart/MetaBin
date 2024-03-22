from Bio import SeqIO

def calculate_gc(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    total_count = sequence.count('A') + sequence.count('T') + gc_count
    gc_percentage = (gc_count / total_count) * 100
    return gc_percentage

fasta_file = "/home/dydinux/TFE/3_CUTM/03/contigs6M_200.fasta"
output_file = "/home/dydinux/TFE/10_Graph_GC_Cov_Binning/03/tableau200_6M.csv"

with open(output_file, 'w') as outfile:
    outfile.write("Contig,Coverage,%GC\n")

    count = 0
    for record in SeqIO.parse(fasta_file, "fasta"):
        if count >= 200:
            break
        
        contig = record.id
        sequence = record.seq
        coverage = float(contig.split("_")[-1])
        gc_percentage = calculate_gc(sequence)

        outfile.write(f"{contig},{coverage},{gc_percentage}\n")
        
        count += 1
