---
title: 'Topographic stresses and the Wenchuan earthquake'
authhead: 'STYRON AND HETLAND'
titlehead: 'WENCHUAN TOPOGRAPHIC STRESS'
authoraddr: 'Corresponding author: Richard H. Styron, Department of Earth and Environmental Sciences, University of Michigan, 2534 CC Little Bldg., 1100 N. University Ave., Ann Arbor, MI 48104, USA (richard.h.styron@gmail.com)'
authors: 'Richard H. Styron \altaffilmark{1} and Eric A. Hetland \altaffilmark{1}'
altaffilnum: 1
altaffiltext: 'Department of Earth and Environmental Sciences, University of Michigan, Ann Arbor, Michigan, USA.'




abstract:
	Topographic stresses are big and stuff. 
...

# Introduction

> "And He has set up on the earth mountains standing firm, lest it should shake
> with you" 
>
> *The Holy Qur'an*, 15:16

Stress is of fundamental importance to many processes in the
earth. Both the isotropic (pressure) and anisotropic (shear)
components of stress exert control on the deformation state of the
earth at any point in the brittle regime.  However, unlike other
fundamental quantities such as temperature, stress is typically
difficult to measure *in situ*, without drilling-based
techniques. Therefore, stress is often treated in a semi-quantitative
manner, with an emphasis on directions and relative magnitudes of the
principal stresses, either locally or regionally [e.g., REFS]. These
estimates of stress are commonly derived from strain, for example from
studies of earthquake focal mechanisms [e.g., Micheal, 1984] or
geodetic velocity fields [e.g., REF].

In areas of substantial relief, high terrain and steep slopes generate
large stresses in the crust beneath and adjacent to the high
topography [REFs]. Because of the irregularity of topography in
mountainous regions, the stresses produced by topography are also
heterogeneous, and may play a prominent role in local or regional
deformation, particularly if the region is tectonically active. For
example, shear and normal stresses on a fault from topographic loading
may push a particular fault closer to or (as suggested by the Qur'an)
farther from failure, or reorient the net shear stress direction on a
fault. These effects may affect the localization or deformational
style in a region. Furthermore, heterogeneous topographic stresses on
a particular fault may affect the way earthquake ruptures propagate
across the fault plane, although the degree to which topographic
stresses effect faulting has received little attention.


In this work, we investigate the effects of topographic stresses on
the faults that ruptured in the Mw 7.9 2008 Wenchuan, China
earthquake.   This earthquake is an ideal candidate for study because
it occurred at the base of the Longmen Shan, one of the largest and
steepest escarpments on Earth (Figure 1), and has a well-studied
coseismic slip distribution characterized by significant along-strike
variations in coseismic slip rate. Additionally, because the
earthquake occurred after ~2000 years of seismic quiescence,
postseismic stresses in the lithosphere are likely to be negligible,
suggesting that the stress state on the faults at the time of rupture
can be approximated as the sum of topographic, lithostatic, and
accumulated tectonic stresses. We then use the Mohr-Coulomb failure
critereon to bracket the tectonic stress field, pore fluid pressure,
and static friction of the fault.


## Previous work on topographic stresses

Aspects of the topographic stresses and their relevance to tectonics
have been studied for some time. Jeffreys [-@jeffreys1924] noted that
the presence of high mountains is evidence that the Earth's crust can
support significant heterogeneous differential stresses over long time
periods. Dalmayrac and Molnar [-@dalmayrac1981] and Molnar and
Lyon-Caen [-@molnar1988] discussed how extensional deformation in the
high parts of orogens temporally coincident with contractional
deformation at the low-elevation margins of the orogen may be
explained by a spatially invariant, depth-integrated horizontal
compressive stress with spatially varying vertical stress field caused
by topographic variation. Richardson and Coblentz [-@richardson1994]
exploited this relationship in the central Andes to estimate
horizontal tectonic stresses through finite element modeling, and more
recently Copley et al. [-@copley2009] performed similar work in
Albania. Bollinger et al. [-@bollinger2004] showed how increased
normal stress on the Main Himalayan thrust due to loading of the high
Himalayan massifs locally suppressed microseismicity and increased
fault locking. Meade and Conrad [-@meade2008] also demonstrated that
the increased weight of the uplifting Andes influenced the Nazca-South
America convergence rate.

Aspects of topographic stresses are also found in common models of
orogenic dynamics. For example, topographic loading is central to thin
viscous sheet models [e.g., @birdpiper80; @flesch2010gpe] for
lithospheric deformation.  Critical taper models for thrust or
extensional wedges [e.g. @dahlen1990; @xiao1991] incorporate both
variation in vertical stress due to changing elevation as well as a
shear stress contributed by the slope of the wedge surface.  Critical
taper models also incorporate the idea that in a growing wedge,
progressively increasing topographic stresses may eventually prevent
continued slip on a given fault plane, and strain will instead be
transferred to the toe of the thrust wedge where the stress state is
more favorable.
 

The contributions of variable topography to the full stress field in
the elastic upper crust has been studied on smaller spatial
scales. McTigue and Mei [-@mctiguemei1981] and Savage and Swolfs
[-@savageswolfs1986] investigated the stress components from long,
symmetric ridges and showed how horizontal tension is induced under
ridge crests and horizontal compression is induced under valleys,
mostly due to shear stresses generated by slopes. Liu and Zoback
[-@liuzoback1992] investigated whether the topographic stresses
generated by the mountains around Cajon Pass (California, USA)
contributed to the observed left-lateral shear stress on a shallow
portion of the right-lateral San Andreas fault. In their study, they
developed methods for calculating the elastic stress tensor field
arbitrary topography, where previous solutions were limited to two
dimensions and required topography to be mathematically-defined (e.g.,
sinusoidal).

Luttrell [-@luttrell2011] inferred the coseismic shear stress changes
during the 2010 Mw 8.8 Maule, Chile earthquake, and using the
topographic stresses due to the overlying fore arc, constrained the
the stresses that led to this earthquake. In their study, they
calculated topographic stresses following a similar proceedure as Lui
and Zoback [-@luizoback1992] (which we describe below), although they
only considered the component of the topographic load that can be
described by convolving a Boussinesq solution with the
topography. Luttrell et al. [-@luttrel2011] also considered the
contribution to stresses due to bouyancy.




## The 2008 Wenchuan, China earthquake

The 2008 *M*7.9 Wenchuan, China earthquake is one of the most
devastating earthquakes in recent history (for an in-depth review and
discussion of the earthquake, see Zhang et al. [-@zhang2010]). Surface
rupture occurred along a 240 km segment of the Beichuan fault and a
parallel 72 km segment of the Pengguan fault [@xu2009] (Figure
\ref{fig:lms_map}). These faults lie at the base of the central and
northeastern Longmen Shan, a mountain range that forms the eastern
margin of the Tibetan plateau. Total relief across the central Longmen
Shan is around 4 km, though relief subsides somewhat to the
northeast. The central and southwestern Longmen Shan is the steepest
margin of the Tibetan plateau [@clarkroyden2000] and one of the
highest and steepest escarpments on earth.  This is most apparent in
the southwestern portion of the earthquake rupture, where elevations >
4000 m over the Pengguan massif (a Precambrian crystalline massif in
the hanging wall of the Beichuan thrust) drop to ~1200 m in as little
as 6 km map distance.

![Map of eastern Tibet and the Sichuan basin, showing active structures from
Styron et al. [-@styron2010]. Faults that ruptured in the 2008 Wenchuan
earthquake are shown in pink. GPS velocities are relative to the mean velocity
of sites within Sichuan basin, with 1$\sigma$ uncertainty, from the dataset of
Liang et al. [-@liang2013]. Beachball is from the Global CMT focal mechanism
solution for the 2008 Wenchuan earthquake. BF = Beichuan fault. PF = Pengguan
fault. P = Pengguan massif. Grey box shows the extent of Figure
\ref{fig:lms_stress_map}.  
\label{fig:lms_map}](../figures/lms_map.pdf)

Surface ruptures during the Wenchuan earthquake are highly variable
and show vertical (reverse-sense) displacements up to 9 m and
horizontal (right-lateral sense) displacements up to 5 m [Lin et al.,
2009; Liu et al., 2009; Xu et al., 2009]. **I'M NOT SURE IT IS THIS
CUT AND DRY, AS LARGE STRIKE-SLIP OFFSETS MAPPED IN SW AS NE, ETC, I
SUGGEST TO CUT: In general, vertical displacements are highest in the
southwestern to central portions of the Beichuan rupture and decrease
in the northeast, whereas horizontal offset is negligible in the
southwest but high in the central to northeast.** Coseismic slip
models constrained by seismic and geodetic data reveal a complicated
pattern of coseismic slip in the Wenchaun earthquake, with several
high-slip patches that dominate the seismic moment release and
significant variation coseismic slip rake along strike [e.g. Nakamura
et al., 2009; @shen2009; @tong2010, @feng2010; @zhang2011; @qi2011;
@fielding2013]. The variation in rake is such that the southwest
portions of the fault slipped largely in a reverse sense, while the
northeast portions sliped largely in a right-lateral sense.  This
change in rake is associated with a change in inferred fault
dip. Sections of faults that ruptured in the Wenchuan earthquake
(which we simply refer to as the "Wenchuan earthquake faults") with
shallow to moderate dips largerly ruptured as thrust, and sections
with steeper dips largely ruptured as strike-slip. Medina Luna and
Hetland [-@medinaluna2013] concluded that this relationship is
consistent with a uniform orientation of principal stresses, where the
variation of the dip of the fault leads to a change in the direction
of maximum fault shear stress, which they assumed to be the coseismic
slip rake.


## This study 

We seek to quantify the topographic stress field in the Longmen Shan
region, and on the Wenchuan earthquake faults
themselves. Specifically, we evaluate the extent to which topographic
stresses promote or inhibit slip in the 2008 Wenchuan earthquake.  If
topographically induced shear stresses on the fault are in roughly in
the same direction as the coseismic slip, then topographic loading
generall promotes coseismic slip (**FIGURE 2a**). If topographic
loading promoted slip across the entire Beichuan faults, the
earthquake would result in the outward spreading of the very high and
steep Longmenshan. On the other hand, if the topographic shear
stresses are roughly in the opposite direction of coseismic slip, then
topographic loading inibits coseismic slip. (**FIGURE 2b**). If
topographic loading resisted slip across the Beichuan failts, then
tectonic stresses would need to counteract the topographic stfault
stresses for the coseismic slip to result.  **DO YOU WANT TO KEEP THE
GPS SENTENCE IN? THERE IS A MISMATCH BETWEEN SEISMIC QUIESENCE AND NO
OR LOW TECTONIC STRESS: The very low GPS inferred pre-seismic strain
rates across the fault (Figure \ref{fig:lms_map}) had convinced many
researchers that the Longmen Shan fault zone was tectonically
quiescent [e.g.  ref].** Additionally, the horizontal component of
coseismic slip generally points away from the high topography of the
central Longmen Shan, which might suggest a topographic collapse of
the Longmenshan during the Wenchuan earthquake.  On a smaller scale,
the heterogeneity of coseismic slip in the earthquake may be
influenced by shorter wavelength variations in topography and
topographic stresses.



![Scenarios for topographic effects on rangefront thrust faulting. (a)
Topographic stresses promote thrust faulting. (b) Topographic stresses inhibit
thrust faulting.
\label{fig:topo_fault_scenarios}](../figures/topo_stress_possibilities.pdf)

Topographic stresses are only one component of the total stress field
in the crust [@molnar1988]. Coseismic slip in the Wenchaun earthquake
is due to the total accumulated stress on the faults, which also
includes components from lithostatic and tectonic stresses. (In the
present stuty, we do not consider stresses due to flexure [e.g.,
Luttrell et al., 2007] or bouancy [e.g., Luttrell et al, 2011].) By
quantifying both the topographic and lithostatic stresses, we can use
coseismic slip models to solve for the tectonic stress assuming that
(1) the total shear stress on the fault is in the direction of the
coseismic slip [e.g., McKenzie, 1969; Angelier, 1979] and (2) the
fault is at Mohr-Coulomb failure everywhere that is slipped.  If
topographic stresses are significant and produce shear in the
direction of fault slip, then for given values of static friction and
pore fluid pressure, we can calculate the amount of tectonic stress
that can be added to the ambient stress field before the faults should
rupture; given limited acceptable ranges for friction and fluid
pressure, we are essentially able to place maximum constraints on
tectonic stress. Alternately, if topographic stresses work against
coseismic slip, for given friction and fluid pressures we can estimate
the minimum magnitudes of tectonic stresses necessary to overcome
shear and frictional resistance to slip. In a scenario with complex
faulting and topography, it may be possible to put tight bounds on
minimum and maximum magnitudes and directions of tectonic stresses.
To account for the non-uniqueness of the solution, we use a Bayesian
Monte-Carlo methodology to estimate posterior probability density
functions (PDFs) of tectonic stresses, static fault friction, and pore
fluid pressure.





# Topographic stresses on the Longmen Shan faults

To quantify tectonic stresses on the Wenchuan earthquake faults, we first
calculate the topographic stress field in the upper crust throughout eastern
Tibet, then interpolate those stresses onto three dimensional models of the
faults taken from coseismic slip models. Finally, we can calculate topographic
shear and normal stresses on the faults and compare those to the coseismic
slip patterns.

## Topographic stress tensor field calculations

## Analytical description

**ALL EQUATIONS WILL NEED TO BE NUMBERED IN GRL, ALSO I CHANGED YOUR
  NOTATION SLIGHTLY TO BE MORE CONSISTENT AND REDUCE SOME
  REDUNDANCIES**


We calculate the stress tensor field induced by topography throughout
eastern Tibet using methods developed by Liu and Zoback
[-@liuzoback1992]. They show that the topographic stress tensor field
can be determined by a convolution of a topographic loading function
with Green's functions describing the stresses in an elastic halfspace
due to a point load at the surface. In our notation, the stress tensor
field due to topography, $M(x,y,z)$, is given by 
\begin{equation}
M(x, y, z) = G(x, y, z) * F(x, y) \; ,
\end{equation}
where $G(x,y,z)$ is a set of Green's functions for
the six stress tensor elements, and $F(x,y)$ is a topographic loading
function, described below.  We assume compressive stresses are
positive, and $x>0$ is east, $y>$ is north, and $z>0$ is
depth. Liu and Zoback [-@liuzoback1992] show that $M(x,y,z)$ can be decomposed into two components as
\begin{equation}
M(x,y,z) = M^B(x,y,z) + M^C(x,y,z) \; .
\end{equation}
$M^B(x,y,z)$ is the component of the stress field due to the vertical
loading of the topography, and is
\begin{equation}
M^B(x, y, z) = G^B(x,y,z) * F_v(x, y) \; ,
\end{equation}
where $G^B(x,y,z)$ are the Boussinesq solutions for stresses in a
halfspace due to a vertical point load on the surface (see Appendix A1) and $F_v(x,y) =
\rho g h(x,y)$. Note that $h(x,y)<0$ since $z<0$ is depth.
$M^C(x,y,z)$ is the component of the stress field due to the
mechanical coupling of the topography to the half-space, i.e., describing 
the lateral spreading forces in the rock above the halfspace, and is given by
\begin{equation}
M^C(x, y, z) = G_x^C(x,y,z) * F_{h, x}(x, y) + G_y^C(x,y,z) * F_{h, y}(x, y) \; ,
\end{equation}
where $G_i^C(x,y,z)$ are the Cerruti solutions for a
 horizontal point source load in the $i$ direction on the halfspace surface (see Appendix A1). The 
 the horizontal loading functions are given by
\begin{equation}
\begin{split}
F_{h, \, x}(x,y) = ( \rho g h(x,y) + \sigma_{xx}^B(x,y,z) + T_{xx} )\, \frac{\partial h}{ \partial x} \\
\quad + (\sigma_{xy}^{B}(x,y,z) + T_{xy}) \frac{\partial h}{ \partial y}
\end{split}
\label{eqn:f_hor_xz}
\end{equation}
and
\begin{equation}
\begin{split}
F_{hor, \, yz}(x,y) = ( \rho g h(x,y) + \sigma_{yy}^B(x,y,z) + T_{yy} )\, \frac{\partial h}{ \partial y} \\
\quad + (\sigma_{xy}^{B}(x,y,z) + T_{xy}) \frac{\partial h}{ \partial x}\; . 
\end{split}
\label{eqn:f_hor_yz}
\end{equation}

$\sigma_{ij}^B$ is the stress from the vertical (Boussinesq) load
evaluated at $z=0$, and $T_{ij}$ is the tectonic stress component,
which we neglect in the present calculations. **DO WE WANT TO COME BACK
TO THIS? WE SOLVE FOR TECTONIC STRESS BUT THEN ASSUME IT IS
ZERO?**.

## Numerical implementation

Topography was taken from the CGIAR-CSI v.4 release [@jarvis2008srtm]
of the Shuttle Radar Topographic Mission [@farr2007srtm] Digital
Elevation Model (DEM) at 1 km nominal resolution. The DEM was
projected from native WGS84 geographic coordinates to UTM zone 48N,
decreasing the nominal horizontal resolution to 851 m. We assume a
Poisson halfspace, and Green's functions for the Boussinesq and
Cerruti point-source solutions were calculated at regular points in
large square, 2-D grid at each depth considered, with the point-source
centered in the grid (see Table \ref{table:convo_params} for model
parameters). The size of the grid was choosen so that the stresses due
to the point-source fall to zero well before the edge of the grid at
all depths considered. So that the Green's functions and the
topography were discretized on the same size grid, we pad the Green's
function array with zeros.  **IN IMAGE PROCESSING, MASK USUALLY
IMPLIED THAT NON-ZERO VALUES ARE ZEROED, I THINK YOU MEAN PAD HERE**
Because of singularities in the Green's functions at depth $z=0$, we
use $\sigma^B(x,y,z)$ with $z=851$ m, the shallowest level of our
calculations, in construction of the horizontal loading functions in
Equations \ref{eqn:f_hor_xz} and \ref{eqn:f_hor_yz}. Convolutions were
computed using a 2D fast Fourier transform **IS THERE A CITATION FOR
THE 2D FFT IN PYTHON**. All calculations were implemented in Python
(v. 2.7.3) using IPython [@perez2007ipython], NumPy (v. 1.7)
[@oliphant2007numpy] and Pandas (v. 12) [@mckinney2010]; additional
statistical analysis was performed with StatsModels [@seabold2010].
We created an open-source Python package to calculate topographic
stresses in a reasonably automated way, which is available at
\url{https://github.com/cossatot/halfspace}. The package is being
expanded to encompass a wide range of elastic stress and strain
solutions as time permits. All data and scripts for this particular
project are available at
\url{https://github.com/cossatot/wenchuan_topo_stress}.


Parameter	     				    | Value      | Unit
------------------------------------|------------|----------------
horizontal spacing	 			 	| 851        | m
vertical spacing   			 	    | 1000       | m
minimum depth						| 851		 | m (below sea level)
maximum depth						| 35851		 | m (below sea level)
density ($\rho$)   			 	    | 2700       | kg m$^{-3}$
g          			 	            | 9.81       | m s$^{-2}$
Green's function radius  	| 9e5        | m
Poisson ratio				| 0.25			 | -

Table: Parameters for numerical calculations of topographic
stresses. \label{table:convo_params} **LAME PARAMETERS HAVE UNITS, AND
GIVING THEM AS UNITLESS AND ONE IS INCONSISTENT WITH REST OF PAPER
THAT IS DIMENSIONAL**

## Topographic fault stress calculations

Topographic stresses on the Wenchuan faults are calculated on point
sets representing the faults taken from coseismic slip models. We use
the coseismic slip models of Shen et al. [-@shen2009], Feng et
al. [-@feng2010], Qi et al.  [-@qi2011], Zhang et al. [-@zhang2011],
and Fielding et al. [-@fielding2013], and discard points above 851 m
below sea level, as this is above the depth at which we compute
$G^C(x,y,z)$ **THE TOP OF THE HALF-SPACE IT Z=0**. The six stress
tensor components calculated at the regular grid point are linearly
interpolated to points describing the faults. Because the fault points
are completely surrounded by the grid nodes at which topographic
stresses were calculated and those nodes are spaced <1 km apart, the
fault points cannot be more than a few hundred meters from the nearest
grid node, so a higher order interpolation is not necessary. We then
project the topographic stress tensor to fault normal stress,
$\sigma_n^M$, down-dip shear stress, $\tau_d^M$ and strike-slip shear
stress, $\tau_s^M$ at each point in describing the fault geometry.

# Results of topographic stress calculations on the Wenchuan faults

Topographic stresses on the Wenchuan faults are in the 1--10s of MPa
range (Figure \ref{fig:lms_topo_stress_rot},
\ref{fig:fault_stress_3d}. Stresses are highest in the southwest,
beneath the Pengguan massif (the highest topography of the Longmen
Shan front), and decrease to the northeast. $\sigma_{zz}^M$ is
typically larger, though not substantially, than $\sigma^M_{xx}$ or
$\sigma^M_{yy}$. **THIS IS THE FIRST TIME YOU HAVE USED $\sigma^M$ AND
IT IS NOT DESCRIBED, PREVIOUSLY YOU USE $M$ FOR THE STRESS FIELD, WHY
A NEW SYMBOL, SHOULD THIS JUST BE $M_{ij}$ TO BE CONSISTENT WITH
PREVIOUS AND NEXT SECTIONS?** Maximum horizontal stress is not
typically aligned with either cardinal horizontal component, and is
typically larger than $\sigma^M_{zz}$ above 10 km. Maximum
$\sigma^m_{zz}$ is near 80 MPa, on the southwestern Beichuan fault
below the high peaks of the Pengguan massif, except for in slip models
containing near-horizontal fault segments in the mid-crust, where
$\sigma^M_{zz}$ reaches 100 MPa. Vertical shear stresses
($\sigma^M_{xz}$ and $\sigma^M_{yz}$) are on the order of 1 MPa, and
horizontal shear stress ($\sigma^M_{xy}$) is on the order of 0.1 MPa.

![Horizontal topographic stresses in the Longmen Shan region at 5 km
depth: black and red lines signify most and least compressive
horizontal stresses.  Other symbols are the same as in Figure
\ref{fig:lms_map}. Stresses shown are down-sampled from the
discretization used in the calculations by a factor of 6.
\label{fig:lms_topo_stress_rot}](../figures/lms_topo_stresses_rot.pdf)

Because the compressive stresses are near equal, $M$ contains a large
isotropic component and a smaller shear component. Consequently, $M$
resolves on the Wenchuan faults with a large $\sigma^M_n$ (median of
about 40-60 MPa for each slip model) and much smaller shear
stresses. The median $\tau^M_d$ is about -3 to -6 MPa in each slip
model, where values less than zero indicate normal-sense shear, and
$\sigma^M_s$ median values range from about -2 to **SHOULD THIS BE
NEGATIVE -1** 1 MPa, where values less than zero indicate sinistral
shear. On the steeper fault segments, topographic shear stresses are
typically normal-sinistral, as opposed to the dominant mode of
coseismic slip, which is reverse-dextral.

![Southwest-looking views of topographic stresses and coseismic slip on
selected slip models. All models share same lateral extent, but the
perspectives for B and C are more inclined than A.
(A) $\sigma_n^M$ (colors), slip magnitude (contours, 1 m interval) and
hanging-wall topography on the Feng et al. [-@feng2010] model of the Beichuan
fault. Note the suppression of fault slip where normal stress is highest, such
as below the Pengguan massif (P). Fault and topography share the same scale. No
vertical exaggeration.
(B) $\tau_d^M$ (colors) and dip slip (contours, 1 m interval) on the Qi et al.
[-@qi2011] 'rough' slip model.
(C) $\tau_s^M$ (colors) and strike slip (contours, 1 m interval) on the Qi et 
al. [-@qi2011] 'rough' slip model. 
\label{fig:fault_stress_3d} ](../figures/fault_stress_3d.pdf)

In contrast to the steeper fault segments, much of the
shallowly-dipping fault segments (the Pengguan fault and flats at the
base of the Beichuan fault, where present) have $\tau^M$ in the
direction of coseismic slip. The full stress tensor $M$ is not
significantly different in these locations, but because of the low dip
angle, $\sigma^M_{zz}$ contributes more significantly to $\sigma^M_n$
than to $\tau^M_d$, which is then dominated by horizontal compression,
leading to reverse-sense shear.  Additionally, the stresses caused by
the Pengguan massif locally resolve as right-lateral on these segments
as well. Coseismic slip on these fault patches is much lower than on
the steeper Beichuan fault, where the majority of slip occurred and
which is topographically loaded in the opposite shear sense.

Compellingly, similar patterns exist in the spatial distributions of
$\sigma^M_n$ and coseismic slip. Most obvious is the coincidence of
locally high $\sigma^M_n$ and locally low slip magnitude on the
southwestern Beichuan fault below the culmination of the Pengguan
massif, in an area of otherwise high slip (Figure
\ref{fig:fault_stress_3d}). These correlations exist for other fault
patches, but they are not as clear (Figure
\ref{fig:feng_slip_sig_n_scatter}). This raises the possibility that
$\sigma^M_n$ is capable of limiting slip once failure has occurred,
and may have implications for estimations of dynamic friction and the
completeness of stress drop during the earthquake. Preliminary
analysis of this is currently being performed, and will be described
in a forthcoming manuscript.

![Coseismic slip magnitude and $\sigma^M_n$ on the four segments of the Feng
et al. [-@feng2010] coseismic slip model. Trendlines are L1 regressions and do
not include points with no slip.
\label{fig:feng_slip_sig_n_scatter}](../figures/feng_slip_sig_n_scatter.png)



# Calculations of tectonic stress, fault friction and pore fluid pressure


**MOVE THIS PARAGRAPH TO THE DISCUSSION: Quantifying the stress,
friction and pore fluid pressure involved in faulting is a major
challenge in studies of faulting and orogenic dynamics [e.g.
@meissner1982; @oglesbyday2002].  Previous workers have demonstrated
that by quantifying topographic stress, other components in the
Coulomb stress balance may be bracketed [e.g., @cattin1997; @lamb2006;
@luttrell2011].  Each of these studies uses somewhat different
approaches. Our approach is most similar to that of Luttrell et
al. [-@luttrell2011], although there are significant differences: (1)
we use the ...  we consider a full range of tectonic stresses instead
of simply calculating the minimum principal tectonic stress, and we
also constrain fluid pressure and fault friction.**

**YOU USE $\phi$ FOR BOTH A STRESS AND A SCALAR, CLARIFIED BELOW, BUT
  I MIGHT HAVE MISSED SOME PLACES, I ALSO GENERALLY THINK OF THREE
  AMONTONS' LAWS, BUT I KNOW THAT GEOLOGISTS TEND TO ONLY CONSIDER IT
  TO BE ONE, AND THE FAILURE CRITERION IS USUALLS REFERRED TO AS
  MOHR-COULOMB, ALTHOUGH I TEND TO LIKE JUST COULOMB BETTER,
  ADDITIONALLY, NEITHER AMONTON OR COULOMB CONSIDERED THE AFFECT OF
  FLUIDS, SO ASCRIBING THIS TO THEM IS SOMEWHAT OVERLY GENEROUS**

Faults fail in earthquakes when the shear stresses on the fault
overcome the frictional stresses resisting slip on the fault [e.g.,
REFS]. We assume that the entire fault was at at the point of failure
when the Wenchuan fault initiated, and use the Mohr-Coulomb failure
critereon 
\begin{equation} 
\tau = \mu ( \sigma_n - \sigma_\p ) \; ,
\label{eqn:amonton_raw} 
\end{equation} 
where where $\mu$ is the
coefficient of static friction on the fault and $\sigma_p$ is the pore fluid pressure [e.g.,
Sibson, 1990]. We describe the pore fluid pressure using a scalar, $0
\leq \phi \leq 1$, which is the pore fluid pressure as a fraction of
total pressure, and so the failure critereon is
\begin{equation} 
\tau = \mu (1 - \phi) \sigma_n \; 
\label{eqn:amonton} 
\end{equation}
[e.g., Sibson, 1990]. We assume that both $\mu$ and $\phi$ are constant across the Wenchuan faults.
$\phi$ is the

We estimate the tectonic stress tensor field, $\mu$, and $\phi$
consistent with published coseismic slip models of the Wenchuan
earthquake using a Bayesian estimation.  Bayesian estimation yields
posterior probability density functions of the model parameters [e.g.,
Mosegaard and Tarantola, 1995]. We first estimate posteriors of $T$
cosistent with the coseismic slip models, and then estimate $\mu$ and
$\phi$ consistent with Mohr-Coulomb failure. The nature of Bayesian
estimation allows us to quantify both the relative likelihoods of
model parameters and the tradeoffs between them. 


## Description of the stress state

We consider the complete stress tensor, $S$, at a point in the crust to be
\begin{equation}
S = M + T + L \; ,
\end{equation}
where $M$ is described above, $T$ is the tectonic stress tensor, and
$L$ is the lithostatic pressure tensor. $L$ is isotrapic, with
diagonal components equal to $\rho g z$.  We assume that $T$ is
latterally homogeneous and only has horizontal stress components
(i.e., $T_{xz} = T_{yz} = T_{zz} = 0$, with $T_{xx}$, $T_{yy}$ and
$T_{xy}$ non-zero). We further assume that $T$ increases linearly with
depth so that the entire upper crust is near the critical failure
envelope [e.g., townend2000], are thus we parameterize the components
of $T$ as scalars multiplied by lithostatic pressure. **IT IS NOT
CLEAR WHY WE NEED THE FOLLOWING EQUATION - I SAY EITHER DELETE OR
EXPAND IT OUT REPLACING $T_{ij}$ AND $L_{kk} WITH $\rho g z$ - THERE
IS A POTENTIAL CONFUSION IN SYMBOLS AGAIN THOUGH, HERE YOU USE
$T_{ij}$ TO BE A STRESS, AND BELOW YOU USE $T_{ij}$ TO BE THE SCALAR**
The full stress tensor is then \begin{equation} S = \begin{bmatrix}
M_{xx} + T_{xx} + L_{xx} & M_{xy} + T_{xy} & M_{xz} \\ M_{xy} + T_{xy}
& M_{yy} + T_{yy} + L_{yy} & M_{yz} \\ M_{xz} & M_{yz} & M_{zz} +
L_{zz} \end{bmatrix} \; .  \label{eqn:stress_tensor} \end{equation}


## Bayesian inversion of tectonic stresses

We invert topographic stresses and coseismic slip models for tectonics
stresses using Bayesian methods, and making the common 'Wallace-Bott'
assumption (named after Wallace [1951] and Bott [1959]) that slip on
the fault occurs in the general direction of the maximum resolved
shear stress on the fault [e.g., McKenzie, 1969; Angelier, 1994]. We
estimate the tectonic stresses in light of the topographic stresses
and slip distributions through the relation 
\begin{equation} 
p(T|D) \propto p(T) \, p(D|T) \; , 
\label{eqn:bayes_rule} 
\end{equation} 
where $p(T)$ is the prior PDF (or *priors*) of $T$, $p(D|T)$ is the
likelihood of observing the coseismic slip distribution $D$ given the
tectonic stresses $T$, and $p(T|D)$ is the posterior PDF of $T$ given
$D$, which is the solution to the inversion [e.g., Mosegaard and
Tarantola, 1995]. Due to the unknown proportionality in equation
(\ref{eqn:bayes_rule}), our posterior only gives likelihood of $T$
relative to the most likely estiamte (MLE) [Tarantola, 2005]. We
follow a Monte-Carlo strategy, where samples of the prior PDF are
retained as samples of the posterior in proportion to $p(D|T)$ [e.g.,
Mosegaard and Tarantola, 1995].

We parameterize $T$ by the magnitudes and orientation of the maximum
and minimum principal tectonic stresses. We assume priors such that
the magintudes of principal tectonic stresses are equally likely
within bounds and that all orientations are equally likely.  Because
the Wenchuan event was an oblique reverse faulting earthquake, we
assume that total horizontal stresses are greater than the vertical
stress, which is satisfied if the tectonic stresses are positive.
Prior samples of maximum principal stress are taken from a uniform
distribution between $\rho g z$ and 2.5 $\rho g z$. Samples of the
minumum principal stress are from a uniform distribution between 0 and
the value for maximum stress.  We describe the orientation of the
tectonic stress using the azimuth of the maximum tectonic stress,
which are sampled uniformly from 0 to 360$^{\circ}$.

We test 100,000 unique samples drawn from the prior using a seeded
pseudorandom number generator. We test the same prior samples against
each of the coseismic slip models.  $S$ is then constructed for each
point discretizing the fault geometries in the coseismic slip
models. The rake of the maximum shear stress $\lambda^S$ on each point
of the fault is calculated and compared to the coseismic slip rake
$\lambda^D$ at that point. A weighted mean misfit is calculated by
\begin{equation}
\bar{\lambda}^m = \sum \nolimits_{i=1}^n \frac{(\lambda^S_i - \lambda^D_i) D_i} {\bar{ D}} \; ,
\label{eqn:rake_misfit}
\end{equation}
where $D$ is the coseismic slip and $\bar{D}$ is the average coseismic
slip in a given coseismic slip model. Finally, the relative likelihood
of each model is computed using a Von Mises distribution as
 \begin{equation}
p (D | T) = \frac{ \exp ( \kappa \cos \bar{\lambda}^m )} {\exp (\kappa \cos \bar{\lambda}^m_{\min})} \;,
\label{eqn:rel_likelihood}
\end{equation}
where $\kappa$ = 8.529, which is calculated so that the 68.2%
confidence interval the Von Mises distribution is within $\pi$/9
radians (20$^{\circ}$), the estimated 1$\sigma$ uncertainty of the
coseismic slip models based on comparisons between rakes of high-slip
fault patches (note that for a planar fault, $\tau$ at $\pi/9$ radians
from $\lambda_{max}$ is still >90% of $\tau_{max}$
[-@lisle2013]). Prior samples are retained in propotion to $p(D|T)$,
and the retained samples are then samples of the posterior.

## Analysis of friction and pore fluid pressure

**CLEAN UP NOTATION, YOU INTRODUCE NEW SYMBOLS IN THIS SUBSECTION, i.e., $S$ vs. $\sigma_n$ vs. $\sigma_n^S$**

Once the tectonic stress distributions consistent with the coseismic
slip models have been determined, we deduce the distributions of $\mu$
and $\phi$ assuming that the stress is at the failure criterion in
equation (\ref{eqn:amonton}). We do this in three steps: First, we
draw a random $\phi$ from a uniform distribution, assuming $0 \leq
\phi < 1$\@. We again use a seeded pseudorandom number generator, such
that each stress model has a uniquely assigned $\phi$ that is
consistent priors accross all coseismic slip models. Second, we
calculate $\tau^S$ and $\sigma_n^S(1-\phi)$ for each point on the
fault. Third, we solve Equation \ref{eqn:amonton} for $\mu$.  **I
DON'T UNDERSTAND THIS NEXT PART, IF ALL THE SAMPLES TRIED HERE ALL
HAVE MAX $\tau$ IN THE DIRECTION OF SLIP, THEN THERE IS NO ADDITIONAL
CONSTRAINT THAT CAN BE APPLIED, THIS SEEMS TO SAY THAT WE DISCARD
MODELS THAT DO NOT PRODUCE THE RIGHT SENSE OF SLIP (THRUST AND
RIGHT-LATERAL), BUT NONE OF THE SAMPLES IN THE POSTERIOR SHOULD HAVE
THAT** Finally, we filter the results so that only models with $0 \ge
\tau \ge 1$ are retained.

After this analysis has been done for all coseismic slip model, we
find the joint posterior (i.e., the posterior consistent with all of
the coseismic slip models) by taking the samples that are common to
all of the individual posteriors. We denote the joint posterior as
$p(P^{\mathrm{joint}} | D)$, where $P$ is the parameter of interest.


# T, $\mu$, $\phi$ results

## Individual slip models
Results for $T$, $\mu$ and $\phi$ are quite consistent across all coseismic
slip models (Figure \ref{fig:T_scatters}). Maximum compressive stress $T_{max}$
is broadly east-west for all models, with a mode trending at ~105$^{\circ}$.
$p(T_{max}|D)$ for each slip model increases from $T$ =0 to 0.5 or 1 before
essentially leveling off, though some slip models, particularly the Qi models,
show a slight decrease in [count? probability?] past the initial mode at $T$ =
0.5--1 (all values for $T$ are relative to $\rho g z$). The low [probability?
density?] below 0.5 indicates that lower tectonic stresses are unlikely to
overcome fault friction and topographic shear stresses resisting reverse-
dextral slip on the Wenchuan faults. $p(T_{min} | D)$ for each slip model has a
mode close to 0 and decreases rapidly, though all slip models show values for
$T_{min}$ up to 2.5. $T_{max}$ and $T_{min}$ do not display any particular
relationship aside from the requirement that $T_max \ge T_{min}$.

![Scatterplots with marginals $p(T|D)$ for each coseismic slip model. Values
are relative to lithostatic pressure. Inset rose diagrams are histograms of
azimuth of $\sigma^T_{max}$.  
\label{fig:T_scatters} ](../figures/T_scatters.pdf)

All slip models show $p(\phi | D)$ to be uniformly high from $\phi$ = 0 to
0.4--0.6 and to decrease linearly to $p(\phi)$ = 0 at $\phi$ = 1 (Figure
\ref{fig:mu_phi_scatters). $p(\mu | D)$ for all slip models has a mode at
$\mu$ = 0.1--0.4 and $p(\mu)$ decreases at higher values. $T_{max}$, $\phi$ and
$\mu$ are highly correlated, where higher values of $T_{max}$ are associated
with higher $\mu$ and lower $\phi$. Combinations of high $\phi$ and low $\mu$
would require much higher $T_{max}$ to overcome fault friction and cause slip,
and so are not represented in the posteriors. Since our maximum $T_{max}$ of
2.5 $\rho g z$ is quite high ($\approx 660$ MPa at 10 km), we view high $\mu$
and low $\phi$ combinations as extremely unlikely for the Wenchuan faults.
Similarly, combinations of very low $\mu$ and very high $\phi$ are associated
with very low $T_{max}$, and have a low probability density, as it is unlikely
that very low $T_{max}$ values can overcome sinistral and normal-sense
topographic shear stresses to cause the observed coseismic slip kinematics.

![Scatterplots of $p(\mu,\phi | D)$ for each coseismic slip model. Colors
in the scatterplot indicate magnitude of $\sigma^T_{max}$. Need color bar.
Contour lines indicate relative density of posteriors; darker lines mean higher
densities.
\label{fig:mu_phi_scatters}](../figures/mu_phi_fms.pdf)

## Joint posteriors
In order to concatenate the posteriors yielded by each coseismic slip model,
we define a final posterior as $p(T^{joint} | D)$, which comprises the samples
common to the posteriors from all slip models. Unsuprisingly, given the broad
similarity between the posteriors from the various slip models, 
$p(T^{joint}_{max} | D)$ is not substantially different from any of the 
constituent model posteriors. $p(\sigma^T_1 | D)$ has a somewhat more well-
defined mode at ~0.6.

$p(\phi^{joint} | D)$ 

In our estimation of $T$, $\phi$ and $\mu$, we have used the same random
combinations of $T$ and $\phi$ for each slip model, and then solved for $\mu$
so that the fault is at a critical stress state (Equation \ref{eqn:amonton}).
because of slight differences in fault attitude, location and slip among the
slip models, some variability exists in $\mu$ for each prior sample. We
therefore choose $p(\mu^{joint} | D)$ to be the median $\mu$ of each slip
model for each sample. $p(\mu^{joint}|D)$ has a mostly similar distribution
as $p(\mu | D)$ for any of the slip models; however, likely because it is an
average value, it lacks some density on the high-$\mu$ tail found in 
$p(\mu | D)$ for the individual slip models, though it is not similarly sparse
on the low-$\mu$ side, suggesting that low values for $\mu$ are more robust.

![Joint model results. 
(A) E-W and N-S components of $T$.
(B) Scatterplot of $\sigma^T_1$ and $\sigma^T_2$, with marginals.
(C) Scatterplot of $\mu$ and $\phi$, with marginals. Need color legend.
\label{fig:joint_posteriors}](../figures/temp_posteriors.pdf)


# Discussion

** MOVE THIS SECTION TO THE DISCUSSION:
comparison:
- we do not incorporate Moho topography (deep, small compared to change at Andean plate boundary
- Topographic calculations are similar, though we do Cerruti correction
- We solve for tectonic stress differently: we explicitly calculate whole stress tensor at each point (M + L + T) and use rake as constraint on allowable stresses. We also use a Bayesian search instead of a minimization, yielding a PDF of the stress results. We consider T1, T3, and rake instead of just T1 and rake.
- We use both normal and shear stresses to constrain pore fluid pressure and friction.
**

**MOVE THIS POINT TO THE DISCUSSION: Few studies have performed
similar quantification of static stress fields on faults (see Section
\ref{previous-work-on-topographic-stresses} for some examples). This
is important to address because most studies of fault rupture dynamics
assume either a homogeneous or stochastic shear stress distribution
[e.g., @oglesbyday2002] and few assume any variation in normal stress
[e.g., @aagaard2001] , despite the importance that stress variations
likely have in earthquake dynamics. By quantifying the topographic
stresses on the fault, including both the shear and normal components,
we may place empirical constraints on the potential heterogeneity of
fault stresses, which may then be compared to the coseismic slip
distribution to evaluate potential interactions.**



## Topographic stresses on the Wenchuan faults

Topographic stresses on the Wenchuan faults are of considerable magnitude:
$\tau^M$ ranges from about -20 to 10 MPa, which is on the order of inferred
stress drop in earthquakes [e.g. @allmann2009]. These stresses are likely
persistent over the lifespan of the topography, i.e. on the order of millions
to tens of millions of years, and vary little over the earthquake
cycle. Therefore, if shear stress drop is complete or near complete on these
faults, some residual tectonic stress must remain to cancel out $\tau^M$. 
$\sigma_n^M$ is larger, with maximum values around 80 MPa on the Beichuan
fault, and up to 100 MPa on thrust flats at depth.

Topographic stresses are generally opposed to the tectonic slip direction,
and therefore have to be overcome by tectonic stresses in order to produce
the observed rupture patterns. However, models with thrust flats at the base
of the faults show topographic loading in the direction of fault slip. This is
especially apparent in the Qi et al. [-@qi2011] model, where the thrust flat is
very broad. If such faults are able to accumulate shear stresses and transfer
them to the higher and steeper faults, topographic stresses may contribute to
the observed coseismic slip.

The spatial variation in topographic stresses decreases in frequency and
amplitude with depth. This is not surprising, because with increasing depth,
the stress field at any point is more sensitive to surface loads from a greater
region, and is less dominated by individual mountain-sized features. The
spatial variablity of stress with depth is similar to the spatial variablity of
coseismic slip in the models considered [e.g., @zhang2011], which are
similarly more smooth at depth. Some of the estimated slip variability is
likely partially due to the more limited detectability of displacements at
depth versus near the surface. However, the negative spatial correlations of
slip versis stress (especially $\sigma^M_N$) (Figures
\ref{fig:fault_stress_3d}, \ref{fig:feng_slip_sig_n_scatter}) suggest this is a
real signal: variations in $M$ influence rupture processes, leading to less
slip where topographic stresses are less favorable on the fault.

## Tectonic stresses, $\mu$, $\phi$

### Direction and magnitude of tectonic stresses
The maximum tectonic stress $\sigma^T_1$ is consistently oriented roughly E-W
in our results. This orientation is oblique to the Longmen Shan, which produces
oblique (right-lateral and reverse sense) shear on the Beichuan fault.
$\sigma^T_2$ is ~N-S oriented, and is only slightly larger than lithostatic
pressure. This stress configuration is compatible with the observed kinematics
of the Wenchuan faults, and in close agreement pre-earthquake stress
measurements near the rupture zone (Figure \ref{fig:lms_stress_map}), mostly
from borehole breakout data from 2-5 km depth [@heidbach2009], which is
the zone of maximum slip in the coseismic slip models. It is somewhat
discrepant with stress orientations estimated at ~800 m depth adjacent to the
Beichuan fault in the WFSD-1 borehole of the Wenchuan Earthquake Fault
Scientific Drilling Project several years after the 2008 earthquake [@cui2014],
which show $\sigma_{Hmax}$ to be more orthogonal to the fault trace, suggesting
that much of the right-lateral component of shear stress was released during
the earthquake. *check on this! At this depth, the results may not be that
different!  Look at magnitudes as well!*

![Topographic and tectonic horizontal stresses (taken from the most likely
estimates of $p(T|D)$ in the Wenchuan rupture region (black and red crosses)
with horizontal maximum stress orientation data taken from before the 2008
Wenchuan event from the World Stress Map [@heidbach2009] (purple arrows).
Other symbology is the same as in Figure \ref{fig:lms_map}. Stresses shown
are downsampled from grid resolution by a factor of 9.
\label{fig:lms_stress_map}](../figures/lms_map_stresses_rot.pdf)

However, the orientation of the tectonic (and total) stresses near the Wenchuan
faults shows a larger difference with the stresses that can be inferred from
regional deformation. For example, the presence of N-S contraction and E-W
extension throughout the high Tibetan plateau and much of the Himalaya [e.g.,
gimme ref; Taylor et al., 2003; Molnar and Lyon-Caen, 1988] indicates a roughly
N-S $\sigma^T_1$ and E-W $\sigma^T_2$. Because $\sigma^T_2$ is only slighly
above lithostatic pressure on the Wenchuan faults, it is quite possible that
the N-S compression in the Himalaya and Tibet, which is almost certainly due
to Indo-Asian plate collision, has almost completely decayed [attenuated?
diminished?] some 850 km northeast of the easternmost Himalaya. Therefore,
contraction across the Longmen Shan cannot easily be interpreted to directly
reflect stresses due to the Indo-Asian collision alone, unless some additional
mechanism of redirecting crustal stresses is incorporated.

The magnitudes of $\sigma^T_1$ and $\sigma^T_2$ are dominantly constrained on
the low end by our analysis; this is apparent by the sharp decrease in the
frequency of $p(T_{max}|D)$ below about 0.5. This indicates that $\sigma^T_1$
of at least ~13.25 MPa km$^{-1}$ is necessary to overcome topographic stresses
resisting reverse and right-lateral slip on the faults. 

### Values of $\phi$ and $\mu$

Our quantification of the stresses on the Wenchuan earthquake faults has
allowed us to estimate average values for $\phi$ and $\mu$ on the faults that
ruptured in the 2008 Wenchuan event, based on stress balance and critical
failure arguments. These values are weighted by the high slip patches

$\phi$...

Our highest likelihood estimates of $\mu$, which is the coefficient of static
friction on the fault immediately before failure, indicate values of 0.2--0.3.
These values are slightly lower than a value of 0.4 for friction at failure in
laboratory experiments on samples recoverd from the WFSD-1 drill hole into the
Beichuan fault [@kuo2014], though that value has a moderately high
likelihood in our posteriors. These values, however, are lower than typical
'Byerlee' type values derived from laboratory experiments on intact rock,
suggesting that slip occurred on preexisting faults because they are weaker
than optimally-oriented new faults.


## Slip on the Beichuan fault vs. optimally-oriented faults

The obliquity of slip on the Wenchuan earthquake faults suggests that these
faults may not be optimally oriented for slip given the total stress state in
the region of these faults. However, the Longmen Shan fault zone dates back to
the Indosinian orogeny, locally late Triassic (226-206 Ma) [-@yong2003] and has
had multiple episodes of reactivation since [e.g., @burchfiel1995; @wang2012],
accumulating tens of kilometers of shortening [e.g.,@hubbard2010]. Such
a mature fault system may be expected to have low coefficients of friction due
to processes such as gouge development [e.g., kuo2014], and therefore may slip
in non-optimal orientations; high $\phi$ values may also contribute to this
[e.g, @sibson1985].  

Our posterior estimates for $T$, $\phi$ and $\mu$ let us quantitatively
evaluate to what extent slip on the Wenchuan faults is more favorable than on
optimally-oriented faults with more typical friction coefficients under the
same stress conditions, assuming these optimal faults exist. Additionally, we
can evaluate the relative contributions of $T$, $\phi$ and $\mu$ on potential
fault weakening and reactivation. To explore these relationships, we perform
some preliminary analysis on a single fault model (from Zhang et al.
[-@zhang2011]) using a subset of 1000 samples drawn randomly from the joint
posteriors. Given the similarity of the fault models and of the posteriors for
each model, we do not expect that an analysis of all results on all fault
models will yield different conclusions.

First, we establish a metric with which to evaluate the favorability of slip
on a given fault plane, which we call the Coulomb failure ratio, or CFR:
\begin{equation}
CFR = \tau / \mu (\sigma_N - \phi)
\label{eqn:cfr}
\end{equation}
The CFR indicates whether a fault should faul under a given stress state:
A CFR > 1 indicates failure, while a CFR < 1 indicates fault stability. We then
calculate the CFR on each point in the model of the Beichuan fault (594 points)
based on the full stress field $S$ at each point on the fault, for each of 1000
samples of $T$, $\phi$ and $\mu$ drawn randomly from the posteriors (note that
each sample contains a value for $T$, $\phi$ and $\mu$ as a set, which is
persistent throughout the work in this study). We call this $CFR_f$. Then,
using the same $S$ and $\phi$, we calculate the CFR on an optimally-oriented
fault with $\mu=0.6$ and no cohesion, which we call $CFR_o$. Note these values
are typical for immature crustal faults [e.g. Townend and Zoback, 2004?], but
lower than laboratory-derived values; using higher values would decrease the
CFR. We then compare $CFR_o$ to $CFR_f$. When $CFR_o > CFR_f$, failure on an
optimal plane is preferred to failure on the Beichuan fault.

Figure \ref{fig:cfr_ratios} shows $log (CFR_o / CFR_f)$ plotted against $\mu$
on the Beichuan fault for all samples. Though considerable scatter exists even
in $log (CFR_f / CFR_o)$, it is clear that in most instances, slip on the
Beichuan fault is preferred over slip on an optimal fault, except for high
values of $\mu$. Because $T$, $\phi$ and $\mu$ can all affect fault
reactivation [e.g., @sibson1985], we compare the relative contributions of
each with a simple mutliple linear regression, using $\sigma^T_{EW}$ normalized
to [0,1) (the same range $\phi$ and $\mu$) as a proxy for $T$. The results are
shown in Table \ref{table:cfr_regress}. It is clear that $\mu$ is most strongly
correlated with $CFR_o/CFR_f$, followed by $\sigma^T_{EW}$ and then $\phi$;
nonetheless, all significantly affect the relative ease of faulting on the
Beichuan fault versus optimal faults.

![Comparison of Coulomb failure ratio (CFR) on the Beichuan fault from the
Zhang et al. [-@zhang2011] model to CFR on an optimally-oriented fault with
$\mu = 0.6$, versus estimated $\mu$ on the Beichuan fault. Values less than
0 (1 in linear space) indicate that slip is favored on the Beichuan fault, even
if it is non- optimally oriented. Values are calculated for each point in the
slip model for 1000 randomly-drawn samples from $p(T,\mu,\phi |D)$.
\label{fig:cfr_ratios}](../figures/cfr_ratios.png)

Parameter           | Coef.   | Std. Err. | t        | $P>|t|$      
--------------------|---------|-----------|----------|----------
Intercept           | -0.2566 | 0.0020    | -128.8   | <0.0001 
$\mu$               | 1.1168  | 0.0086    | 130.6    | <0.0001
$\sigma^T_{EW}$     | 0.9138  | 0.0048    | 191.2    | <0.0001
$\phi$              | 0.5762  | 0.0055    | 105.7    | <0.0001 

Table: Sensitivity of CFR ratios to relevant stress state parameters: Results
of multivariate linear regression of $CFR_f/ CFR_o)$ against $\mu$, $\phi$ and
$\sigma^T_{EW}$. \label{table:cfr_regress} 


# Conclusions

We have calculated the topographic stresses on the Wenchuan earthquake faults,
and used those stresses to constrain tectonic stresses, fault friction and
pore fluid pressure. From this work, we derive several conclusions:

Topographic stresses in the Longmen Shan region, and on the Wenchuan faults, 
are large. $\tau^M$ on the faults is up to |20| MPa, and $\sigma^M_N$ is up to
80 MPa, and higher (up to 100 MPa) on deep thrust flats present in some
coseismic slip models.

These topographic stresses generally resist the slip displayed during the 2008
Wenchuan earthquake. $\tau^M$ is opposed to the slip direction over much of the
fault, and high values of $\sigma^M_N$ increase the frictional resistance to
slip, potentially limiting slip magnitude in locations such as below the
Pengguan massif.

Because topographic stresses resist coseismic slip, the earthquake has to have
been caused by tectonic stresses. The results of our Bayesian inversion for
tectonic stresses, fault friction and pore fluid pressure indicate that the
maximum tectonic stress is oriented ~E-W and has a likely minimum of 13.25 MPa
km$^{-1}$. The minimum tectonic stress is oriented ~N-S and is fairly low.
The coefficient of static friction on the fault is estimated at about 0.2-0.3,
and fluid pressures are likely 0-0.5 of the total pressure.

Taken together, these results suggest that local stress conditions caused by
topographic loading are unfavorable to slip on the Wenchuan earthquake faults,
but because of the low friction coefficients and moderate fluid pressures,
slip occurred on these faults instead of more favorably-oriented faults
elsehere in the region.


# Appendix

## A1: Green's functions for point-source loads

Note that in these solutions, $\lambda$ and $\mu$ are re-defined, and are the
first and second Lame's parameters, respectively, instead of rake and fault
friction as in the body of the manuscript.

### Boussinesq's solutions for vertical point-source loads


\begin{equation}
\sigma _{xx}^B = \frac{ F_v }{ 2\pi } \left[ \frac{ 3x^2 }{ r^5 } 
+ \frac{\mu (y^2 + z^2)}{(\lambda + \mu) r^3 (z + r)}
- \frac{\mu z}{(\lambda + \mu) r^3} 
- \frac{\mu x^2}{ (\lambda + \mu) r^2 (z + r)^2 }\right]
\end{equation}

\begin{equation}
\sigma _{yy}^B = \frac{F_v}{2\pi } \left [ \frac{3y^2}{r^5}
+ \frac{\mu (x^{2} + z^{2})}{(\lambda + \mu) r^{3}(z + r)}
- \frac{\mu z}{(\lambda + \mu) r ^{3}}
- \frac{\mu y^{2}}{(\lambda + \mu ) r^{2} (z +r)^{2}} \right ]
\end{equation}

\begin{equation}
\sigma _{xy}^{B} = \frac{F _{v}}{2\pi} \left[ \frac{3xyz}{r^{5}}
- \frac{\mu x y (z + 2r)}{(\lambda + \mu) r^{3} (z + r)^{2}} \right]
\end{equation}

\begin{equation}
\sigma _{zz}^{B} = 3 F _{v} z^{3} / 2 \pi r^{5}
\end{equation}

\begin{equation}
\sigma _{xz}^{B} = 3 F _{v} xz^{2} / 2 \pi r^{5}
\end{equation}

\begin{equation}
\sigma _{yz}^{B} = 3 F _{v} yz^{2} / 2 \pi r^{5}
\end{equation}


### Cerruti's solutions for horizontal point-source loads

\begin{equation}
\sigma_{xx}^{C_x} = \frac{ F_{h,x} x }{2 \pi r^3} \left[ \frac{ 3x^2}{r^2}
- \frac{\mu}{(\lambda + \mu)(z+r)^2} (r^2 - y^2 - \frac{2ry^2}{r+z}) \right]
\end{equation}

\begin{equation}
\sigma_{yy}^{C_x} = \frac{ F_{h,x} x }{2 \pi r^3} \left[ \frac{ 3y^2}{r^2}
- \frac{\mu}{(\lambda + \mu)(z+r)^2} (3r^2 - x^2 - \frac{2rx^2}{r+z}) \right]
\end{equation}

\begin{equation}
\sigma_{xy}^{C_x} = \frac{ F_{h,x} x }{2 \pi r^3} \left[ \frac{ 3x^2}{r^2}
- \frac{\mu}{(\lambda + \mu)(z+r)^2} (r^2 - x^2 - \frac{2rx^2}{r+z}) \right]
\end{equation}

\begin{equation}
    \sigma^{C_x}_{zz} = \frac{ 3 F_{h,x} x z^2 }{2 \pi r^5}
\end{equation}

\begin{equation}
    \sigma^{C_x}_{xz} = \frac{ 3 F_{h,x} z x^2 }{2 \pi r^5}
\end{equation}

\begin{equation}
    \sigma^{C_x}_{yz} = \frac{ 3 F_{h,x} x y z }{2 \pi r^5}
\end{equation}



# References
