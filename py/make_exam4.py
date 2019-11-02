import numpy as np
import pylab as plt
np.random.seed(17)
plt.rc('font', size=8)
nproblem = 8 # magic
nstudent = 115 # magic

problems = [r"""\begin{problem}
(From Problem Set 4, problem xx)
foo
\end{problem}""", r"""\begin{problem}
(From Problem Set 4, problem xx)
bar
\end{problem}""", r"""\begin{problem}
(From Problem Set 4, problem xx)
yo
\end{problem}""", r"""\begin{problem}
(From the reading)
sup
\end{problem}""", r"""\begin{problem}
(From the reading)
damn
\end{problem}""", r"""\begin{problem}
(From Lecture, 2019-10-xx)
suh
\end{problem}""", r"""\begin{problem}
(From Lecture, 2019-10-xx)
dude
\end{problem}""", r"""\begin{problem}
(From the xxx Lab)
roar
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
