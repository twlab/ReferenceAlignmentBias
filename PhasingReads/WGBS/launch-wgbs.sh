source activate snakemake && snakemake -p --jobs $THREADS --snakefile wgbs.smk --configfile $REFERENCE_ASSEMBLY.stats.yaml --config base_tmp_dir=$TEMP_DIRECTORY --directory $WORKING_DIRECTORY
