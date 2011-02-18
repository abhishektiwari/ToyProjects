#! /usr/bin/env Rscript
# Copyright © 2010-2011 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProjects.
#
# Files included in this package ToyProjects are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

# Generic methods to extend the '['
`[.myclass` <- function (x, i)  {
  y <- unclass(x)[i]
  ns <- attr(x, "n")[i]
  class(y) <- "myclass"
  attr(y, "n") <- ns
  return (y)
}
