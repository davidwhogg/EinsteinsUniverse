import numpy as np
import pylab as plt
np.random.seed(17)
plt.rc('font', size=8)
nproblem = 8 # magic
nstudent = 150 # magic

problems = [r"""\begin{problem}
(From Problem Set 6)
What would be the radius of a black hole with the mass of the Earth?
\end{problem}""", r"""\begin{problem}
(From Problem Set 6)
What is the distance between Earth and the source of GW170817?
\end{problem}""", r"""\begin{problem}
(From Problem Set 6)
What is the mean orbital speed $v$ of the star S2 in the Galactic Center?
\end{problem}""", r"""\begin{problem}
(From Problem Set 6)
In event GW150914, what were the three black-hole masses $M_1,M_2,M_3$?
\end{problem}""", r"""\begin{problem}
(From the reading)
In what year did LIGO make its first discovery of a black-hole merger?
\end{problem}""", r"""\begin{problem}
(From Lecture)
Roughly what is the orbital period of the International Space Station?
\end{problem}""", r"""\begin{problem}
(From the reading)
What happens when something crosses the horizon of the black hole?
\end{problem}""", r"""\begin{problem}
(From Lecture)
What---very roughly---is the (dimensionless) ratio of the mass of the black
hole at the center of the Milky Way to the total mass of the Milky Way? That is,
what fraction of the total mass of the Milky Way is the black hole?
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
\examheader{Term Exam 6}

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
