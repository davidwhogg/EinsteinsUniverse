import numpy as np
import pylab as plt
np.random.seed(17)
plt.rc('font', size=8)
nproblem = 8 # magic
nstudent = 125 # magic

"""
# THIS FIGURE MAKES A LONGITUDINAL WAVE
plt.figure(figsize=(5, 1.5))
N = 8192
xmax = 20.
ymax = 4.
wavelength = 5.0
xs = np.random.uniform(0, xmax, size=N)
ys = np.random.uniform(0., ymax, size=N)
I = np.sin(2. * np.pi * xs / wavelength) < 2. * np.random.uniform(size=N) - 1.
xs = np.append(xs[I], np.random.uniform(0., xmax, size=N//2))
ys = np.append(ys[I], np.random.uniform(0., ymax, size=N//2))
plt.plot(xs, ys, "k.", ms=1.)
plt.xlabel(r"x (meters)")
plt.ylabel(r"y (meters)")
plt.tight_layout()
plt.xticks(np.arange(21))
plt.yticks(np.arange(21))
plt.xlim(0, xmax)
plt.ylim(0, ymax)
plt.savefig("../tex/soundwave.png", dpi=200)
"""

plt.figure(figsize=(5, 1.5))
N = 8192
xmax = 20.
ymax = 3.
wavelength = 5.3
xs = np.arange(0., xmax+1., 0.01)
ys = np.sin(2. * np.pi * xs / wavelength)
plt.plot(xs, ys, "k-")
plt.xlabel(r"x (meters)")
plt.ylabel(r"y (meters)")
plt.tight_layout()
plt.xticks(np.arange(21))
plt.yticks(np.arange(-5,5))
plt.xlim(0, xmax)
plt.ylim(-ymax, ymax)
plt.savefig("../tex/randomwave.png", dpi=200)

plt.figure(figsize=(5, 1.5))
wavelength = 5.0
xs = np.arange(0., xmax+0.0001, xmax/1000.)
ys = ymax / 2. + np.sin(2. * np.pi * xs / wavelength)
I = xs < 1.5 * wavelength
ys[I] = ymax / 2.
I = xs > 2.5 * wavelength
ys[I] = ymax / 2.
plt.plot(xs, ys, "k-")
xabc = np.array([8., 9.5, 10.5])
yabc = ymax / 2. + np.sin(2. * np.pi * xabc / wavelength)
plt.plot(xabc, yabc, "k.")
for l,x,y in zip(["A ", " B", " C"], xabc, yabc):
    ha = "left"
    if l == "A ": ha = "right"
    plt.text(x, y, l, ha=ha, va="top")
plt.arrow(10., 3.5, -3., 0., lw = 0.3, width=0.08, color="k")
plt.xlabel(r"x (meters)")
plt.ylabel(r"y (meters)")
plt.tight_layout()
plt.xticks(np.arange(21))
plt.yticks(np.arange(21))
plt.xlim(0, xmax)
plt.ylim(0, ymax)
plt.savefig("../tex/wavepulse.png", dpi=200)

problems = [r"""\begin{problem} (From Problem Set 2)
What, roughly, are the sizes of a water molecule, an iron atom, and a uranium
atom?
\end{problem}""", r"""\begin{problem} (From Problem Set 2)
Electrons are bound to a metal by a work function of $2\,\eV$.
Does a photon of wavelength $0.5\,\mu m$ have enough energy
to liberate one of those electrons?
\end{problem}""", r"""\begin{problem} (From Problem Set 2)
What would be the SI base units of the expression
$\displaystyle\sqrt{\frac{T\,L}{M}}$?
(Note that this may be \emph{different} from the expression
you had on your Problem Set.)
\end{problem}""", r"""\begin{problem} (From the reading)
Boltzmann, Fresnel, Maxwell: Which one of these scientists was
\emph{not} involved in creating the kinetic theory of gases?
\end{problem}""", r"""\begin{problem} (From the Newton's Second Law Lab)
A $50\,\g$ mass will have roughly what weight in $N$? Roughly!
\end{problem}""", r"""\begin{problem} (From the Interference and Diffraction of Light Lab)
You put red and green light through the same diffraction
grating. Which has a larger angular separation between the central
spot and the first bright spot in the experiment? Red or green? And
why (in 10 words or less)?
\end{problem}""", r"""\begin{problem} (From Lecture on 2019-09-30)
Here's a picture of a traveling wave on a pond, traveling to the left.
Roughly what is its wavelength?\\
\includegraphics{randomwave.png}
\end{problem}""", r"""\begin{problem} (From Lecture on 2019-09-28)
This wave on a string is moving to the left. The string is moving only
up and down. Draw arrows at points A, B, and C showing which way those
bits of string are moving.\\
\includegraphics{wavepulse.png}
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
\examheader{Term Exam 2}

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
