#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProjects.
#
# Files included in this package ToyProjects are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

"""
CSVPlot takes a csv file as input and plots it using Matplotlib. User needs 
to provide the command-line arguments and either short- or long-style flags
to specify various options. It can simply used to create 2D line plots.

usage: python CSVPlot.py [ -h | -f | -t | -c | -d | -v | -p] [arg] ...
Options and arguments (and corresponding environment variables):
-h    : print this help message (also --help)
-f    : input CSV file location (also --file)
-t    : tab-delimited csv files
-c    : comma-separated values (CSV) file (default)
-s    : semi colon delimited file
-o    : colon delimited file
-v    : save output images as svg file (default)
-p    : save output images as transparent png file
arg   : reference columns for plotting. CSVPlot plots all other columns 
        against the reference column. By default it uses column 1.

Example use:
1. For help information,
python CSVPlot.py --help 
OR
python CSVPlot.py --h 
2. For plotting column x and y of file data.csv,
python CSVPlot.py -c - p -f data.csv x y
python CSVPlot.py -t -v --file=data.csv x y

"""
import os
import sys
import getopt
import matplotlib.pyplot as mpl
import numpy as np
import csv

class Usage(Exception):
    "Usage() exception class, which we catch in an except clause at the end of main()"
    def __init__(self, msg):
        "A description of the Usage constructor"
        self.msg = msg

def main(argv=None):
    """
    main() function to analyse the command line flags and arguments, and
    activate further anlysis
    """
    fdelimiter = ","
    foutput = "svg"
    fargument = "0"
    if argv is None:
        argv=sys.argv
    try:
        if len(argv) <= 2:
            raise Usage(__doc__)
        try:
            opts,args = getopt.getopt(sys.argv[1:], "ctsovphf:", ["help","file="])
        except getopt.error, msg:
            raise Usage(msg)
        #Option processing
        for option, value in opts:
            if option in ("-h","--help"):
                raise Usage(__doc__)
                sys.exit(0)
            else:
                if option in ("-f", "--file"):
                    fname=value
                    print "Input CSV File:", fname
                    fdir=os.path.realpath(os.path.dirname(fname))
                    #fdir=os.path.dirname(os.path.realpath(fname))
            if option in("-t"):
                fdelimiter = "\t"
            elif option in("-c"):
                fdelimiter = ","
            elif option in("-s"):
                fdelimiter = ";"
            elif option in("-o"):
                fdelimiter = ":"
            if option in("-p"):
                foutput = "png"
            elif option in ("-v"):
                foutput = "svg"
        #Argument processing
        if len(args) != 0:
            for argument in args:
                argument.strip()
                try:
                    cargument = int(argument)
                except:
                    print 'cannot cast column argument to int'
                if isinstance(cargument, int) and cargument >= 1:
                    print "For column-",cargument
                    fargument = cargument-1
                    plotter(fname, fdelimiter, foutput, fargument, fdir)
        else:
            plotter(fname, fdelimiter, foutput, fargument, fdir)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

def plotter(fname, fdelimiter, foutput, fargument, fdir):
    """
    This function parse the data in csv file and then calls different 
    plotting functions"
    """
    try:
        fopen = open(fname,'r')
        csvreader = csv.reader(fopen, delimiter = ",")
        fields = csvreader.next()
    except:
        print "Can not open input csv file",fname
    fopen.close
    data = np.loadtxt(fname, delimiter = fdelimiter, unpack = True, skiprows = 1)
    mpl.plotfile(fname, cols = range(len(fields)/2), delimiter = fdelimiter, subplots = True, newfig = True)
    print "creating a example figure with ", len(fields)/2-1, "subplots"
    allfig = fdir + os.path.sep + "All_fig" + "." + foutput
    mpl.savefig(allfig)
    mpl.clf()
    i = 0;
    while i < len(fields):
        if fargument != i:
            mpl.plot(data[fargument], data[i])
            fieldname=fdir +os.path.sep + fields[fargument] +"_" + fields[i] + "." + foutput
            mpl.xlabel(fields[fargument])
            mpl.ylabel(fields[i])
            mpl.title(fields[fargument] + " vs " + fields[i])
            #Issues with transparent option when png is opted need fine tuning.
            #Check Howto section of matplotlib website
            #mpl.savefig(fieldname, transparent = True)
            mpl.grid(True)
            mpl.savefig(fieldname)
            print "Saving", fieldname
            mpl.clf()    
        i=i+1
        
if __name__ == "__main__":
    """
    The main program collected into function main()
    """
    sys.exit(main())
