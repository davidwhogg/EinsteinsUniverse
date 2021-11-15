import numpy as np
import pylab as plt
np.random.seed(17)
plt.rc('font', size=8)
nproblem = 8 # magic
nstudent = 115 # magic

problems = [r"""\begin{problem}
(From Problem Set 4, problem 1)
Roughly speaking, what is the rest-mass energy of a baseball?
That is, what is the energy equivalent of the mass of a baseball?
Use $E=m\,c^2$ and give your answer in Joules.
\end{problem}""", r"""\begin{problem}
(From Lecture)
Einstein didn't write down $E=m\,c^2$ originally. What equation did he
write down, for which $E=m\,c^2$ is a special case?
\end{problem}""", r"""\begin{problem}
(From Problem Set 4, problem 2)
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
(From Lecture)
If you bring together two protons and two neutrons in a fusion
reactor, they will combine to make one helium nucleus. When that
reaction happens, the nucleus will radiate some energy (in the form of
photons). Will the He nucleus have a mass that is greater than, equal
to, or less than the combined mass of two protons and two neutrons?
\end{problem}""", r"""\begin{problem}
(From Lecture)
In normal space, the straight line (or geodesic) is the path of \emph{shortest
total distance} between two points. In spacetime, the geodesic is the path
of what?
\end{problem}""", r"""\begin{problem}
(From Problem Set 4, problem 3)
When the elevator is accelerating downwards, is the magnitude of the
normal force from the elevator floor on the package greater than, smaller than,
or equal to $m\,g$?
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
\examheader{Term Exam 4}

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
