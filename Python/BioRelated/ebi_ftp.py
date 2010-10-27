>>> from ftplib import FTP
>>> ftpebi = FTP('ftp.ebi.ac.uk')
>>> ftpebi.login()
'230 Login successful.'
>>> ftpebi.dir()
drwxr-xr-x   10 ftp      ftp          4096 Aug 27 14:13 pub
>>> ftpebi.cwd('pub')
'250 Directory successfully changed.'
>>> ftpebi.dir()
lrwxrwxrwx    1 ftp      ftp            20 May 13 18:21 blast -> databases/ncbi/blast
drwxrwxr-x   57 ftp      ftp          4096 Oct 08 21:01 contrib
drwxrwxr-x  152 ftp      ftp          8192 Sep 03 16:34 databases
drwxrwxr-x    2 ftp      ftp          4096 Aug 29  2002 embnet.news
drwxrwxr-x    2 ftp      ftp          4096 Mar 25  2008 help
drwxr-x---    7 ftp      ftp          4096 May 15  2000 mirror-patch-test
drwxrwxr-x    2 ftp      ftp          4096 Aug 15  2001 phd
drwxrwxr-x   27 ftp      ftp          4096 Dec 19  2007 software
>>> ftpebi.cwd('databases')
'250 Directory successfully changed.'
>>> ftpebi.dir()
drwxrwsr-x    2 ftp      ftp          4096 Feb 13  2009 1000genomes
drwxr-xr-x    6 ftp      ftp          4096 Mar 25  1997 16S_RNA
drwxrwxr-x    2 ftp      ftp          4096 Nov 02  2000 3Dee
drwxrwxr-x    2 ftp      ftp          8192 May 18  2000 3d_ali
drwxrwxr-x    2 ftp      ftp          4096 Jun 08  2007 ASD

output truncated

>>> ftpebi.nlst()
['1000genomes', '16S_RNA', '3Dee', '3d_ali', 'ASD', 'DictyDB', 'EGI', 'FBA2KO', 'Fregene_datasets', 'GO', 'HGNC', 'IPI', 'IntAct', 'MassSpecDB', 'PeptideSearch', 'Pfam', 'RESID', 'RHdb', 'SPproteomes', 'Science', 'SubtiList', 'UTR', 'Unigene', 'ace', 'alu', 'androgenr', 'arrayexpress', 'astd', 'backup.info', 'berlin', 'bii', 'bio_catal', 'biomart', 'blocks', 'blocks.old', 'camoddssp', 'camodhssp', 'camodpdb', 'cd40lbase', 'chebi', 'chembl', 'clustr', 'codonusage', 'cpgisle', 'cutg', 'dali', 'databanks', 'dbEST', 'dbGSS', 'dbSTS', 'dbcat', 'dgva', 'domo', 'dssp', 'ecdc', 'edgp', 'edpcc', 'embl', 'embnet', 'emdb', 'emp', 'emvec', 'ena', 'ensembl', 'enzyme', 'epd', 'fans_ref', 'fastafiles', 'fingerPRINTScan', 'flybase', 'fssp', 'geneticcode', 'genome_reviews', 'genomes', 'gpcrdbsup', 'haema', 'haemb', 'hamsters', 'hla', 'hovergen', 'hssp', 'imgt', 'info', 'intact', 'integr8', 'intenz', 'interpro', 'ipd', 'journals_toc', 'kabat', 'limb', 'lista', 'lrgex', 'mdm2', 'methyl', 'microarray', 'microcosm', 'misfolded', 'models', 'msd', 'mutres', 'ncbi', 'nmrshiftdb', 'nrdb90', 'nrl_3d', 'nrsub', 'nucleosomal_dna', 'ols', 'p53', 'p53APC', 'parasites', 'patentdata', 'pdb_finder', 'pdb_select', 'pdb_seq', 'pir', 'pir2sptr', 'piraln', 'pkcdd', 'plmitrna', 'pmc', 'pride', 'primers', 'prints', 'prodom', 'prof_pat', 'prosite', 'pubchem', 'puu', 'ras', 'rcsb', 'rdp', 'rebase', 'reference_proteomes', 'reflist', 'relibrary', 'repbase', 'rhea', 'rldb', 'rrna', 'sbase', 'seqanalref', 'smallrna', 'srp', 'stackdb', 'stride', 'supplementary', 'swissprot', 'taxonomy', 'testsets', 'tfd', 'tmp', 'transfac', 'transterm', 'trembl', 'trna', 'uniprot', 'variantdbs', 'xray', 'yeast']
>>> ftpebi.nlst('pubchem')
['pubchem/Bioassay', 'pubchem/CACTVS', 'pubchem/Compound', 'pubchem/Compound_3D', 'pubchem/README', 'pubchem/Substance', 'pubchem/data_spec', 'pubchem/publications', 'pubchem/specifications']
>>> ftpebi.nlst('pubchem/Compound')
['pubchem/Compound/CURRENT-Full', 'pubchem/Compound/Daily', 'pubchem/Compound/Extras', 'pubchem/Compound/Monthly', 'pubchem/Compound/README', 'pubchem/Compound/Weekly']

