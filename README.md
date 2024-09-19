# VCF Annotation App

## Descrição do Projeto

Este projeto visa anotar um arquivo VCF utilizando **Snakemake** e, em seguida, servir as variantes anotadas através de uma **API Flask**. A pipeline foi projetada para realizar as anotações e disponibilizar essas informações em um ambiente interativo via API, permitindo filtros baseados em frequência alélica (AF) e profundidade de leitura (DP).

### Arquivos e Estrutura

- **NIST.vcf.gz**: Este é o arquivo VCF de entrada que será utilizado como exemplo para a anotação.
- **Snakefile**: Contém a configuração da pipeline em Snakemake, que executa a anotação do VCF utilizando o **VEP** (Variant Effect Predictor). O output anotado é salvo no diretório `results`.
- **results/**: O diretório onde o VCF anotado e o arquivo de sumário são salvos após a execução do Snakemake. O arquivo de saída principal é o `annotated_variants.vcf`.
- **app.py**: Arquivo responsável pela criação da API Flask, que lê o VCF anotado e permite a filtragem das variantes com base nos parâmetros de frequência e profundidade inseridos pelo usuário.
- **templates/**: Diretório contendo o arquivo HTML básico para a interface do Flask.
- **test.py**: Arquivo de testes (opcional) para verificar a integridade das funções.

## Rodando o Projeto

### Pré-requisitos

Antes de rodar o projeto, certifique-se de ter as seguintes dependências instaladas:

- **Python 3.7+**
- **Conda** ou **Virtualenv** (para gerenciar ambientes)
- **bcftools**
- **vep** (Variant Effect Predictor, v112. Para o presente projeto, foi baixado e estava disponível em cache)

###  Executando o Snakemake para Anotar o VCF

Certifique-se de que o VEP está configurado corretamente no seu ambiente e que o cache está disponível para rodar offline.

### Rode a pipeline do Snakemake para anotar o arquivo VCF:
  
   ```bash
   snakemake -s Snakefile
   ```
### Rodando o App Flask

Após rodar o Snakemake e gerar o VCF anotado, execute o servidor Flask:

   ```bash
   python app.py
   ```

A API permite que você filtre variantes com base nos seguintes parâmetros:

    AF: Frequência alélica
    DP: Profundidade de leitura
