>>> from ftplib import FTP
>>> ftp = FTP('ftp.ncbi.nih.gov')
>>> ftp.login()
'230-Anonymous access granted, restrictions apply.\n Please read the file README.ftp\n230    it was last modified on Wed Apr  7 10:18:00 2010 - 193 days ago'
>>> ftp.retrlines('LIST')
dr-xr-xr-x   3 ftp      anonymous     4096 Sep  7 21:03 1000genomes
-r--r--r--   1 ftp      anonymous 10737418240 May 17 19:21 10GB
-r--r--r--   1 ftp      anonymous 1073741824 May 17 19:19 1GB
-r--r--r--   1 ftp      anonymous     1868 Apr  7  2010 README.ftp
lr--r--r--   1 ftp      anonymous       29 Apr  7  2010 asn1-converters -> toolbox/ncbi_tools/converters
dr-xr-xr-x   8 ftp      anonymous     4096 Sep 29  2004 blast
dr-xr-xr-x   3 ftp      anonymous     4096 Sep 13  2004 cgap
dr-xr-xr-x   4 ftp      anonymous     4096 Jan  8  2009 cn3d
dr-xr-xr-x  27 ftp      anonymous     4096 Sep 13 20:05 dbgap
dr-xr-xr-x   3 ftp      anonymous     4096 Aug 23 19:52 dra0
dr-xr-xr-x  11 ftp      anonymous     4096 Jun  4  2006 entrez
dr-xr-xr-x   7 ftp      anonymous     4096 Jun  2 15:21 epigenomics
dr-xr-xr-x   0 ftp      anonymous        0 Dec  4  2009 era0
dr-xr-xr-x   3 ftp      anonymous     4096 May  3 19:46 era1
dr-xr-xr-x   6 ftp      anonymous     4096 Aug  4  2006 fa2htgs
dr-xr-xr-x  10 ftp      anonymous   155648 Oct  1 20:20 genbank
dr-xr-xr-x   6 ftp      anonymous     4096 Aug 11 17:09 gene
dr-xr-xr-x  63 ftp      anonymous     8192 Sep 21 14:02 genomes
dr-xr-xr-x  24 ftp      anonymous     4096 Aug 18 03:08	hapmap
dr-xr-xr-x  12 ftp      anonymous     4096 Oct 14 16:39 mmdb
dr-xr-xr-x   5 ftp      anonymous   135168 Aug 19 03:53 ncbi-asn1
dr-xr-xr-x 147 ftp      anonymous    12288 Jul 26 20:07 pub
dr-xr-xr-x  10 ftp      anonymous     4096 Oct 15 18:28 pubchem
dr-xr-xr-x   2 ftp      anonymous     4096 Oct 16 01:15 pubmed
dr-xr-xr-x  15 ftp      anonymous     4096 Mar 24  2010 refseq
dr-xr-xr-x  57 ftp      anonymous     8192 Aug 20  2008 repository
dr-xr-xr-x   5 ftp      anonymous     4096 Oct  8 18:51 sequin
dr-xr-xr-x   9 ftp      anonymous     4096 May 24 20:03 sky-cgh
dr-xr-xr-x  16 ftp      anonymous    12288 May 18 02:50 snp
dr-xr-xr-x  13 ftp      anonymous     4096 Jul  9 16:55 sra
dr-xr-xr-x   4 ftp      anonymous     4096 Apr 13  2010 sra0
dr-xr-xr-x   5 ftp      anonymous     4096 May  5 00:11 sra1
dr-xr-xr-x   4 ftp      anonymous     4096 May 24 21:46 sra2
dr-xr-xr-x   2 ftp      anonymous     4096 Sep 29  2004 tech-reports
dr-xr-xr-x  13 ftp      anonymous     4096 Oct 16  2006 toolbox
dr-xr-xr-x   5 ftp      anonymous     4096 Apr 24  2009 tpa
dr-xr-xr-x   2 ftp      anonymous     4096 Sep  2 16:04 varpipe-intqc
'226 Transfer complete.'

>>>ftp.close



