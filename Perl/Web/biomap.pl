#!/usr/bin/perl -w 

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProjects.
#
# Files included in this package ToyProjects are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.
use LWP::Simple;
for ($i =1; $i <= 10; $i++) {	
	for("A" .. "V") {
		$url = "http://expasy.org/biomap/gifs/biochem_".$_.$i.".png";
		print $url, "\n";
		my $data = LWP::Simple::get($url);
		my $filename = "biochem_".$_.$i.".png";
		open (FH, ">$filename");
		binmode (FH);
		print FH $data;
		close (FH);
	}
}
