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
    - S = M + T + P = $\lambda$

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

### Methods
#### Topographic stress calculations
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

#### Tectonic stress calculations
- We can use topographic stresses and the event of fault failure to constrain
  tectonic stresses, based on Mohr-Coulomb failure criteria
- Assumptions:
	- $S = M + T + P - \lambda$
    - $


