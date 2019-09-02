LATEX       = pdflatex
CHECK_RERUN = grep "Rerun to get" $*.log

all: syllabus.pdf ps1.pdf

%.pdf: %.tex
	${LATEX} $*
	( ${CHECK_RERUN} && ${LATEX} $* ) || echo "Done."
	( ${CHECK_RERUN} && ${LATEX} $* ) || echo "Done."
