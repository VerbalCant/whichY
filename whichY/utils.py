import pysam

def load_bam(bam_file):
    """
    Load Y-DNA data from a BAM file.
    Args:
        bam_file (str): Path to the BAM file.
    Returns:
        list: List of sequences from the BAM file.
    """
    sequences = []
    with pysam.AlignmentFile(bam_file, "rb") as bam:
        for read in bam.fetch():
            sequences.append(read.query_sequence)
    return sequences

# Existing functions like load_y_dna and get_alignment_file