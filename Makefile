# Makefile for source rpm: elinks
# $Id$
NAME := elinks
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
