#!/usr/bin/perl 
#===============================================================================
#
#         FILE:  fastafrcsv.pl
#
#        USAGE:  ./fastafrcsv.pl 
#
#  DESCRIPTION:  
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:   (), <>
#      COMPANY:  
#      VERSION:  1.0
#      CREATED:  11/02/2007 04:55:22 PM SGT
#     REVISION:  ---
#===============================================================================

use strict;
use warnings;

while (<>)
{
	#print $_;
	my @a = split(/,/,$_);#delimiter
	#print '>'.$a[0]."\n".$a[1]."\n";
	#print '>'.$a[1]."AlleleA_ProbeSeq \n".$a[5]."\n";
	#print '>'.$a[1]."AlleleB_ProbeSeq \n".$a[7]."\n";
	print '>'.$a[1]."SourceSeq \n".$a[16]."\n";
}

