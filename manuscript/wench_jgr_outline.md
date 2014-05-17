# Title

## Abstract

## Introduction
- Stress is important, hard to quantify

- Topography creates substantial stress fields in high-relief areas
    - Both weight of topography ($\rho g z$) and shear stresses from slope
 
- Topographic stresses may influence fault activity
    - put faults nearer to or farther from failure
    - reorient shear stresses on faults
    - interaction of earthquake-rupture with heterogeneous static stresses

- Topographic stresses may be used to constrain tectonic stress in active fault
  environments
    - S = M + T + P = $\phi$

- We want to do both
    - Wenchuan earthquake is a good candidate
        - large, well studied
        - occurred at base of major topography
        - significant changes in fault rake that are vaguely correlated w/ topo
    - We calculate topographic stresses
        - magnitudes, orientations, etc.
        - compare with slip stuff
    - Then we constrain tectonic stresses
        - rakes, magnitudes, etc.


### Background on topographic stresses
- Orogenic/range scales: 
    - Molnar and Lyon-Caen, Copley, Dalmayrac and Molnar
    - coulomb wedges, 
    - thin sheets
    - Bollinger et al

- Smaller scales:
    - Liu and Zoback
	- Savage and Swolfs, etc for near-surface
    - anything else?

### Background on Wenchuan event
- Geology and physiography
    - big mountains
    - slow fault

- Earthquake stuff
    - size, etc.
    - variability of rake along strike
    - previous work on stress fields

## Topographic stress calculations
- Follow Liu and Zoback
- Statement of notation
- More coherent derivation (?) 
- Specifics of stress calculations for Eastern Tibet
	- make table
		- crustal parameters (density, poisson solid, ...)
		- Convolution parameters (grid spacing, kernel size, DEM size,
								  depth, vertical resolution)
	- Boussinesq details
	- Cerruti details (use top layer of Boussinesq calc, etc.)
	- Done with python, links to code (Halfspace module, run scripts)

- Stress projections on faults
	- Calculated at points in coseismic slip models
	- Resolved into $\tau_s$, $\tau_d$, $\sigma_n$
	- Compared to coseismic slip inversions (?)

### Topographic stress results

- Magnitude, directions of topographic stresses
    - magnitudes
        - cardinal directions (M diagonals)
        - principal stress directions--trends
        - $\sigma_n^M$ high
    - directions of $\tau^M$
    - coulomb stresses (fault mostly pushed away from failure)
    - 
- Topographic stresses are large, esp. on the SW Beichuan fault
- Stresses are opposed to fault slip for most fault segments
    - flats at depth are loaded in slip sense
- normal stresses are up to ~80 MPa

## Tectonic stress calculations
- We can use topographic stresses and the event of fault failure to constrain
  tectonic stresses at time of failure, based on Mohr-Coulomb failure criteria
- Then can use stress posteriors to solve for acceptable $(\phi, \mu)$

- Assumptions:
	- At failure, $\tau = \mu \sigma_n (1 - \phi)$
	- $S = M + T + L - \phi$
    - $T_{i,z} = 0$
	- $T$ is a linear function of $\rho g z$
	- $\phi$ is a constant fraction of total pressure
	- $\mu$ does not vary along the fault

- Bayesian inversion:
	- Construct priors so that $\rho g z \le \sigma_1^T \le 2.5 \rho g z$ and 
	  $0 \le \sigma_3^T \le \sigma_1^T$ and $0 \le \theta \le 2 \pi$ (direction
	  of $\sigma_1^T$)
	- Calculate shear rake on fault
	- Calculate misfit on rake using directional statistics
		- One-sided Von Mises distribution
		- appropriate uncertainty
	- Sample posterior through comparison with r[0,1)

- $\mu, \; \phi$ analysis
	- Sample $\phi$ from r[0,1)
	- solve for $\mu$
	- trim results for $\mu \le 0$ and $\mu \ge 1$
	- profit!

### Tectonic stresses
- Magnitudes and orientations
    - Consistent across all slip models
    - mode ~100°--110° (check)




- $\mu, \; \phi$ 
- numbers retained.
- $\tau$ and $\sigma_n^{eff}$.
- $\lambda$

## Discussion

- Magnitude, directions of topographic stresses
    - magnitudes
        - cardinal directions (M diagonals)
        - principal stress directions--trends
        - $\sigma_n^M$ high
    - directions of $\tau^M$
    - coulomb stresses (fault mostly pushed away from failure)
    - 
    - correlations with slip


- Comparison of stresses w/ those derived from other studies:
    - Luo and Liu 2010 Tectonophysics ($\tau$)
    - Zoback and Townend 2001
    - etc

- Comparison of friction, fluid pressure w/ other studies:
    - results from fault drilling
    - other model estimates






*need more description of $\tau^M$ results.*

*something about residual stresses being low compared to 2kyr accumulated
tectonic stress*

*slip weighting means that we are not too influenced by deep fault geometry*



## List of figures
1. map of eastern Tibet/ SB
1. schematic topo stress/faulting
1. 3D fault results [clean up]
1. normal stress / slip scatterplot, feng model [make vector]
1. posteriors for each fault model *
    - azimuth scatters
    - T posteriors
    - mu, phi
1. joint posteriors (larger) [put both T2 and T2/T1], rose
1. plots showing total shear and normal stress *
1. lorena-style plots *
1. some sort of summary/discussion figure (?)


to do:
make script to make plots
clean up figs
incorporate geodynamic discussions
get tong working
comparison w/ lorena's results
compare w/ borehole data

![Topographic normal stress $\sigma_n^M$ (colors), slip magnitude (contours,
1 m interval) and hanging-wall topography on the Feng et al. [2010] model of
the Beichuan fault. Note the suppression of fault slip where normal stress is
highest, such as below the Pengguan massif (P).
\label{fig:feng_slip_sig_n_beich} ](../figures/feng_slip_sig_n_beich.png)
