A simple shell script to create the phenotype file from a .fam file:
```
FAM_FILE=test.fam \
&& PHE_FILE=test.phe \
&& echo "#FID IID T2D" > $PHE_FILE \
&& awk -F " " '{print $1" "$2" "$6}' $FAM_FILE >> $PHE_FILE
```
