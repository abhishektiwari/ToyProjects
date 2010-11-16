#!/usr/bin/perl -w 

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProjects.
#
# Files included in this package ToyProjects are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.
use LWP::Simple;
$c=0;
for("M" .. "V") {
	$col = $_;
	for ($i = 1, $r = 0; $i <= 10, $r < 10; $i++, $r++) {	
		$url = "http://expasy.org/biomap/gifs/biochem_".$col.$i.".png";
		print $url, "\n";
		my $data = LWP::Simple::get($url);
		my $filename = "biochem_c".$c."_r".$r.".png";
		open (FH, ">$filename");
		binmode (FH);
		print FH $data;
		close (FH);
	}
	$c++;
}

# Call the montage function from ImageMagic and create a final big image
# system("montage -border 0 -geometry 720x -tile 10x10 biochem* meta.png")
