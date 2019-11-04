import numpy as np
import pylab as plt
np.random.seed(17)
plt.rc('font', size=8)
nproblem = 8 # magic
nstudent = 115 # magic

problems = [r"""\begin{problem}
(From Problem Set 4, problem 1)
What would be the kinetic energy of a baseball moving at half the
speed of light? Give your answer in Joules.
\end{problem}""", r"""\begin{problem}
(From Problem Set 4, problem 2)
How much energy does it take to heat up 1\,kg of water by 1\,deg C?
\end{problem}""", r"""\begin{problem}
(From Problem Set 4, problem 3)
How much uranium, very roughly, would it take to replace a 40-tonne carbon
footprint, if you could switch all that fossil-fuel usage over to
nuclear fission? That is, what did you get for the mass in uranium for
this problem?
\end{problem}""", r"""\begin{problem}
(From the reading)
For what discovery was Einstein awarded the Nobel Prize in 1921?
\end{problem}""", r"""\begin{problem}
(From the reading)
If you are in a rocket that is moving in the $x$-direction with
respect to the Earth at $0.75\,c$ and, inside the rocket, you are
moving at $0.75\,c$ in the $x$ direction with respect to the rocket,
how fast are you moving with respect to the Earth? No need to
calculate. All I want to know is: Are you moving closer to $0.75\,c$,
$0.95\,c$, or $1.5\,c$?
\end{problem}""", r"""\begin{problem}
(From Lecture, 2019-10-29)
If you bring together two protons and two neutrons in a fusion
reactor, they will combine to make one helium nucleus. When that
reaction happens, the nucleus will radiate some energy (in the form of
photons). Will the He nucleus have a mass that is greater than, equal
to, or less than the combined mass of two protons and two neutrons?
\end{problem}""", r"""\begin{problem}
(From Lecture, 2019-10-31)
How does the vomit comet make everyone inside experience weightlessness?
What are the pilots doing to make that happen?
\end{problem}""", r"""\begin{problem}
(From the Equivalence Principle Lab)
When the elevator is starting down
from the top floor, that is, when it is accelerating downwards, does the scale
show a larger weight or smaller weight than when the elevator was at
rest at the top?
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

\section*{\textsl{Einstein's Universe} Term Exam 4}
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
