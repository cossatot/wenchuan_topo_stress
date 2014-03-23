# Topographic stresses and the Wenchuan earthquake

## Abstract

## Introduction
Stress is of fundamental importance to many processes in the earth. During
deformation, both the isotropic (pressure) and anisotropic (shear) components
of stress exert control on the deformation state of the earth at any point in
the brittle regime. However, unlike other fundamental quantities such as
temperature, stress is typically difficult to measure *in situ*. Therefore,
stress is often treated in a semi-quantitative manner, with an emphasis on
directions and relative magnitudes of the principal stresses locally or
regionally. These values are commonly derived from strain, for example from
studies of earthquake focal mechanisms or geodetic velocity fields.

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
the largest and steepest escarpments on Earth (Figure 1), and has a well-
studied coseismic slip distribution displaying significant along-strike changes
in kinematics that may be caused by changes in topographic shear stress along
the fault. Additionally, because the earthquake occurred after ~2000 years of
seismic quiescence, postseismic stresses in the lithosphere are likely to be
negligable, suggesting that the stress state on the faults at the time of
rupture can be described as the sum of topographic, lithostatic, and
accumulated tectonic stresses. This allows us to use the Mohr-Coulomb failure
criterion to bracket the tectonic stress field, pore fluid pressure, and
friction on the fault at failure.

*Need more here*

### Previous work on topographic stresses
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
Albania. Bollinger et al [2004] showed how increased normal stress on the
Main Himalayan thrust due to loading of the high Himalayan massifs locally
suppressed microseismicity and increased fault locking.

Aspects of topographic stresses are also found in common models of orogenic
dynamics. For example, thin viscous sheet models [refs] for lithospheric
deformation incorporate the ideas of constant horizontal stress with variable
vertical stress due to topographic variation. Critical taper models for thrust
or extensional wedges [e.g. Dahlen, 1990; Xiao et al. 1991] incorporate both
variation in vertical stress due to changing elevation as well as a shear
stress contributed by the slope of the wedge surface.

The contributions of variable topography to the full stress field (not simply
the vertical stress) in the elastic upper crust has been studied on smaller
spatial scales. McTigue and Mei [1981] and Savage and Swolfs [1986]
investigated the stress components from long, symmetric ridges and showed how
horizontal tension is induced under ridge crests and horizontal compression is
induced under valleys, mostly due to shear stresses generated by slopes. Liu
and Zoback [1992] investigated whether the topographic stresses generated by
the mountains around Cajon Pass (California, USA) contributed to the observed
left-lateral shear stress on a shallow portion of the right-lateral San Andreas
fault. In their study, they developed methods for calculating the full (six
component) stress tensor field from arbitrary topography based on elastic
halfspace techniques, where previous solutions were limited to two dimensions
and required topography to be mathematically-defined (e.g., sinusoidal).

*Luttrell?*

comparison:

- we do not incorporate Moho topography (deep, small compared to change at  Andean plate boundary

- Topographic calculations are similar, though we do Cerruti correction

- We solve for tectonic stress differently: we explicitly calculate whole stress tensor at each point (M + L + T) and use rake as constraint on allowable stresses.  We also use a Bayesian search instead of a minimization, yielding a PDF of the stress results.  We consider T1, T3, and rake instead of just T1 and rake.
- We use both normal and shear stresses to constrain pore fluid pressure and friction.

### The 2008 Wenchuan, China earthquake
The 2008 *M*7.9 Wenchuan, China earthquake is one of the most devastating
earthquakes in recent history. It is also extremely well-studied, and as such
only relevant information will be summarized here. For an in-depth review and
discussion of the earthquake, see Zhang et al. [2010]. The earthquake occurred
on the Beichuan and Pengguan faults at the base of the central and northeastern
Longmen Shan, a mountain range that forms the eastern margin of the Tibetan
plateau. Total relief across the central Longmen Shan is around 4 km, though
relief subsides somewhat to the northeast. The central and southwestern Longmen
Shan is the steepest margin of the Tibetan plateau [Clark and Royden, 2000] and
one of the highest and steepest escarpments on earth. This is most apparent in
the southwestern portion of the earthquake rupture, where the extremely steep
Pengguan massif, a Precambrian crystalline massif in the hanging wall of the
Beichuan thrust, where elevations >4 km drop to ~1200 m in as little as 6
km map distance (Figure 2).

Strain accumulation along the Longmen Shan faults is very slow; before the
earthquake, some workers had assumed that the fault was inactive [refs], though
GPS geodesy in the region indicated 4 ± 2 mm a$^{-1}$ of contraction across the
eastern Tibetan margin [Zhang et al., 2004]. Densmore et al [2007] performed an
extensive neotectonic investigation of the Longmen Shan faults, and showed that
...


## Topographic stresses on the Longmen Shan faults
*need an intro paragraph*

### Topographic stress tensor field calculations

#### Analytical description

We calculate the stress tensor field induced by topography throughout eastern
Tibet using methods based on elastic halfspace techniques developed by Liu and
Zoback [1992]. They show that the topographic stress tensor field can be
determined by a convolution of a topographic loading function with Green's
functions describing the stresses in an elastic halfspace due to a point load
at the surface (in our notation):

$$M(x, y, z) = G(x, y, z) * F(x, y)$$

where $M(x,y,z)$ is the topographic stress tensor field, $G(x,y,z)$ is the set
of Green's functions for the six stress independent stress tensor elements, and
$F(x,y)$ is the field of forces on the halfspace surface due to topographic
loading. In our notation and calculations, $x$ is east-west (positive is east),
$y$ is north-south (positive is north), and $z$ is up-down (positive is
down). Computation of $M$ is performed in two steps: First, the stress field
from the vertical component of the topographic load is calculated using the
vertical loading function $F_v(x,y)$ and Green's functions $G^B(x,y,z)$ derived
from Boussinesq's solutions for stresses in a halfspace due to a vertical point
load on the halfspace surface

$$M^B(x, y, z) = G^B(x,y,z) * F_v(x, y) \; ,$$

where $F_v(x,y) = \rho g h(x,y)$ and $h(x,y)$ is the negative elevation at
point $(x,y)$. Second, a correction is applied for shear and spreading forces
in the rock above the halfspace and the irregular surface boundary condition
through a convolution of Green's functions $G^C(x,y,z)$ constructed from
Cerruti's solutions for a horizontal point source load on the halfspace surface
and a horizontal loading function $F_{hor}(x,y)$. The horizontal loading
function is decomposed into two orthogonal components, $F_{hor, \, xz}(x,y)$
and $F_{hor, \, yz}(x,y)$, which are

\begin{equation}
F_{hor, \, xz}(x,y) = ( \rho g h(x,y) + \sigma_{xx}^B(x,y,z) + T_{xx} )\,  \frac{\partial h}{ \partial x}  + (\sigma_{xy}^{B}(x,y,z) + T_{xy}) \frac{\partial h}{ \partial y}
\label{eqn:f_hor_xz}
\end{equation}

and

\begin{equation}
F_{hor, \, yz}(x,y) = ( \rho g h(x,y) + \sigma_{yy}^B(x,y,z) + T_{yy} )\,  \frac{\partial h}{ \partial y}  + (\sigma_{xy}^{B}(x,y,z) + T_{xy}) \frac{\partial h}{ \partial x}\; . 
\label{eq:f_hor_yz}
\end{equation}

$\sigma_{ij}^B$ is the stress component *ij* from the vertical (Boussinesq)
load evaluated at $z=0$, and $T_{ij}$ is the tectonic stress component *ij*, which is considered
to be zero for the topographic stress calculation. The horizontal loading
functions are convolved with the Green's functions independently and then
summed:

$$M^C(x, y, z) = G^C(x,y,z) * F_{hor, xz}(x, y) + G^C(x,y,z) * F_{hor, yz}(x, y)$$

The total topographic stress field is then calculated as 

$$M(x,y,z) = M^B(x,y,z) + M^C(x,y,z) \; .$$

#### Numerical implementation


These calculations were implemented in Python (v. 2.7.3) using NumPy (v. 1.7)
and Pandas (v. 12). We have created an open-source Python package called
'halfspace' to perform topographic loading calculations in a reasonably
automated way; it is available at https://github.com/cossatot/halfspace and is
being expanded to encompass a wide range of elastic stress and strain solutions
as time permits. All data and scripts for this particular project are available
at https://github.com/cossatot/wenchuan_topo_stress. 

Topography was taken from the CGIAR-CSI v.3 release of the Shuttle Radar
Topographic Mission Digital Elevation Model (DEM) at 1 km nominal resolution.
The DEM was projected from native WGS84 geographic coordinates to UTM zone 48N,
decreasing the nominal horizontal resolution to 851 m. Green's functions for
the Boussinesq and Cerruti point-source solutions were calculated in large
square 2-D arrays at a constant depth (see Table 1 for model parameters).
A mask was applied to each Green's function array such that values outside the
kernel radius (i.e. the 'corners' of the array) were zero. Because of
singularities in the Green's functions at depth $z=0$, we use $\sigma^B(x,y,z)$
with $z=851 \, m)$, the shallowest level of our calculations, in construction
of the horizontal loading functions in Equations \ref{eqn:f_hor_xz} and
\ref{eqn:f_hor_yz}. Convolutions were performed as multiplications in the time
domain, and were done separately for each depth.

Parameter	          					Value       Unit
---------            					------      ----
horizontal spacing	 				 	851         m
vertical spacing     				 	1000        m
minimum depth							851			m (below sea level)
maximum depth							35851		m (below sea level)
density ($\rho$)     				 	2700        kg m$^{-3}$
g                    				 	9.81        m s$^{-2}$
Green's function kernel radius        	9e5         m
Lame's param (1)						1			-
Lame's param (2)						1			-


Table: Parameters for numerical calculations of topographic stresses.

### Topographic fault stress calculations

Topographic stresses on the Wenchuan faults are calculated on point sets
representing the faults taken from coseismic slip models. We use the coseismic
slip models of Shen et al. [2009], Feng et al. [2010], Qi et al. [2011], Zhang
et al. [2012], and Fielding et al. [2013], and discard points above 851 m
below sea level, as this is above the top of our halfspace model. The six
directional stress tensor component are calculated at each point in the fault
models through linear interpolation. Because the fault points are completely
surrounded by the grid nodes at which topographic stresses were calculated and
those nodes are spaced <1 km apart, the fault points cannot be more than a few
hundred meters from the nearest grid node, so more sophisticated interpolation
techniques (e.g., based on splines) are not necessary. We then resolve the 
topographic fault normal stress $\sigma_n^M$, down-dip shear stress $\tau_d^M$
and strike-slip shear stress $\tau_s^M$ at each point in the coseismic slip
models.

## Calculations of tectonic stress, fault friction and pore fluid pressure

Faults fail in earthquakes when the shear stresses on the fault overcome the
frictional stresses resisting slip on the fault. At the point of failure, the
shear stress and normal stress are equal, as in the familiar Coulomb failure
criterion $\tau = \mu \sigma_n (1 - \phi)$ where $\mu$ is the coefficient
of static friction on the fault and $\phi$ is the fluid pressure.

Quantifying the stress, friction and pore fluid pressure involved in faulting
is a major challenge in studies of faulting and orogenic dynamics [e.g. refs].
Previous workers have demonstrated that by quantifying topographic stress,
other components in the Coulomb stress balance may be bracketed [e.g., Cattin
et al.,1997; Lamb, 2006; Luttrell et al., 2011]. Each of these studies uses
somewhat different approaches and scales; ours are most similar to those of
Luttrell [2011], although there are significant differences[, as discussed
below].

We estimate the tectonic stresses $T$, fault friction $\mu$ and pore fluid
pressure $\phi$ on the Wenchuan faults at the time of fault failure through
a Bayesian inversion to estimate tectonic stresses consistent with published
coseismic slip models, and then a second analysis [need a better description]
to estimate fault friction and pore fluid pressures consistent with the
posterior stresses. Our methods yield joint probability distributions for the
parameters we estimate, illustrating both the likelihood of values for each
parameter and the tradeoffs between them. 


### Description of the stress state

We consider the complete stress tensor $S$ at a point in the crust to be
$S = M + T + L$, where $M$ is the topographic stress tensor as described above,
$T$ is the tectonic stress tensor, and $L$ is the lithostatic pressure tensor.
In our analysis, $M$ is a full stress tensor with independent and non-zero
values for each element; $L$ has only the principal stresses $L_{xx}$, $L_{yy}$
and $L_{zz}$, which all equal $\rho g z$ and off-diagonal (shear) stresses are
zero; and $T$ has only horizontal stresses $T_{xx}$, $T_{yy}$ and $T_{xy}$,
which are assumed to increase linearly with depth so that the entire upper
crust is near the critical failure envelope [e.g., Zoback and Townend], and
are therefore parameterized as scalars multiplied by lithostatic pressure. 

Therefore, the full stress tensor at a point is
\begin{equation}
S = \begin{pmatrix}
    M_{xx} + T_{xx} + L{xx} & M_{xy} + T_{xy}  &   M_{xz}  \\
	M_{xy} + T_{xy}  &   M_{yy} + T_{yy} + L{yy} & M_{yz}  \\
	M_{xz}          &   M_{yz}              M_{zz} + T_{yy} + L{yy}
	\end{pmatrix} \; .
\label{eqn:stress_tensor}
\end{equation}

$\phi$ is considered to be a scalar between zero and one that expresses pore
fluid pressure as a fraction of total pressure (the mean of the eigenvalues
of $S$) at each point on the fault. $\mu$ is the coefficient of static friction
and is considered constant along the fault.


### Bayesian inversion of tectonic stresses

We invert topographic stresses and coseismic slip models for tectonics stresses 
through a Bayesian process in which we do stuff.

We choose priors for the magnitudes and orientation of the maximum and minimum
principal tectonic stresses. The maximum principal stress is sampled from a
uniform distribution between [?] $\rho g z$ and 2.5 $\rho g z$. The minumum
principal stress is sampled from a uniform distribution between 0 and the value
for maximum stress. Because the Wenchuan event was an oblique reverse faulting
earthquake, both the maximum and minimum (horizontal) stress directions have to
be positive as they are greater than the vertical stress. The stress
orientations are taken as the azimuth of maximum tectonic stress and are sampled
uniformly from 0 to 360$^{circ}$.

For each of 100,000 iterations, unique samples for each of the priors are
drawn. Then, the complete stress tensor $S$ is constructed for each fault point
in a coseismic slip model. The rake of the maximum shear stress $\lambda^S$ on
each point on the fault is then calculated, and compared with the coseismic
slip rake $\lambda^D$ at that point. Then, a weighted mean misfit is
determined:

\begin{equation}
\bar{\lambda}^m = \sum \nolimits_{i=1}^n \frac{(\lambda^S_i - \lambda^D_i) * D_i} {\bar{ D}}\label{eqn:rake_misfit}
\end{equation}

Finally, the relative likelihood of each model is taken as 
\begin{equation}
p (D | T) = \frac{ \exp ( \kappa \cos \bar{\lambda}^m )} {\exp (\kappa \cos \bar{\lambda}^m_{\min})}
\label{eqn:rel_likelihood}
\end{equation}

$\kappa$ = 8.529, which is calculated so that 68.2% of the Von Mises
distribution is within $\pi$/9, the estimated 1$\sigma$ uncertainty of the
coseismic slip models based on comparisons between rakes of high-slip fault
patches.
