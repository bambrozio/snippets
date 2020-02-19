# Simulating GWAS dataset
- Simulating Plink files (.bim, .bed, .fam, .phe)
- Converting Plink files to VCF
- Extracting phenotype from .fam file into a .phe to be used with the Plink argument `--pheno` in a association (`--glm`) test.
```
$ echo "1000000  null      0.00 1.00  1.00 1.00" > 1miSNP5kSamples.sim
$ echo "1000     disease   0.00 1.00  2.00 mult" >> 1miSNP5kSamples.sim


$ plink1.9 --simulate 1miSNP5kSamples.sim acgt --make-bed --out 1miSNP5kSamples --simulate-ncases 2100 --simulate-ncontrols 2900
PLINK v1.90b3.31 64-bit (3 Feb 2016)       https://www.cog-genomics.org/plink2
(C) 2005-2016 Shaun Purcell, Christopher Chang   GNU General Public License v3
Logging to 1miSNP5kSamples.log.
Options in effect:
  --make-bed
  --out 1miSNP5kSamples
  --simulate 1miSNP5kSamples.sim acgt
  --simulate-ncases 2100
  --simulate-ncontrols 2900

16034 MB RAM detected; reserving 8017 MB for main workspace.
Writing --simulate dataset to 1miSNP5kSamples-temporary.bed +
1miSNP5kSamples-temporary.bim + 1miSNP5kSamples-temporary.fam ... done.
Realized simulation parameters saved to 1miSNP5kSamples-temporary.simfreq.
1001000 variants loaded from .bim file.
5000 people (0 males, 5000 females) loaded from .fam.
5000 phenotype values loaded from .fam.
Using 1 thread (no multithreaded calculations invoked.
Before main variant filters, 5000 founders and 0 nonfounders present.
Calculating allele frequencies... done.
1001000 variants and 5000 people pass filters and QC.
Among remaining phenotypes, 2100 are cases and 2900 are controls.
--make-bed to 1miSNP5kSamples.bed + 1miSNP5kSamples.bim + 1miSNP5kSamples.fam
... done.


$ FAM_FILE=1miSNP5kSamples.fam \
> && PHE_FILE=1miSNP5kSamples.phe \
> && echo "#FID IID T2D" > $PHE_FILE \
> && awk -F " " '{print $1" "$2" "$6}' $FAM_FILE >> $PHE_FILE

$ head -n 3 1miSNP5kSamples.phe 
#FID IID T2D
per0 per0 2
per1 per1 2
$ tail -n 3 1miSNP5kSamples.phe 
per4997 per4997 1
per4998 per4998 1
per4999 per4999 1


$ plink1.9 --recode vcf bgz --bfile 1miSNP5kSamples --out 1miSNP5kSamples
PLINK v1.90b3.31 64-bit (3 Feb 2016)       https://www.cog-genomics.org/plink2
(C) 2005-2016 Shaun Purcell, Christopher Chang   GNU General Public License v3
Logging to 1miSNP5kSamples.log.
Options in effect:
  --bfile 1miSNP5kSamples
  --out 1miSNP5kSamples
  --recode vcf bgz

16034 MB RAM detected; reserving 8017 MB for main workspace.
1001000 variants loaded from .bim file.
5000 people (0 males, 5000 females) loaded from .fam.
5000 phenotype values loaded from .fam.
Using up to 4 threads (change this with --threads).
Before main variant filters, 5000 founders and 0 nonfounders present.
Calculating allele frequencies... done.
1001000 variants and 5000 people pass filters and QC.
Among remaining phenotypes, 2100 are cases and 2900 are controls.
--recode vcf bgz to 1miSNP5kSamples.vcf.gz ... done.


$ mv 1miSNP5kSamples.vcf.gz 1miSNP5kSamples.vcf.bgz

$ ls -lath
total 2.6G
-rw-r----- 1 airflow airflow  886 Feb 19 15:13 1miSNP5kSamples.log
-rw-r----- 1 airflow airflow 1.3G Feb 19 15:13 1miSNP5kSamples.vcf.bgz
-rw-r----- 1 airflow airflow  86K Feb 19 14:59 1miSNP5kSamples.phe
-rw-r----- 1 airflow airflow  26M Feb 19 14:44 1miSNP5kSamples.bim
-rw-r----- 1 airflow airflow 116K Feb 19 14:44 1miSNP5kSamples.fam
-rw-r----- 1 airflow airflow 1.2G Feb 19 14:44 1miSNP5kSamples.bed
-rw-r----- 1 airflow airflow  35M Feb 19 14:43 1miSNP5kSamples-temporary.simfreq
-rw-r----- 1 airflow airflow   80 Feb 19 14:34 1miSNP5kSamples.sim
```