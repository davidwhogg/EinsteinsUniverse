import numpy as np
import pylab as plt
np.random.seed(17)
nproblem = 8 # magic
nstudent = 125 # magic

plt.figure(figsize=(9, 3))
N = 8192
xs = np.random.uniform(-4., 6., size=N)
ys = np.random.uniform(0., 2., size=N)
I = np.sin(5 * xs) < 2. * np.random.uniform(size=N) - 1.
xs = np.append(xs[I], np.random.uniform(-4., 6., size=N//2))
ys = np.append(ys[I], np.random.uniform(0., 2., size=N//2))
plt.plot(xs, ys, "k.")
plt.xlabel(r"x (meters)")
plt.ylabel(r"y (meters)")
plt.tight_layout()
plt.xlim(-4, 6)
plt.ylim(0., 2.)
plt.savefig("../tex/soundwave.png")

problems = [r"""\begin{problem} (From Problem Set 2)
Find a combination of a mass $m$, a length $L$ and a tension (force)
$T$ that has units of speed (length over time).
\end{problem}""", r"""\begin{problem} (From Problem Set 2)
Electrons are bound to a metal by a work function of $2\,\eV$.
Does a photon of wavelength $0.5\,\mu m$ have enough energy
to liberate one of those electrons?
\end{problem}""", r"""\begin{problem} (From the reading)
What, roughly, is the principle of relativity? State it in 30 words or less!
\end{problem}""", r"""\begin{problem} (From the reading)
Boltzmann, Fresnel, Maxwell: Which one of these scientists was
\emph{not} involved in creating the kinetic theory of gases?
\end{problem}""", r"""\begin{problem} (From the Newton's Second Law Lab)
A $50\,\g$ mass will have roughly what weight in $N$? Roughly!
\end{problem}""", r"""\begin{problem} (From the Interference and Diffraction of Light Lab)
You put red and green light through the same diffraction
grating. Which has a larger angular separation between the central
spot and the first bright spot in the experiment? Red or green? And
why?
\end{problem}""", r"""\begin{problem} (From Lecture on 2019-09-24)
Here's a picture of a traveling sound wave. Roughly what is its wavelength?
\end{problem}""", r"""\begin{problem} (From Lecture on 2019-09-??)
This wave on a string is moving to the left. The string is moving only
up and down. Draw arrows at points A, B, and C showing which way those
bits of string are moving.
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

\section*{\textsl{Einstein's Universe} Term Exam 2}
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
