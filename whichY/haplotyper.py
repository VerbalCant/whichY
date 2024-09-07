# haplotyper.py

from .utils import load_y_dna, get_alignment_file, load_bam
from .lineage_identification import identify_lineage

def haplotype_analysis(input_file, alignment_file, input_format='fasta'):
    """
    Perform haplotype analysis on the provided Y-DNA data.
    Args:
        input_file (str): Path to the input data file (FASTA, VCF, or BAM).
        alignment_file (str): Path to the alignment file.
        input_format (str): Format of the input file ('fasta', 'vcf', 'bam').
    Returns:
        tuple: The paternal lineage of the Y-DNA data and confidence score.
    """
    # Load the input data based on format
    if input_format == 'bam':
        y_dna_data = load_bam(input_file)
    else:
        y_dna_data = load_y_dna(input_file, input_format)
    
    # Get the alignment file
    alignment_file = get_alignment_file(alignment_file)
    
    # Perform haplotype analysis
    lineage, confidence_score = identify_lineage(y_dna_data, alignment_file)
    
    return lineage, confidence_score