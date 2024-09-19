from flask import Flask, request, jsonify, render_template
import vcfpy

app = Flask(__name__)

def filter_variants(af_threshold, dp_threshold):
    filtered_variants = []
    with vcfpy.Reader.from_path('results/annotated_variants.vcf') as reader:
        for record in reader:
            af_values = record.INFO.get('AF', [0])  # AF tradicional
            dp = record.INFO.get('DP', 0)  # DP
            csq_field = record.INFO.get('CSQ', [])

            # Extrair Existing_variation, AF_1000Genomes (do CSQ) e SYMBOL do campo CSQ
            for csq_entry in csq_field:
                csq_values = csq_entry.split('|')

                existing_variation = csq_values[17]  # Existing_variation
                symbol = csq_values[3]  # SYMBOL (nome do gene)

                # Tentar converter AF (do CSQ) para float e pular se der erro
                try:
                    af_csq = float(csq_values[39]) if csq_values[39] else 0.0  # AF_1000Genomes
                except ValueError:
                    af_csq = 0.0

                # Tentar converter AF tradicional (do campo INFO) para float e pular se der erro
                try:
                    af = float(af_values[0]) if af_values else 0.0  # AF tradicional
                except ValueError:
                    af = 0.0

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/filter', methods=['GET'])
def filter_variants_api():
    # Pegar parâmetros AF e DP da requisição
    af_threshold = float(request.args.get('af_threshold', 0.01))  # Default 0.01
    dp_threshold = int(request.args.get('dp_threshold', 10))  # Default 10

    # Filtrar variantes com base nos thresholds fornecidos
    filtered_variants = filter_variants(af_threshold, dp_threshold)

    # Retornar as variantes filtradas como JSON
    return jsonify(filtered_variants)


if __name__ == '__main__':
    app.run(debug=True)
