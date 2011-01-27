#! /usr/bin/env Rscript
# Copyright © 2010-2011 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProject.
#
# Files included in this package ToyProject are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

library(methods)

# Class defintion
setClass(
  "Sequences",
  representation(
    sequences="character"
  )
)
# New class defintion,inherting from superclass
setClass(
  "DNASequences",
  contains="Sequences",
  representation(
    chromosome="character"
  )
)

# Creating and initializing the object in single step
dnaSeq1 <- new("DNASequences", sequences = "aataaat", chromosome = "X")


# Initialize method
setMethod(
  "initialize",
  signature(
    .Object="Sequences"
  ),
  function(.Object, ..., sequences=character(0))  {
    sequences <- tolower(sequences)
    callNextMethod(.Object, ..., sequences=sequences)
  }
)

# Creating and initializing the object in single step
dnaSeq2 <- new("DNASequences", sequences = "AATAT",  chromosome = "X") 

# OR
# Creating object
dnaSeq3 <- new("DNASequences")
# Initializing the object in single step
initialize(dnaSeq3, sequences = "AATAT",  chromosome = "X")
