>>> ftpkegg = FTP('ftp.genome.jp')
>>> ftpkegg.login()
'230 Anonymous access granted, restrictions apply'
>>> ftpkegg.retrlines('LIST')
drwxr-xr-x   4 (?)      (?)          4096 Nov  5  2007 pub
'226 Transfer complete'
>>> ftpkegg.dir()
drwxr-xr-x   4 (?)      (?)          4096 Nov  5  2007 pub
>>> ftpkegg.cwd('pub')
'250 CWD command successful'
>>> ftpkegg.dir()
drwxr-xr-x   3 (?)      (?)          4096 Nov  5  2007 db
drwxrwxr-x  13 (?)      (?)          4096 Oct  4 03:06 kegg
>>> ftpkegg.cwd('kegg')
'250 CWD command successful'
>>> ftpkegg.dir()
drwxrwxr-x   6 (?)      (?)          4096 Oct 16 22:25 brite
lrwxrwxrwx   1 (?)      (?)            26 Jan 30  2009 expression -> ../db/community/expression
drwxr-xr-x   8 (?)      (?)          4096 Oct 16 22:16 genes
drwxrwxr-x   8 (?)      (?)          4096 Oct 17 00:24 ligand
drwxr-xr-x   3 (?)      (?)          4096 Oct 11  2005 linkdb
drwxr-xr-x   3 (?)      (?)          4096 Oct 16 03:11 medicus
drwxrwxr-x   7 (?)      (?)          4096 Oct 16 23:59 pathway
drwxrwxr-x   9 (?)      (?)          4096 Jun 24  2009 pathway_gif
drwxrwxr-x   4 (?)      (?)          4096 Mar 28  2007 release
drwxr-xr-x   5 (?)      (?)          4096 Jan  6  2010 software
drwxrwxr-x   4 (?)      (?)          4096 Apr 30 00:04 xml
>>> ftpkegg.nlst()
['expression', 'brite', 'genes', 'ligand', 'linkdb', 'pathway', 'release', 'software', 'xml', 'pathway_gif', 'medicus']

>>>ftp.close
