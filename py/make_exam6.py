import numpy as np
import pylab as plt
np.random.seed(17)
plt.rc('font', size=8)
nproblem = 8 # magic
nstudent = 120 # magic

problems = [r"""\begin{problem}
(From Problem Set 6)
What is the mass of a black hole that has a radius of 1\,AU?
\end{problem}""", r"""\begin{problem}
(From Problem Set 6)
Alice and Bob drive from point A to point B, and it takes Alice 5 hours. If Bob takes one hour longer to
 do the drive than Alice took, by what factor was he driving slower? Answer in any form you like!
\end{problem}""", r"""\begin{problem}
(From Problem Set 6)
What is the mass of the black hole at the center of the Milky Way?
\end{problem}""", r"""\begin{problem}
(From Problem Set 6)
Why did the black hole merger discovered by \textsl{LIGO} produce a final black hole that is less massive than the sum of the masses of the two black holes that merged to make it? Or, where did the mass go?
\end{problem}""", r"""\begin{problem}
(From the reading)
The \textsl{Event Horizon Telescope} took an image of a black hole. Where was that black hole?
\end{problem}""", r"""\begin{problem}
(From Lecture)
What is the relationship between an acceleration $a$, a change in velocity $\Delta v$ and a small time interval $\Delta t$? Give an equation.
\end{problem}""", r"""\begin{problem}
(From Lecture)
When a gravitational wave passes through the \textsl{LIGO} detector, what does it do to the detector arms?
\end{problem}""", r"""\begin{problem}
(From Lecture)
The \textsl{Event Horizon Telescope} measurement of the black-hole size was (in angular units) something like 40\,micro-arcseconds. How many arcseconds are there in a degree?
\end{problem}"""]
assert len(problems) == nproblem

print(r"""
\documentclass[12pt, letterpaper]{article}
\include{eu}
\pagestyle{empty}

\begin{document}

""")

for student in range(nstudent):
    print(r"""
\noindent
Name: \rule[-1ex]{0.60\textwidth}{0.1pt}
NetID: \rule[-1ex]{0.20\textwidth}{0.1pt}

\section*{\textsl{Einstein's Universe} Term Exam 6}
\setcounter{problem}{1}

""")
    pindx = np.argsort(np.random.uniform(size=nproblem))
    for problem, indx in enumerate(pindx):
        print(problems[indx])
        print(r"""
\vfill ~
""")
        if problem == 3:
            print(r"""
\clearpage

""")
    print(r"""
\cleardoublepage

""")

print(r"""
\end{document}
""")
