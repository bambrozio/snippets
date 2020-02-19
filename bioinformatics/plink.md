# Simulating GWAS dataset
- Simulating Plink files (.bim, .bed, .fam, .phe)
- Converting Plink files to VCF
- Extracting phenotype from .fam file into a .phe to be used with the Plink argument `--pheno` in a association (`--glm`) test.
- Run association
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
...  886 Feb 19 15:13 1miSNP5kSamples.log
... 1.3G Feb 19 15:13 1miSNP5kSamples.vcf.bgz
...  86K Feb 19 14:59 1miSNP5kSamples.phe
...  26M Feb 19 14:44 1miSNP5kSamples.bim
... 116K Feb 19 14:44 1miSNP5kSamples.fam
... 1.2G Feb 19 14:44 1miSNP5kSamples.bed
...  35M Feb 19 14:43 1miSNP5kSamples-temporary.simfreq
...   80 Feb 19 14:34 1miSNP5kSamples.sim


$ head 1miSNP5kSamples.bim 
1       null_0  0       1       A       T
1       null_1  0       2       C       A
1       null_2  0       3       G       T
1       null_3  0       4       C       T
1       null_4  0       5       A       C
1       null_5  0       6       T       A
1       null_6  0       7       C       G
1       null_7  0       8       A       T
1       null_8  0       9       C       G
1       null_9  0       10      T       A
$ head 1miSNP5kSamples.fam 
per0 per0 0 0 2 2
per1 per1 0 0 2 2
per2 per2 0 0 2 2
per3 per3 0 0 2 2
per4 per4 0 0 2 2
per5 per5 0 0 2 2
per6 per6 0 0 2 2
per7 per7 0 0 2 2
per8 per8 0 0 2 2
per9 per9 0 0 2 2
$ tail 1miSNP5kSamples.fam 
per4990 per4990 0 0 2 1
per4991 per4991 0 0 2 1
per4992 per4992 0 0 2 1
per4993 per4993 0 0 2 1
per4994 per4994 0 0 2 1
per4995 per4995 0 0 2 1
per4996 per4996 0 0 2 1
per4997 per4997 0 0 2 1
per4998 per4998 0 0 2 1
per4999 per4999 0 0 2 1


$ plink2 --glm --bfile 1miSNP5kSamples --pheno 1miSNP5kSamples.phe --pheno-name T2D --out 1miSNP5kSamples
PLINK v2.00a2LM 64-bit Intel (6 Oct 2019)      www.cog-genomics.org/plink/2.0/
(C) 2005-2019 Shaun Purcell, Christopher Chang   GNU General Public License v3
Logging to 1miSNP5kSamples.log.
Options in effect:
  --bfile 1miSNP5kSamples
  --glm
  --out 1miSNP5kSamples
  --pheno 1miSNP5kSamples.phe
  --pheno-name T2D

Start time: Wed Feb 19 15:30:41 2020
16034 MiB RAM detected; reserving 8017 MiB for main workspace.
Using up to 4 compute threads.
5000 samples (5000 females, 0 males; 5000 founders) loaded from
1miSNP5kSamples.fam.
1001000 variants loaded from 1miSNP5kSamples.bim.
1 binary phenotype loaded (2100 cases, 2900 controls).
Calculating allele frequencies... done.
--glm logistic regression on phenotype 'T2D': done.
Results written to 1miSNP5kSamples.T2D.glm.logistic .
End time: Wed Feb 19 15:31:13 2020


$ head 1miSNP5kSamples.T2D.glm.logistic 
#CHROM  POS     ID      REF     ALT     A1      TEST    OBS_CT  OR      LOG(OR)_SE      Z_STAT  P
1       1       null_0  T       A       A       ADD     5000    1.0671  0.0666712       0.974056        0.330029
1       2       null_1  A       C       C       ADD     5000    1.10771 0.0525845       1.9453  0.0517392
1       3       null_2  T       G       G       ADD     5000    1.01267 0.0409198       0.307753        0.75827
1       4       null_3  T       C       C       ADD     5000    1.00489 0.040452        0.120568        0.904033
1       5       null_4  C       A       A       ADD     5000    0.975667        0.0563826       -0.436911       0.662176
1       6       null_5  A       T       T       ADD     5000    0.916188        0.0885134       -0.988937       0.322694
1       7       null_6  G       C       C       ADD     5000    1.03001 0.0417934       0.707417        0.479308
1       8       null_7  T       A       A       ADD     5000    0.931843        0.0565486       -1.24832        0.211915
1       9       null_8  G       C       C       ADD     5000    0.9851  0.0408423       -0.367573       0.713191
```