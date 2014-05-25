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

Stress is of fundamental importance to many processes in the earth. Both the
isotropic (pressure) and anisotropic (shear) components of stress exert control
on the deformation state of the earth at any point in the brittle regime.
However, unlike other fundamental quantities such as temperature, stress is
typically difficult to measure *in situ*, without drilling-based techniques 
(i.e., there is no remote sensing of stress in the earth). Therefore, stress is
often treated in a semi-quantitative manner, with an emphasis on directions and
relative magnitudes of the principal stresses locally or regionally. These
values are commonly derived from strain, for example from studies of earthquake
focal mechanisms or geodetic velocity fields.

In areas of substantial relief, high terrain and steep slopes generate
proportionally large pressures and shear stresses in the crust beneath and
adjacent to the high topography. Because of the irregularity of topography in
mountainous regions, the stresses produced by topography are heterogeneous as
well, and may play a prominent role in local or regional deformation,
particularly if the region is tectonically active. For example, shear and
normal stresses on a fault from topographic loading may push a particular fault
closer to or (as suggested by the Qur'an) farther from failure, or reorient the
net shear stress direction on a fault. These effects may affect the
localization or deformational style in a region. Furthermore, heterogeneous
topographic stresses on a particular fault may affect the way earthquake
ruptures propagate across the fault plane.

Though topographic stresses may be very heterogeneous, they may also be
precisely estimated, because topography and material parameters (such as
density) of constituent rocks are very well known compared to many other
parameters of interest. Therefore, in areas where topographic stresses are
a significant component of the total stress budget, these stresses may be used
in conjunction with information on the deformational condition of a location to
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
negligible, suggesting that the stress state on the faults at the time of
rupture can be described as the sum of topographic, lithostatic, and
accumulated tectonic stresses. This allows us to use the Mohr-Coulomb failure
criterion to bracket the tectonic stress field, pore fluid pressure, and
friction on the fault at failure.


## Previous work on topographic stresses
Aspects of the topographic stresses and their relevance to tectonics have
been studied for some time. Jeffreys [-@jeffreys1924] noted that the presence
of high mountains is evidence that the Earth's crust can support significant
heterogeneous differential stresses over long time periods Dalmayrac and
Molnar [-@dalmayrac1981] and Molnar and Lyon-Caen [-@molnar1988] discussed
how extensional deformation in the high parts of orogens temporally
coincident with contractional deformation at the low-elevation margins of the
orogen may be explained by a spatially invariant depth-integrated horizontal
compressive stress with spatially varying vertical stress field caused by
topographic variation. Richardson and Coblentz [-@richardson1994] exploited
this relationship in the central Andes to estimate horizontal tectonic
stresses through finite element modeling, Copley et al. [-@copley2009]
performed similar work in Albania. Bollinger et al. [-@bollinger2004] showed
how increased normal stress on the Main Himalayan thrust due to loading of
the high Himalayan massifs locally suppressed microseismicity and increased
fault locking.

Aspects of topographic stresses are also found in common models of orogenic
dynamics. For example, topographic loading is central to thin viscous sheet
models [e.g., @birdpiper80; @flesch2010gpe] for lithospheric deformation.
Critical taper models for thrust or extensional wedges [e.g. @dahlen1990;
@xiao1991] incorporate both variation in vertical stress due to changing
elevation as well as a shear stress contributed by the slope of the wedge
surface.  Critical taper models also incorporate the idea that in a growing
wedge, progressively increasing topographic stresses may eventually prevent
continued slip on a given fault plane, and strain will instead be transferred
to the toe of the thrust wedge where the stress state is more favorable.

The contributions of variable topography to the full stress field in the
elastic upper crust has been studied on smaller spatial scales. McTigue and Mei
[-@mctiguemei1981] and Savage and Swolfs [-@savageswolfs1986] investigated the
stress components from long, symmetric ridges and showed how horizontal tension
is induced under ridge crests and horizontal compression is induced under
valleys, mostly due to shear stresses generated by slopes. Liu and Zoback
[-@liuzoback1992] investigated whether the topographic stresses generated by
the mountains around Cajon Pass (California, USA) contributed to the observed
left-lateral shear stress on a shallow portion of the right-lateral San Andreas
fault. In their study, they developed methods for calculating the full (six
component) stress tensor field from arbitrary topography based on elastic
halfspace techniques, where previous solutions were limited to two dimensions
and required topography to be mathematically-defined (e.g., sinusoidal).

Luttrell [-@luttrell2011] performed a study very similar to ours in the region
of the 2010 8.8 Maule, Chile earthquake. They calculated stresses on the
megathrust from 




comparison:
- we do not incorporate Moho topography (deep, small compared to change at Andean plate boundary
- Topographic calculations are similar, though we do Cerruti correction
- We solve for tectonic stress differently: we explicitly calculate whole stress tensor at each point (M + L + T) and use rake as constraint on allowable stresses. We also use a Bayesian search instead of a minimization, yielding a PDF of the stress results. We consider T1, T3, and rake instead of just T1 and rake.
- We use both normal and shear stresses to constrain pore fluid pressure and friction.

## The 2008 Wenchuan, China earthquake
The 2008 *M*7.9 Wenchuan, China earthquake is one of the most devastating
earthquakes in recent history. It is also extremely well-studied, and as such
only relevant information will be summarized here. For an in-depth review and
discussion of the earthquake, see Zhang et al. [-@zhang2010]. Surface rupture
occurred along a 240 km segment of the Beichuan fault and a parallel 72 km
segment of the Pengguan fault [@xu2009] (Figure \ref{fig:lms_map}). These
faults lie at the base of the central and northeastern Longmen Shan, a mountain
range that forms the eastern margin of the Tibetan plateau. Total relief across
the central Longmen Shan is around 4 km, though relief subsides somewhat to the
northeast. The central and southwestern Longmen Shan is the steepest margin of
the Tibetan plateau [@clarkroyden2000] and one of the highest and steepest
escarpments on earth.  This is most apparent in the southwestern portion of the
earthquake rupture, where the extremely steep Pengguan massif (a Precambrian
crystalline massif in the hanging wall of the Beichuan thrust), is located and
elevations > 4000 m drop to ~1200 m in as little as 6 km map distance.

![Map of eastern Tibet and the Sichuan basin, showing active structures from
Styron et al. [-@styron2010]. Faults that ruptured in the 2008 Wenchuan
earthquake are shown in pink. GPS velocities are relative to the mean velocity
of sites within Sichuan basin, with 1$\sigma$ uncertainty, from the dataset of
Liang et al. [-@liang2013]. Beachball is from the Global CMT focal mechanism
solution for the 2008 Wenchuan earthquake. BF = Beichuan fault. PF = Pengguan
fault. P = Pengguan massif. Grey box shows the extent of Figures
\ref{fig:lms_topo_stresses_rot} and \ref{fig:lms_stress_map}.  
\label{fig:lms_map}](../figures/lms_map.pdf)

Coseismic slip on the fault is spatially variable. Surface ruptures on the 
Beichuan fault show vertical (reverse-sense) displacements up to 6.5 m and
horizontal (right-lateral sense) displacements up to 4.9 m. In general,
vertical displacements are highest in the southwestern to central portions of
the Beichuan rupture and decrease in the northeast, whereas horizontal offset
is negligible in the southwest but high in the central to northeast. The rake
of coseismic slip is consequently variable as well, from close to pure reverse
faulting in the southwest to dominantly right-lateral in the northeast. Shorter
wavelength variations in slip rake and magnitude are apparent, as well.
Coseismic slip models estimating slip at depth, derived from geodetic and
seismic data [e.g. @shen2009; @tong2010; @feng2010; @zhang2011; @qi2011;
@fielding2013] reproduce the surface offsets, but typically show even greater
displacements at depth.  Additionally, these coseismic slip models show that
slip at depth is concentrated into a small number of high-slip patches that
dominate the seismic moment release [e.g., @zhang2011]. 

Coseismic slip models also clearly show that the broad along-strike shift in
rake from reverse slip in the southwest to right-lateral slip in the northeast
is persistent at depth. This change in rake is associated with a change in
fault dip. Sections of the fault with mostly reverse slip have shallow to
moderate dips, where sections with mostly right-lateral slip have steeper dips.
Medina Luna and Hetland [-@medinaluna2013] concluded that this relationship is consistent
with a uniform stress tensor that produces maximum shear stresses in the
direction of coseismic slip on the variably-oriented fault segments. However,
the horizontal component of coseismic slip also generally points away from the
high topography of the central Longmen Shan, particularly the Pengguan massif
in the hanging wall of the Beichuan fault. This suggests that the very high
and steep mountains may be spreading outward.

![Scenarios for topographic effects on rangefront thrust faulting. (a)
Topographic stresses promote thrust faulting. (b) Topographic stresses inhibit
thrust faulting.
\label{fig:topo_fault_scenarios}](../figures/topo_stress_possibilities.pdf)

## This study
We seek to quantify the topographic stress field in the Longmen Shan region,
and on the Wenchuan earthquake faults themselves. This study is motivated by
several distinct sets of ideas, but is also largely exploratory, as topographic
stresses on faults are somewhat understudied.
 
We evaluate the extent to which topographic stresses promote or inhibit slip
similar to the coseismic displacement field in the 2008 Wenchuan event on those
faults that ruptured (which we call the Wenchuan earthquake faults).  Several
aspects of the rupture suggest topographic forcing or involvement in the
earthquake. First, the coseismic displacement of the hanging wall is roughly
radial away from the high Pengguan massif in the southwestern portion of the
rupture. Second, the very low pre-seismic strain rates across the fault evident
in the GPS velocity field (Figure \ref{fig:lms_map}) had convinced many
researchers that the Longmen Shan fault zone was tectonically quiescent [e.g.
ref]; it is possible that the earthquake occurred due to topographic forces
such as in gravitational spreading or collapse models of orogenic dynamics. In
this case, it is possible that accumulated shear stresses on the fault were
topographic in origin and the interseismic strain field associated with these
stresses has a fundamentally different geodetic signature than the typical
tectonically-induced velocity gradients across locked faults. On a smaller
scale, the heterogeneity of surface and subsurface displacement in the
earthquake may be influenced by shorter wavelength variations in topography
and topographic stresses.

Few studies have performed similar quantification of static stress fields on
faults (see Section \ref{previous-work-on-topographic-stresses} for some
examples). This is important to address because most studies of fault rupture
dynamics assume either a homogeneous or stochastic shear stress distribution
[e.g., @oglesbyday2002] and few assume any variation in normal stress [e.g.,
@aagaard2001] , despite the importance that stress variations likely have in
earthquake dynamics. By quantifying the topographic stresses on the fault,
including both the shear and normal components, we may place empirical
constraints on the potential heterogeneity of fault stresses, which may then be
compared to the coseismic slip distribution to evaluate potential interactions.

Topographic stresses are one component of the total stress field in the crust
[@molnar1988], in addition to lithostatic and tectonic stresses.
These all contribute to fault deformation. In the case of the Wenchuan event,
by analyzing the coseismic displacements, we can essentially invert for the
total stress field immediately before rupture, under certain constraints [e.g.,
@mckenzie1969; @medinaluna2013]. Because we will have fully
quantified two elements (topographic and lithostatic) of the stress field, we
may solve for the third (tectonic stress) that best matches the coseismic
displacement field. This solution is nonunique, so our methods will be
iterative (Monte Carlo based), in order to explore the ranges of tectonic
stresses that are consistent with the observed displacements. Furthermore, the
interaction between topographic stresses and the displacement field will
determine where we can firmly constrain tectonic stresses. For example, if
topographic stresses are significant and produce shear in the direction of
fault slip, then for given values of static friction and pore fluid pressure,
we can calculate the amount of tectonic stress that can be added to the ambient
stress field before the faults should rupture; given limited acceptable ranges
for friction and fluid pressure, we are essentially able to place maximum
constraints on tectonic stress. Alternately, if topographic stresses work
against coseismic slip, for given friction and fluid pressures we can estimate
the minimum magnitudes of tectonic stresses necessary to overcome shear and
frictional resistance to slip. In a scenario with complex faulting and
topography, it may be possible to put tight bounds on minimum and maximum
magnitudes and directions of tectonic stresses.


# Topographic stresses on the Longmen Shan faults

To quantify tectonic stresses on the Wenchuan earthquake faults, we first
calculate the topographic stress field in the upper crust throughout eastern
Tibet, then interpolate those stresses onto three dimensional models of the
faults taken from coseismic slip models. Then, we can calculate topographic
shear and normal stresses on the faults and compare those to the coseismic
slip patterns.

## Topographic stress tensor field calculations

## Analytical description

We calculate the stress tensor field induced by topography throughout eastern
Tibet using methods based on elastic halfspace techniques developed by Liu and
Zoback [-@liuzoback1992]. They show that the topographic stress tensor field
can be determined by a convolution of a topographic loading function with
Green's functions describing the stresses in an elastic halfspace due to
a point load at the surface (in our notation):
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
and a horizontal loading function $F_{hor}(x,y)$. See Appendix A1 for the
individual Green's functions. The horizontal loading function is decomposed
into two orthogonal components, $F_{hor, \, xz}(x,y)$ and 
$F_{hor, \, yz}(x,y)$, which are

\begin{equation}
\begin{split}
F_{hor, \, xz}(x,y) = ( \rho g h(x,y) + \sigma_{xx}^B(x,y,z) + T_{xx} )\, \frac{\partial h}{ \partial x} \\
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

$\sigma_{ij}^B$ is the stress component *ij* from the vertical (Boussinesq)
load evaluated at $z=0$, and $T_{ij}$ is the tectonic stress component *ij*,
which is considered to be zero for the topographic stress calculation. The
horizontal loading functions are convolved with the Green's functions
independently and then summed:

$$M^C(x, y, z) = G^C(x,y,z) * F_{hor, xz}(x, y) + G^C(x,y,z) * F_{hor, yz}(x, y)$$

The total topographic stress field is then calculated as 

$$M(x,y,z) = M^B(x,y,z) + M^C(x,y,z) \; .$$

## Numerical implementation

These calculations were implemented in Python (v. 2.7.3) using IPython
[@perez2007ipython], NumPy (v. 1.7) [@oliphant2007numpy] and Pandas (v. 12)
[@mckinney2010]; additional statistical analysis was performed with StatsModels
[@seabold2010]. We have created an open-source Python package called
'halfspace' to perform topographic loading calculations in a reasonably
automated way; it is available at \url{https://github.com/cossatot/halfspace}
and is being expanded to encompass a wide range of elastic stress and strain
solutions as time permits. All data and scripts for this particular project are
available at \url{https://github.com/cossatot/wenchuan_topo_stress}. 

Topography was taken from the CGIAR-CSI v.4 release [@jarvis2008srtm] of the
Shuttle Radar Topographic Mission [@farr2007srtm] Digital Elevation Model (DEM)
at 1 km nominal resolution. The DEM was projected from native WGS84 geographic
coordinates to UTM zone 48N, decreasing the nominal horizontal resolution to
851 m. Green's functions for the Boussinesq and Cerruti point-source solutions
were calculated in large square 2-D arrays at a constant depth (see Table
\ref{table:convo_params} for model parameters).  A mask was applied to each
Green's function array such that values outside the kernel radius (i.e. the
'corners' of the array) were zero.  Because of singularities in the Green's
functions at depth $z=0$, we use $\sigma^B(x,y,z)$ with $z=851 \, m)$, the
shallowest level of our calculations, in construction of the horizontal loading
functions in Equations \ref{eqn:f_hor_xz} and \ref{eqn:f_hor_yz}. Convolutions
were performed as multiplications in the time domain, and were done separately
for each depth.

Parameter	     				    | Value      | Unit
------------------------------------|------------|----------------
horizontal spacing	 			 	| 851        | m
vertical spacing   			 	    | 1000       | m
minimum depth						| 851		 | m (below sea level)
maximum depth						| 35851		 | m (below sea level)
density ($\rho$)   			 	    | 2700       | kg m$^{-3}$
g          			 	            | 9.81       | m s$^{-2}$
Green's function kernel radius  	| 9e5        | m
Lame's parameter (1)				| 1			 | -
Lame's parameter (2)				| 1			 | -

Table: Parameters for numerical calculations of topographic stresses. \label{table:convo_params}

## Topographic fault stress calculations

Topographic stresses on the Wenchuan faults are calculated on point sets
representing the faults taken from coseismic slip models. We use the coseismic
slip models of Shen et al. [-@shen2009], Feng et al. [-@feng2010],  Qi et al.
[-@qi2011], Zhang et al. [-@zhang2011], and Fielding et al. [-@fielding2013],
and discard points above 851 m below sea level, as this is above the top of our
halfspace model. The six directional stress tensor component are calculated at
each point in the fault models through linear interpolation. Because the fault
points are completely surrounded by the grid nodes at which topographic
stresses were calculated and those nodes are spaced <1 km apart, the fault
points cannot be more than a few hundred meters from the nearest grid node, so
more sophisticated interpolation techniques (e.g., based on splines) are not
necessary. We then resolve the topographic fault normal stress $\sigma_n^M$,
down-dip shear stress $\tau_d^M$ and strike-slip shear stress $\tau_s^M$ at
each point in the coseismic slip models.

# Results of topographic stress calculations on the Wenchuan faults

Topographic stresses on the Wenchuan faults are in the 1--10s of MPa range
(Figure \ref{fig:lms_topo_stresses_rot}, \ref{fig:fault_stress_3d}. Stresses are highest in the southwest,
beneath the Pengguan massif (the highest topography of the Longmen Shan front),
and decrease to the northeast. $\sigma_{zz}^M$ is the typically the largest of
the 'cardinal' compressive stresses ($\sigma^M_{i=j}$), though it is not
substantially larger than the other cardinal components. Maximum horizontal
stress is not typically aligned with either cardinal horizontal component, and
is typically larger than $\sigma^M_{zz}$ above 10 km. Maximum $\sigma^m_{zz}$
is near 80 MPa, on the southwestern Beichuan fault below the high peaks of the
Pengguan massif, except for slip models with thrust flats at the base of the
southwestern Beichuan fault, where $\sigma^M_{zz}$ reaches 100 MPa. Vertical
shear stresses ($\sigma^M_{xz, yz}$) are on the order of 1 MPa, and horizontal
shear stress ($\sigma^M_{xy}$) is on the order of 0.1 MPa.

![Topographic horizontal in the Wenchuan rupture region (black and red crosses)
at 5 km. Other symbology is the same as in Figure \ref{fig:lms_map}. Stresses
shown are downsampled from grid resolution by a factor of 6.
\label{fig:lms_topo_stresses_rot}](../figures/lms_topo_stresses_rot.pdf)

Because the compressive stresses are near equal, $M$ contains a large
isotropic, or pressure, component and a smaller shear component. Consequently,
$M$ resolves on the Wenchuan faults with a large $\sigma^M_n$ (median of about
40-60 MPa for each slip model) and much smaller shear stresses. $\tau^M_d$
median of about -3 to -6 MPa, where values less than zero indicate normal-sense
shear; and $\sigma^M_s$ median values range from about -2 to 1 MPa, where
values less than zero indicate sinistral shear. Thus, topographic shear
stresses are typically resolved as normal-sinistral, as opposed to the dominant
mode of coseismic slip, which is reverse-dextral. Both $\sigma^M_n$ and
$\tau^M$ increase the overall resistance to tectonic slip in the 2008 Wenchuan
event, and had to be overcome by tectonic compression in order for the
earthquake to occur.

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

However, much of the shallowly-dipping fault segments (the Pengguan fault and
flats at the base of the Beichuan fault, where present) have $\tau^M$ in the
direction of coseismic slip. The full stress tensor $M$ is not significantly
different in these locations, but because of the low dip angle, $\sigma^M_{zz}$
contributes more significantly to $\sigma^M_n$ than to $\tau^M_d$, which is
then dominated by horizontal compression, leading to reverse-sense shear.
Additionally, the stresses caused by the Pengguan massif locally resolve as
right-lateral on these segments as well. Coseismic slip on these fault patches
is much lower than on the steeper Beichuan fault, where the majority of slip
occurred and which is loaded in the opposite shear sense.

Compellingly, similar patterns exist in the spatial distributions of
$\sigma^M_n$ and coseismic slip. Most obvious is the coincidence of locally
high $\sigma^M_n$ and locally low slip magnitude on the southwestern Beichuan
fault below the culmination of the Pengguan massif, in an area of otherwise
high slip (Figure \ref{fig:fault_stress_3d}). These correlations exist
for other fault patches, but they are not as clear (Figure
\ref{fig:feng_slip_sig_n_scatter}). This raises the possibility that
$\sigma^M_n$ is capable of limiting slip once failure has occurred, and may
have implications for estimations of dynamic friction and the completeness of
stress drop during the earthquake. Preliminary analysis of this is currently
being performed, and will be described in a forthcoming manuscript.

![Coseismic slip magnitude and $\sigma^M_n$ on the four segments of the Feng
et al. [-@feng2010] coseismic slip model. Trendlines are L1 regressions and do
not include points with no slip.
\label{fig:feng_slip_sig_n_scatter}](../figures/feng_slip_sig_n_scatter.png)



# Calculations of tectonic stress, fault friction and pore fluid pressure

Faults fail in earthquakes when the shear stresses on the fault overcome the
frictional stresses resisting slip on the fault. At the point of failure, the
shear stress and normal stress are equal, as given in Amonton's law [e.g.,
Sibson, 1990]:
\begin{equation}
\tau = \mu ( \sigma_n - \phi )
\label{eqn:amonton}
\end{equation}
where $\mu$ is the coefficient
of static friction on the fault and $\phi$ is the fluid pressure.

Quantifying the stress, friction and pore fluid pressure involved in faulting
is a major challenge in studies of faulting and orogenic dynamics [e.g.  
@meissner1982; @oglesbyday2002].  Previous workers have demonstrated that by
quantifying topographic stress, other components in the Coulomb stress balance
may be bracketed [e.g., @cattin1997; @lamb2006; @luttrell2011].  Each of these
studies uses somewhat different approaches and scales; ours are most similar to
those of Luttrell et al. [-@luttrell2011], although there are significant
differences: primarily, we consider a full range of tectonic stresses instead
of simply calculating the minimum principal tectonic stress, and we also
constrain fluid pressure and fault friction.

We estimate the tectonic stress tensor field $T$, fault friction $\mu$ and pore
fluid pressure $\phi$ on the Wenchuan faults at the time of fault failure
through a Bayesian inversion to estimate tectonic stresses consistent with
published coseismic slip models, and then a second analysis to estimate fault
friction and pore fluid pressures consistent with the posterior stresses. Our
methods yield joint probability distributions for the parameters we estimate,
illustrating both the likelihood of values for each parameter and the tradeoffs
between them. 

In this work, we will assume that 'tectonic stresses' are horizontal stresses
in the crust that are laterally homogeneous and do not result from local or
regional topography as calculated in this study. We do not immediately ascribe
all tectonic stress to typical plate tectonic forces, either; because of the
complexities of deformation in orogens, tectonic stresses could include
contributions from processes such as lower crustal flow [e.g. @clark2005] or
stresses induced by activity on neighboring faults [e.g., ref],.

## Description of the stress state

We consider the complete stress tensor $S$ at a point in the crust to be
$S = M + T + L$, where $M$ is the topographic stress tensor as described above,
$T$ is the tectonic stress tensor, and $L$ is the lithostatic pressure tensor.
In our analysis, $M$ is a full stress tensor with independent and non-zero
values for each element; $L$ has only the principal stresses $L_{xx}$, $L_{yy}$
and $L_{zz}$, which all equal $\rho g z$ and off-diagonal (shear) stresses are
zero; and $T$ has only horizontal stresses $T_{xx}$, $T_{yy}$ and $T_{xy}$,
which are assumed to increase linearly with depth so that the entire upper
crust is near the critical failure envelope [e.g., @townend2000], and
are therefore parameterized as scalars multiplied by lithostatic pressure. 

Therefore, the full stress tensor at a point is
\begin{equation}
S = \begin{bmatrix}
  M_{xx} + T_{xx} + L_{xx} & M_{xy} + T_{xy} &  M_{xz} \\
	M_{xy} + T_{xy} &  M_{yy} + T_{yy} + L_{yy} & M_{yz} \\
	M_{xz}     &  M_{yz}  &  M_{zz} + L_{zz}
	\end{bmatrix} \; .
\label{eqn:stress_tensor}
\end{equation}

$\phi$ is considered to be a scalar between zero and one that expresses pore
fluid pressure as a fraction of total pressure (the mean of the main diagonal
of $S$) at each point on the fault. $\mu$ is the coefficient of static friction
and is considered constant along the fault.


## Bayesian inversion of tectonic stresses

We invert topographic stresses and coseismic slip models for tectonics stresses
using Bayesian methods, and making the common 'Wallace-Bott' assumption (named
after Wallace [1951] and Bott [1959]) that slip on the fault occurs in the
general direction of the maximum resolved shear stress on the fault [e.g.,
McKenzie, 1969; Angelier, 1994]. We estimate the tectonic stresses in light of
the topographic stresses and slip distributions through the relation
\begin{equation}
p(T|D) \propto p(T) \, p(D|T)
\label{eqn:bayes_rule}
\end{equation}
where $p(T)$ is the prior probability distribution (or *priors*) of $T$, 
$p(D|T)$ is the likelihood of observing the coseismic slip distribution $D$
given the tectonic stresses $T$, and $p(T|D)$ is the posterior probability
distribution of $T$ given $D$, which is the solution to the inversion.

We choose priors for the magnitudes and orientation of the maximum and minimum
principal tectonic stresses. The maximum principal stress is sampled from a
uniform distribution between $\rho g z$ and 2.5 $\rho g z$. The minumum
principal stress is sampled from a uniform distribution between 0 and the value
for maximum stress. Because the Wenchuan event was an oblique reverse faulting
earthquake, both the maximum and minimum (horizontal) stress directions have to
be positive as they are greater than the vertical stress. The stress
orientations are taken as the azimuth of maximum tectonic stress and are
sampled uniformly from 0 to 360$^{\circ}$.

For each of 100,000 iterations, unique samples for each of the priors are drawn
using a seeded pseudorandom number generator (so that the same priors are drawn
for each coseismic slip model). Then, the complete stress tensor $S$ is
constructed for each fault point in a coseismic slip model. The rake of the
maximum shear stress $\lambda^S$ on each point on the fault is then calculated,
and compared with the coseismic slip rake $\lambda^D$ at that point. Then, a
weighted mean misfit is determined:

\begin{equation}
\bar{\lambda}^m = \sum \nolimits_{i=1}^n \frac{(\lambda^S_i - \lambda^D_i) D_i} {\bar{ D}}
\label{eqn:rake_misfit}
\end{equation}

Finally, the relative likelihood of each model is taken as 
\begin{equation}
p (D | T) = \frac{ \exp ( \kappa \cos \bar{\lambda}^m )} {\exp (\kappa \cos \bar{\lambda}^m_{\min})}
\label{eqn:rel_likelihood}
\end{equation}

where $\kappa$ = 8.529, which is calculated so that 68.2% of the Von Mises
distribution is within $\pi$/9 radians (20$^{\circ}$), the estimated 1$\sigma$
uncertainty of the coseismic slip models based on comparisons between rakes of
high-slip fault patches (note that for a planar fault, $\tau$ at $\pi/9$
radians from $\lambda_{max}$ is still >90% of $\tau_{max}$ [-@lisle2013]).
Then, the posterior distribution $p(T | D)$ is estimated *(sampled?)* by
comparing each model likelihood to a random number selected from the uniform
distribution [0, 1), and retaining those models with a higher likelihood than
the random value.

## Analysis of friction and pore fluid pressure

Once the tectonic stress distributions consistent with the coseismic slip data
have been determined, we analyze the distributions of $\mu$ and $\phi$ required
for critical failure conditions on the faults. First, we take each model
retained in $p(T|D)$, and for each model draw a random $\phi$ from the uniform
distribution $p(\phi)= [0,1)$ (again using a seeded pseudorandom number
generator for consistent priors across all coseismic slip models). Next, we
calculate $\tau^S$ and $\sigma_n^S-\phi$ for each point on the fault. Then, we
solve Equation \ref{eqn:amonton} for $\mu$. Finally, we filter the
results so that only models with $0 \ge \tau \ge 1$ are retained.

After this analysis has been done for all slip models, we find the set of
posteriors that are common to all models, which we call the "joint" [?]
posteriors, or $p(P^{joint} | D)$ where $P$ is the parameter of interest.


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
\label{fig:joint_posteriors}](../figures/joint_pdfs.pdf)


# Discussion

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
the earthquake.

![Topographic and tectonic horizontal stresses (taken from the most likely
estimates of $p(T|D)$ in the Wenchuan rupture region (black and red crosses)
with horizontal maximum stress orientation data taken from before the 2008
Wenchuan event from the World Stress Map [@heidbach2009] (purple arrows), and
horizontal maximum stress orientation data from after the earthquake at the
WFSD-1 drill hole [@cui2014] (blue arrows). Other symbology is the same as in
Figure \ref{fig:lms_map}. Stresses shown are downsampled from grid resolution
by a factor of 9.
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

Figure \ref{fig:cfr_ratios} shows $log (CFR_o / CFR_f)$ plotted against $\mu$,
$\phi$ and $\sigma_T_xx$ on the Beichuan fault for all samples. Though
considerable scatter exists even in $log (CFR_f / CFR_o)$, it is clear that in
most instances, slip on the Beichuan fault is preferred over slip on an optimal
fault, except for high values of $\mu$. Because $T$, $\phi$ and $\mu$ can all
affect fault reactivation [e.g., @sibson1985], we compare the relative
contributions of each with a simple mutliple linear regression, using
$\sigma^T_{xx}$ normalized to [0,1) (the same range $\phi$ and $\mu$) as
a proxy for $T$ ($\sigma^T_{xx}$ is essentially $\sigma^T_{max}$ in most of the
posteriors). The results are shown in Table \ref{table:cfr_regress}. It is
clear that $\mu$ is most strongly correlated with $CFR_o/CFR_f$, followed
closely by $\sigma^T_{EW}$ and then $\phi$; nonetheless, all significantly
affect the relative ease of faulting on the Beichuan fault versus optimal
faults.

![Comparison of Coulomb failure ratio (CFR) on the Beichuan fault from the
Zhang et al. [-@zhang2011] model to CFR on an optimally-oriented fault with
$\mu = 0.6$, versus estimated $\mu$ on the Beichuan fault. Values less than
0 (1 in linear space) indicate that slip is favored on the Beichuan fault, even
if it is non- optimally oriented. Values are calculated for each point in the
slip model for 1000 randomly-drawn samples from $p(T,\mu,\phi |D)$.
\label{fig:cfr_ratios}](../figures/cfr_plots.pdf)


Parameter           | Coef.   | Std. Err. | t        | $P>|t|$      
--------------------|---------|-----------|----------|----------
Intercept           | -0.2566 | 0.0020    | -128.8   | <0.0001 
$\mu$               | 1.1168  | 0.0086    | 130.6    | <0.0001
$\sigma^T_{EW}$     | 0.9138  | 0.0048    | 191.2    | <0.0001
$\phi$              | 0.5762  | 0.0055    | 105.7    | <0.0001 

Table: Sensitivity of CFR ratios to relevant stress state parameters: Results
of multivariate linear regression of $CFR_o/ CFR_f)$ against $\mu$, $\phi$ and
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
