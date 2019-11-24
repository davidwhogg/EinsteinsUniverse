LATEX       = pdflatex
CHECK_RERUN = grep "Rerun to get" $*.log

all: syllabus.pdf \
     ps1.pdf ps2.pdf ps3.pdf ps4.pdf ps5.pdf ps6.pdf \
     exam5.pdf

exam5.tex: ../py/make_exam5.py
	cd ../py ; make

%.pdf: %.tex eu.tex
	${LATEX} $*
	( ${CHECK_RERUN} && ${LATEX} $* ) || echo "Done."
	( ${CHECK_RERUN} && ${LATEX} $* ) || echo "Done."
