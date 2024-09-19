import vcfpy

def filter_variants(af_threshold, dp_threshold):
    filtered_variants = []
    with vcfpy.Reader.from_path('results/annotated_variants.vcf') as reader:
        for record in reader:
            af_values = record.INFO.get('AF', [0])  # AF tradicional do campo INFO
            dp = record.INFO.get('DP', 0)  # DP do campo INFO
            csq_field = record.INFO.get('CSQ', [])

            # Extrair Existing_variation, AF_1000Genomes (do CSQ) e SYMBOL do campo CSQ
            for csq_entry in csq_field:
                csq_values = csq_entry.split('|')

                # Pegar os campos de interesse pelo índice
                existing_variation = csq_values[17]  # Existing_variation
                af_csq = csq_values[39]  # AF do 1000 Genomes
                symbol = csq_values[3]  # SYMBOL (nome do gene)

                # Converter AF do CSQ para float, se disponível
                af_csq = float(af_csq) if af_csq else 0.0

                # Converter AF tradicional (do campo INFO) para float
                af = float(af_values[0]) if af_values else 0.0

                # Verificar se o AF (tradicional) e DP atendem aos critérios
                if af >= af_threshold and dp >= dp_threshold:
                    filtered_variants.append({
                        'chrom': record.CHROM,
                        'pos': record.POS,
                        'id': record.ID,
                        'ref': record.REF,
                        'alt': [str(alt) for alt in record.ALT],
                        'af': af,  # AF tradicional
                        'af_1000g': af_csq,  # AF do 1000 Genomes
                        'dp': dp,
                        'existing_variation': existing_variation,
                        'symbol': symbol  # Nome do gene
                    })

    return filtered_variants


# Exemplo de uso
af_threshold = 0.01
dp_threshold = 10
filtered_variants = filter_variants(af_threshold, dp_threshold)

# Exibir as variantes filtradas
for variant in filtered_variants:
    print(variant)
