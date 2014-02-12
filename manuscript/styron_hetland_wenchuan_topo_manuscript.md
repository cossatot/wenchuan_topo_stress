# Topographic stresses and the Wenchuan earthquake

## Abstract

## Introduction
Stress is of fundamental importance to many processes in the earth. During
deformation, both the isotropic (pressure) and anisotropic (shear) components
<<<<<<< HEAD
of stress exert control on the deformation state of the earth at any point
in the brittle regime.  However, unlike other fundamental quantities such
as temperature, stress is extremely difficult to measure *in situ* and is
typically inferred from strain.

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
 
## Methods
### Topographic stress calculations
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

### Tectonic stress calculations
- We can use topographic stresses and the event of fault failure to constrain
  tectonic stresses at time of failure, based on Mohr-Coulomb failure criteria
- Then can use stress posteriors to solve for acceptable $(\phi, \mu)$

- Assumptions:
	- At failure, $\tau = \mu \sigma_n^{eff} (1 - \phi)$
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

## Results
### Topographic stresses
- Topographic stresses are large, esp. on the SW Beichuan fault
- Stresses are opposed to fault slip for most fault segments
- normal stresses are up to ~80 MPa

=======
of stress exert control on the deformation state of the earth at any point in
the brittle regime. However, unlike other fundamental quantities such as
temperature, stress is typically difficult to measure *in situ*. Therefore,
stress is often treated in a semi-quantitative manner, with an emphasis on
directions and relative magnitudes of the principal stresses locally or
regionally. These values are commonly derived from strain, for example from
studies of earthquake focal mechanisms or geodetic velocity fields.
>>>>>>> 9ab246c5a02b9a90cc6ec5b8a9bbb360a7160fd7

In areas of substantial relief, high terrain and steep slopes generate
proportionally large pressures and shear stresses in the crust beneath and
adjacent to the high topography. Because of the irregularity of topography in
mountainous regions, the stresses produced by topography are heterogeneous as
well, and may play a prominent role in local or regional deformation,
particularly if the region is tectonically active. For example, shear and
normal stresses on a fault from topographic loading may push a particular fault
closer to or farther from failure, or reorient the net shear stress direction
on a fault. These effects may affect the localization or deformational style in
a region.  Furthermore, heterogeneous topographic stresses on a particular
fault may affect the way earthquake ruptures propagate across the fault plane.

Though topographic stresses may be very heterogeneous, they may also be
precisely estimated, because topography and material parameters (such as
density) of constituent rocks are very well known compared to many other
parameters of interest. Therefore, in areas where topographic stresses are
a significant component of the total stress budget, these stresses may be used
in conjuction with information on the deformational condition of a location to
place quantitative constraints on other types of stresses and related
parameters such as fault friction and pore fluid pressure.

In this work, we study the effects of topographic stresses on the faults that
ruptured in the 2008 Wenchuan, China earthquake. This earthquake is an ideal
candidate for study because it occurred at the base of the Longmen Shan, one of
the largest and steepest escarpments on Earth, and has a well-studied coseismic
slip distribution displaying significant along-strike changes in kinematics
that may be caused by changes in topographic shear stress along the fault.
Additionally, because the earthquake occurred after ~2000 years of seismic
quiescence, postseismic stresses in the lithosphere are likely to be
negligable, suggesting that the stress state on the faults at the time of
rupture can be described as the sum of topographic, lithostatic, and
accumulated tectonic stresses. This allows us to use the Mohr-Coulomb failure
criterion to bracket the tectonic stress field, pore fluid pressure, and
friction on the fault at failure.

## Previous work on topographic stresses
Aspects of the topographic stresses and their relevance to tectonics have been
studied for some time. Jeffreys [1924] noted that the presence of high
mountains is evidence that the Earth's crust can support significant
heterogeneous differential stresses over long time periods[,placing bounds on
its rheology?]. Dalmayrac and Molnar [1981] and Molnar and Lyon-Caen [1988]
discussed how extensional deformation in the high parts of orogens temporally
coincident with contractional deformation at the low-elevation margins of the
orogen may be explained by a spatially invariant depth-integrated horizontal
compressive stress with spatially varying vertical stress field caused by
topographic variation. Richardson and Coblentz [1994] exploited this
relationship in the central Andes to estimate horizontal tectonic stresses
through finite element modeling, Copley et al [2009] performed similar work in
Albania.  Bollinger et al [2004] showed how increased normal stress on the
Main Himalayan thrust due to loading of the high Himalayan massifs locally
suppressed microseismicity and increased fault locking.

Aspects of topographic stresses are also found in common models of orogenic
dynamics. For example, thin viscous sheet models [refs] for lithospheric deformation
incorporate the ideas of constant horizontal stress with variable vertical stress
due to topographic variation. Critical taper models for thrust or extensional
wedges [e.g. Dahlen, 1990; Xiao et al. 1991] incorporate both variation in
vertical stress due to changing elevation as well as a shear stress contributed
by the slope of the wedge surface.

The contributions of irregular topography to the full stress field
(not simply the vertical stress) in the elastic upper crust has been studied
on smaller spatial scales. McTigue and Mei [1981] and Savage and Swolfs [1986]
investigated the stress components from long, symmetric ridges and showed how
horizontal tension is induced under ridge crests and horizontal compression
is induced under valleys, mostly due to shear stresses generated by slopes.
[martel sackung]
