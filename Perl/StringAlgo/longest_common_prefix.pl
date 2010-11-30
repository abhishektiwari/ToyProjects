# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProjects.
#
# Files included in this package ToyProjects are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.
#!/usr/bin/perl

use strict;
use warnings;

sub longest_common_prefix {
    my $prefix = shift;
    for (@_) {
	chop $prefix while (! /^$prefix/);
    }
    return $prefix;
}

print longest_common_prefix(@ARGV), " ";
