rule vep_annotation_online:
    input:
        "NIST.vcf.gz"  # Arquivo VCF original
    output:
        "results/annotated_variants.vcf"  # Arquivo anotado de saída
    params:
        assembly="GRCh37"  # Ou GRCh38, dependendo do VCF
    shell:
        """
        vep --offline --dir_cache ~/.vep/ --input_file {input} --output_file {output} --vcf --fork 4 --check_existing --everything
#        vep --offline --dir_cache ~/.vep/ --input_file {input} --output_file {output} --vcf --fork 4 --check_existing --fields 'SYMBOL,Consequence,IMPACT,AF,AFR_AF,AMR_AF,EAS_AF,SAS_AF,EUR_AF'
#        vep --offline --dir_cache ~/.vep/ --input_file {input} --output_file {output} --vcf --fork 4 --check_existing --fields 'CLIN_SIG,SYMBOL,AF,AFR_AF,AMR_AF,EAS_AF,EUR_AF,SAS_AF,gnomADe_AF,gnomADe_AFR_AF,gnomADe_AMR_AF,gnomADe_ASJ_AF,gnomADe_EAS_AF,gnomADe_FIN_AF,gnomADe_NFE_AF,gnomADe_OTH_AF,gnomADe_SAS_AF,gnomADg_AF,gnomADg_AFR_AF,gnomADg_AMI_AF,gnomADg_AMR_AF,gnomADg_ASJ_AF,gnomADg_EAS_AF,gnomADg_FIN_AF,gnomADg_MID_AF,gnomADg_NFE_AF,gnomADg_OTH_AF,gnomADg_SAS_AF'
#        vep --offline --dir_cache ~/.vep/ --input_file {input} --output_file {output} --vcf --fork 4 --check_existing --fields 'Allele,Consequence,IMPACT,SYMBOL,Gene,Feature_type,Feature,BIOTYPE,EXON,INTRON,HGVSc,HGVSp,cDNA_position,CDS_position,Protein_position,Amino_acids,Codons,Existing_variation,DISTANCE,STRAND,FLAGS,VARIANT_CLASS,SYMBOL_SOURCE,HGNC_ID,CANONICAL,MANE_SELECT,MANE_PLUS_CLINICAL,TSL,APPRIS,CCDS,ENSP,SWISSPROT,TREMBL,UNIPARC,UNIPROT_ISOFORM,GENE_PHENO,SIFT,PolyPhen,DOMAINS,miRNA,AF,AFR_AF,AMR_AF,EAS_AF,EUR_AF,SAS_AF,gnomADe_AF,gnomADe_AFR_AF,gnomADe_AMR_AF,gnomADe_ASJ_AF,gnomADe_EAS_AF,gnomADe_FIN_AF,gnomADe_NFE_AF,gnomADe_OTH_AF,gnomADe_SAS_AF,gnomADg_AF,gnomADg_AFR_AF,gnomADg_AMI_AF,gnomADg_AMR_AF,gnomADg_ASJ_AF,gnomADg_EAS_AF,gnomADg_FIN_AF,gnomADg_MID_AF,gnomADg_NFE_AF,gnomADg_OTH_AF,gnomADg_SAS_AF,MAX_AF,MAX_AF_POPS,CLIN_SIG,SOMATIC,PHENO,PUBMED,MOTIF_NAME,MOTIF_POS,HIGH_INF_POS,MOTIF_SCORE_CHANGE,TRANSCRIPTION_FACTORS'
        """
