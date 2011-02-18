#! /usr/bin/env Rscript
# Copyright © 2010-2011 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProjects.
#
# Files included in this package ToyProjects are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

# Generic methods to extend the 'c'
c.myclass <- function(..., recursive = FALSE)  {
  dots <- list(...)
  ns <- sapply(dots, attr, which = "n")
  classes <- rep("myclass", length(dots))
  res <- structure(unlist(dots, recursive = FALSE), class = classes)
  attr(res, "n") <- ns
  return (res)
}
