# tests/test_haplotyper.py

import unittest
from whichY.haplotyper import haplotype_analysis

class TestHaplotyper(unittest.TestCase):
    def test_identify_lineage(self):
        # Test with a known Y-DNA sequence in FASTA format
        lineage, confidence = haplotype_analysis('test_data.fasta', 'alignment_file', 'fasta')
        self.assertEqual(lineage, 'ExpectedLineage')
        self.assertGreaterEqual(confidence, 0.0)
        self.assertLessEqual(confidence, 1.0)
        
        # Test with a known Y-DNA sequence in BAM format
        lineage, confidence = haplotype_analysis('test_data.bam', 'alignment_file', 'bam')
        self.assertEqual(lineage, 'ExpectedLineage')
        self.assertGreaterEqual(confidence, 0.0)
        self.assertLessEqual(confidence, 1.0)
