
## R1a
> The complete stress tensor is divided into contributions from topography,
> tectonic, and lithostatic stress (eq 9). The tectonic stress is then assumed
> to increase linearly with depth "so that the entire crust is near the critical
> failure envelope" (line 247), referencing Towend and Zoback 2000. This is
> essentially just a statement of Byerlee's law, in which brittle failure occurs
> in the upper crust at a stress level approximately equal to the lithostatic
> pressure applied to the rock scaled by ~0.6 (this study's parameter T'?).

This is related to, but not really a restatement of, Byerlee's law. This is
much more a statement of the Coulomb failure envelope. Byerlee's law is related
to the failure of intact rock, which is often quoted (as in the review, and
in our section 6.3) as 0.6. This coefficient is related to the coefficient of
internal friction of intact rock, which is not our $T'$. In our study, we are
primarily concerned with the failure of a specific, pre-existing fault, whose
strength (coefficient of static friction) is unknown but likely less than
unfractured rock. We scale tectonic stresses linearly with depth, and each
component of tectonic stress ($T_{xx}$, $T_{xy}$, and $T_{yy}$, or $T_{max}$,
$T_{min}$, and azimuth) increases with depth at a different rate.

$T'$ is simply $T / \rho g z$ (line 275 of original manuscript).

## R1b
> However, this means that the formulation expressed in equation 9 is counting
> the lithostatic contribution of stress twice. 

We have not double-counted lithostatic stress, we have simply been unclear in
our description of the stress state. Lithostatic stress is an isotropic tensor,
so (as described) it has non-zero terms only the diagonals of the tensor. 
Tectonic stress is
only horizontal, $T'$ is scaled by $\rho g z$ (not by the tensor $L$, as we had
previously, and erroneously stated). So non-zero values of $T$ and $L$ are not 
the same
components of the stress tensor. 

We amend the submitted description:

> We consider the complete stress tensor, $S$, at a point in the crust to
> be
> 
> \begin{equation}
> S = M + T + L \; ,
> \end{equation}
> 
> where $M$ is described above, $T$ is the tectonic stress tensor, and $L$
> is the lithostatic stress tensor. $L$ is isotropic, with diagonal
> components equal to $\rho g z$. We assume that $T$ is laterally
> homogeneous and only has horizontal stress components (i.e.,
> $T_{xz} = T_{yz} = T_{zz} = 0$, with $T_{xx}$, $T_{yy}$ and $T_{xy}$
> non-zero). We further assume that $T$ increases linearly with depth so
> that the entire upper crust is near the critical failure envelope
> [e.g., *Townend and Zoback, 2000*], and thus we parameterize the components of $T$
> as scalars multiplied by lithostatic pressure, denoted as $T^\prime$

to

> We consider the complete stress tensor, $S$, at a point in the crust to
> be

> \begin{equation}
> S = M + T + L \; ,
> \end{equation}

> where $M$ is described above, $T$ is the tectonic stress tensor, and $L$
> is the lithostatic stress tensor. $L$ is isotropic, with diagonal
> components equal to $\rho g z$. We assume that $T$ is laterally
> homogeneous and only has horizontal stress components (i.e.,
> $T_{xz} = T_{yz} = T_{zz} = 0$, with $T_{xx}$, $T_{yy}$ and $T_{xy}$
> non-zero). The expanded stress tensor is:

> \begin{equation}
> S = \begin{bmatrix}
>   M_{xx} + T_{xx} + L_{xx} & M_{xy} + T_{xy} &  M_{xz} \\
> 	M_{xy} + T_{xy} &  M_{yy} + T_{yy} + L_{yy} & M_{yz} \\
> 	M_{xz}     &  M_{yz}  &  M_{zz} + L_{zz}
> 	\end{bmatrix} \; .
> \label{eqn:stress_tensor}
> \end{equation}

> We further assume that $T$ increases linearly with depth so
> that the entire upper crust is near the critical failure envelope at an unspecified coefficient of friction
> [e.g., *Townend and Zoback, 2000*], and thus we parameterize the components 
> of $T$ as scalars multiplied by $\rho g z$, denoted as $T^\prime$. Therefore, 
> if $T'_{xx} = 0.1$, at some point just below 1 km, $L=27$ MPa, so
> $S_{xx} = M_{xx}$ + 27 MPa + 2.7 MPa.


which hopefully clarifies this.


## R1c
> The Towend paper derives its results from deep drilling studies, so it
> would be more appropriate to assume that the total stress S increases 
> linearly with depth in this manner. 

To increase $S$ linearly with depth,
we would need to vary $T$ spatially to exactly counterbalance variations in $M$
that deviate from linearity. Instead, we find it much simpler to approximate
$T$ as increasing linearly with depth, because then we can quantify it with
three numbers ($T'_{xx}$, $T'_{xy}$, and $T'_{yy}$, or equivalently $T'_{max}$,
$T'_{min}$ and the azimuth of $T'_{max}$). Additionally, because $L$ increases
rapidly with depth, it overwhelms the largest topographic stresses on the
fault (~80 MPa) at about 3 km, so for most of the crust, $S$ does
increase essentially linearly with depth.


## R2
> The authors make the "Wallace-Bott" assumption (line 277) that fault slip
> direction aligns with maximum horizontal principal stress direction, and the
> subsequent analysis of tectonic stress is made with the criteria that
> acceptable solutions minimize the difference between these two (equation 11
> and lines 300-301). However, several of the results described in discussion
> section 6.2 interpret the alignment of the modeled tectonic stress
> orientation and coseismic slip direction as a meaningful result: e.g., line
> 401, line 407, line 417. For example, that the shear stress has non-trivial
> contributions of both strike and dip-slip was required since the stress must
> align with the oblique-slip earthquake. 

In these comments, the reviewer basically asserts that we set up our model to
replicate observations and then claim that is significant that our model's
predictions match the observations, and then gives several example lines (401,
407, 417). Though this is not the interpretation of the paragraph that we had
intended, it is apparent how this interpretation could be made. Nonetheless,
the specific lines seem to be off the mark in this:

Line 401 is basically a quick description of the results (E-W maximum principal
tectonic stress produces oblique shear on the fault), and is not a claim about
the significance of the results.

Line 407 is a comparison of our estimated maximum principal stress and stress
measurements from the WFSD drill hole at that location; the drill hole stress
measurements were not used in our inversion, and therefore this is an
independent confirmation of our results, not a direct consequence of the
inversion.

Line 417 states that dip-slip and strike-slip shear are nearly equal in the
most-likely model results, and then compares that result to an orogen-scale
elastic block modeling study, not to the coseismic slip models used in the
inversion.

However, in one instance in this paragraph (lines 403-404) we are guilty as
charged, and make amendments. We change the lines:

> This stress configuration is compatible with the observed kinematics of the
> Wenchuan faults, and in close agreement pre-earthquake stress measurements
> near the rupture zone...

to 

> This stress configuration is in close agreement with pre-earthquake stress
> measurements near the rupture zone...


## R3
> Line 188: In the Liu and Zoback formulation, tectonic stress is an integrated
> part of the horizontal loading functions (equations 5 and 6). Is it 
> appropriate to neglect tectonic stress in these equations but then add it 
> back in linearly during the analysis of section 4? I expect this has some
> ramifications. 

This was something we puzzled over for a while.
However, the horizontal loading functions specify
horizontal surface loads that are then propagated into the subsurface using
Cerruti's solutions [Appendix A2]. The Liu and Zoback formulations of the
loading functions require a fixed tectonic stress at
depths above zero (i.e., in the topography that is imposed on the surface of 
the elastic half-space). Because we assume that tectonic stress increases 
linearly
with depth, with zero contribution of tectonic stress at the surface of the 
half-space, tectonic stress does not need to be included in the horizontal 
loading function of the second order terms of the topographic stresses.

An additional complication is that the calculation of topographic stresses in
the region (not their interpolation onto the fault) takes about 9 hours, and
so devising some iterative scheme where we could calculate topographic
stresses, then find tectonic stress and then add that back into the topographic
stress calculations and repeat until some criteria is reached, is really out
of the question with the Bayesian inversion scheme we've chosen (there are
about 18,000 models in the joint posterior). While the assumption that the 
tectonic component of stress vanishes in the upper few kilometers of the the 
Earth (i.e., above the reference depth which is taken to be the top of the 
elastic half-space), we feel we adaquately described this choice in our 
construction of the model and with this choice are horizontal loading 
functions in the calculation of topographic stresses is entirely 
self-consistent.

## R4
> Line 193 assumes a "Poisson halfspace", presumably meaning an elastic
> halfspace made up of a Poisson solid with Poisson ratio of 0.25. While this
> is an oft-made assumption, in this situation it has more impact. Figure 2
> nicely illustrates how the topography loading on the fault planes can change
> sign depending on how effective the vertical load is at generating horizontal
> stresses, which is precisely what the Poisson ratio governs. It would be
> helpful, therefore, to know how robust these results are to choice of
> Poisson ratio. 

We had chosen our the value of 0.25 for the Poisson ratio not only because of
 convenience (the shear modulus and Lame's parameters drop out
of the equations) but because this is the most likely value for the rather
felsic Tibetan crust based on seismic studies.  But in light of these comments,
we have recalculated the fault stresses using a Poisson ratio of 0.28, as a
test. We have found that the stresses are different by 1 or 2 MPa, which is
a very small difference relative to the overall magnitudes. We have changed the
relevant sentence in first paragraph of Section 2.2 from:

> We assume a Poisson halfspace

to

> We assume a Poisson ratio of 0.25, following receiver function studies
suggesting values of ca. 0.24-0.26 throughout central and western China [*Chen
et al., 2010*] (we have tested a Poisson ratio of 0.28, which is on the higher
end of values for intermediate rock compositions [*Zandt and Ammons, 1995*],
and found the results to vary by a few percent). 
 

## R5
> Line 292: do both the tectonic stresses have to be positive? Vertical 
> principal stress could still be the least compressive if Tmin were negative 
> and Tmax were positive, right? This would increase the available permitted 
> parameter space.

In general, neither of the tectonic stresses have to be positive. However,
vertical stress cannot be least compressive if $T_{min}$ were negative
(tensile), unless topographic stress produced a strong horizontal compression
in the direction of $T_{min}$ and less strong vertical compression. Our results
show that the topographic stresses are mostly stronger (more compressive) in
the vertical direction than in the horizontal directions.

Additionally, from a tectonic standpoint, there is no real reason to consider
N-S tectonic tension (the direction of $T_{min}$ in our results) at the western 
margin of the Sichuan Basin;
this is a region surrounded by thrust and strike-slip faults of various
orientations (e.g. Figure 1). If there was tectonic tension in the region, then
the patterns of deformation would be different in the interior of the Sichuan
Basin away from topography; currently here is thrust faulting in that region,
which
indicates a vertical $\sigma^3$. There is no evidence of N-S extension anywhere
in the Himalayan-Tibetan orogen except for in the Miocene in the Himalaya,
which is synchronous with parallel thrusting (the famed Himalayan extrusion). 

The purpose of Bayesian priors is to not only keep potentially likely models 
in, but also as importantly to keep
unlikely models out. Because we adopt a relatively simple scheme of uniform
probabilities over some interval, adding unlikely models to the prior at the same
rate as more likely models, will decrease the acceptance rate of models tested
that are retained in the posterior,
and therefore we would need to test many more models to obtain the same level 
of sampling of the posterior as we do
(we note that we are already at the limit of what can be done with 128 GB RAM).


## R6
> The emphasis on the Bayesian estimation providing a doubly bounded constraint 
> on tectonic stress (379) or on the on the ability of the study to identify 
> more than a minimum bound of the tectonic stress (line 373) is overstated. 
> The fundamental gist of this study is that topography provides a resistive
> force that must be overcome by tectonic stress (lines 140-142). This provides
> a physical minimum bound for tectonic stress, but there is no information
> considered that physically provides any upper bound. Unsurprisingly,
> therefore, the results in figure 6 show a pdf with a lower bound only, as
> noted on line 413. This is not a failure or triumph of the chosen statistical
> scheme, it's a physical limitation of the available data. 

While the results are certainly more sensitive to the low end of allowable
$T'_{max}$ values, they are somewhat sensitive to the high end. This
sensitivity varies with slip model, as is apparent in Figure 6. Figure 8,
the joint results, show that $T'_{max}$ decreases past about 1.0, and the
likelihood of $T'_{max}=2.5$ is about 60% of the likelihood of $T'_{max}=0.8$.
Additionally, this is assuming that $T'_{max}$ is *a priori* equal at 0.8 and
2.5 (which is our simple model); personally, I find it rather unlikely that
tectonic stresses would be so high, although we chose the model prior to be
a bit different than our personal, unquantified prior beliefs. So in short,
while we do not find a hard upper-bound, the posterior does not indicate that
the likelihood of models at the upper bound is equal to the likelihood of 
models at lower $T'_{max}$.

The lines 373 and 379, chosen by the reviewer, are in a discussion of
methodological differences between this study and another that only attempts to
constrain the minimum tectonic stress in a similar environment; the differences
here are in approach more than results. 


## R7
> I'm concerned that the Bayesian PDF estimation as used for T'min, e.g. in 
> figure 6, results in a biased estimate. Because there's a requirement that 
> Tmin < Tmax, half of parameter space is off limits a priori (lines 293-296).
> It therefore seems unsurprising that the T'min PDF is heavily weighted toward
> zero. Is there a way to re-scale the problem so that the parameters being
> estimated are independent? 

The requirement that $T_{min} < T_{max}$ is not simply an attribute of our
priors or Bayesian estimation scheme, but minimum is
defined to be less than maximum, so the half of the parameter space where this
would occur is off limits by definition.

Constructing suitable priors, though, was something that we spent some time on.
The issue with picking stresses independently is that they're not independent,
because $T_{min} < T_{max}$, regardless of the value of $T_{max}$, so there is
an inherent conditional probability. So they can't be sampled indendently, and
there are two approaches that can be taken. One of them is to take a random
(uniform) Nx2 array and sort each row, so that one column is $T_{max}$ and the
other is $T_{min}$. This approach yields a uniform joint prior probability
density over the available half of the $T_{min}$ x $T_{max}$ parameter space,
but yields marginal priors for $T_{max}$ that are strongly biased towards high
values, and priors for $T_{min}$ that are biased towards the low end. 

The other is to do what we did, and take a random (uniform) Nx1 array for
T$_{max}$, and then take $T_{min}$ as some random value from [0,1) of
$T_{max}$. This gives a uniform prior PDF for $T_{max}$, a similar prior for
$T_{min}$ as the first option, and a higher joint probability density towards
the low $T_{max}$ end of the $T_{max}$ vs $T_{min}$ space.

The marginal priors for
$T_{max}$ would be much more strongly biased in the first sampling approach,
while the marginals for
$T_{min}$ is less affected by the sampling strategy. Overall, we feel that our
approach is less biased, because it results in a uniform $T_{max}$, which is
the more important value.

On further reflection, it would be possible to pick a uniform $T_{min}$ and
then build $T_{max}$ around that, but then $T_{max}$ would be non-uniform. We
can think of no particular reason to favor this approach, since researchers are
generally more interested in estimating maximum principal tectonic stress than
minimum.

However, it is clear in Figure 8b, where $T'_{min}$ is scaled to $T'_{max}$,
that the *ratio* of $T_{min}$ to $T_{max}$ is constrained by the inversion;
the most likely value for $T_{min} \approx 0.3 T_{max}$, regardless of the
value for $T_{max}$. This point was mentioned in passing in section 5.1 (line
330) but could be discussed in more detail, particularly with reference to 
Figure 8.1. Therefore, we add to Section 5.2:

>It is also apparent in Figure 8b that regardless of the magnitude of
$T^\_{\mathrm{max}}$, $p_{J}(T^\prime_{\mathrm{min}} | D)$ is
consistently 0--0.6 $p_{J}(T^\prime_{\mathrm{max}} | D)$, with a mode
of about 0.3; this indicates that the relative magnitude of the
tectonic stresses has a substantial influence on the rake of the maximum
shear stress resolved on the fault.


## R8
> The caption for Figure 4 is truncated on p 43, and is not present anywhere
> else in the text. The figure itself is not self-explanatory, and the details
> aren't sufficiently explained in the results section 3. This seems to be an
> unfortunate LaTEX mishap, but since this model is the primary finding of this
> study and the basis for the subsequent analysis, the reader unfortunately
> cannot just "read past" the omitted details. Some of the obvious gaps are
> noted below. 

This is indeed true, and it is unfortunate. However, the unclipped figure
caption was available to the reviewer in the 'article file' available to
him/her (not the merged pdf) on the review website. More fortunately, the
general reader will be reading a professionally typeset version of the paper,
not a submitted LaTeX draft.


## R9
> It is not entirely clear which faults are shown in 4a, and not at all clear
> what faults or regions of space are represented in 4b-c (by the way, a b and
> c are not labeled either). What depths are represented in these models? The
> visible portion of the caption notes "same lateral extent, but different
> perspectives", but it is not clear what this means. And why is the maximum
> slip magnitude in "A" 7m, but the maximum component slips in "B" and "C" are
> 14m and 10m? 

The caption states that 

The magnitude of slip in the models varies by a factor of about 2. The rakes
and the spatial distribution of slip vary much less.


## R10
> Also, as section 3 represents the principal findings of this study, the 
> reader would benefit from some additional discussion here of the relevant
> features of the models. For example, the text on lines 237-239 and lines
> 244-247 seem to represent and important result worthy of more attention and
> discussion. 

We have added a paragraph and a half describing the characteristics of the slip
models used, including the similarities and differences of their geometry and
slip distributions, to Section 2.3:

>We use six models,
those of *Shen, et al.* [*2009*], *Feng, et al.* [*2010*], *Zhang, et al.*
[*2011*], *Fielding, et al.,* [*2013*] and two from *Qi, et al.* [*2011*]. 
DELETED LINE
All of these models rely on geodetic data to some degree, but they do not all use the same data in their inversion (e.g., *Feng, et al.* [*2010*] uses a different InSAR catalogue as the others), all use differnet inversion stratagies, and different fault geometries (the two models of *Qi et al.* [*2011*] share a common fault geometry but use different regularization in the inferrence of the slip distribution).
DELETED LINE
By using a suite of models in our calculations,
we can infer that results that are persistent in most or all of the
models are more robust, while other results specific to only one of the coseismic slip models can be more confidently linked to
specifics of the model geometry or inferred slip distribution in those models. 

>In general, the fault geometries in all of the coseismic slip models are simmilar, as well as the inferred pattern of slip distribution
above 10 km or so (i.e., the locations of high and low slip patches and the slip
rake are similar in all of the models).  Although some of models use discrete, planar fault
segments, whereas others use a single continuous, non-planar fault,
the fault geometry models are essentially collocated. However, there is significant
variability in the magnitude of slip in the different models; for example, the
maximum slip magnitude in the Qi 'rough' model is about twice that of the
Feng model. Large differences also exist in the deeper geometries of the
models: the Qi, Fielding and Shen models all have horizontal or subhorizontal
thrust flats at or below 15 km, though only minor slip is assumed to have
occurred on these fault segments. In contrast, the Feng and Zhang models are
planar to their lower end at 25-30 km.

The significance of the findings highlighted here by the reviewer are discussed
in the discussion (Section 6.4, particularly lines 504-511). In general, our
chosen expository style in this paper is more geared towards description of the
results rather than (over-)interpretation. The results themselves are described,
and the results files are made available for readers who are interested in
probing them for themselves. Because our results cover both topographic and
tectonic stresses, as well as fault strength parameters, there are a lot of
implications for anything from earthquake processes to orogenic development,
and we feel it is better to be reasonably brief in our discussion of 
individual aspects of these implications.


## R11
> The introduction of the study says the work intends to "investigate the
> effects of topographic stress on the faults" (line 48) and then "bracket the
> tectonic stress field, pore fluid pressure, and static friction of the fault"
> (line54). However, in beginning to describe the topographic stress resolved on
> faults, section 3 refers to an upcoming manuscript for analysis of how these
> stresses might affect faulting. This is indeed an interesting aspect of the
> study, but either that information should be included here or the focus on
> influencing rupture process should be removed from the abstract and
> introduction. 

There is nothing in the abstract that references a topographic influence on the
rupture processes. In one sentence in the introduction (lines 41-45), we write
that topographic stresses *may* influence rupture propagation. We do not
'focus' on this. Additionally, as promised in the two quoted passages (from
lines 48 and 54), we do investigate the effects of topographic stress on the
faults, and bracket the tectonic stresses, friction, and fluid pressure on the
faults. This is the focus of the paper.

The first-order 'effects of topographic stress on the faults' is whether those
stresses promote or inhibit slip on the faults. We show that topographic
stresses are overwhelmingly resistive/inhibiting to fault slip, both by adding
shear stress to the faults in the opposite direction to slip, and by adding
significant normal stress to the faults. 

The influence of topographic stresses on a rupture that does occur may be a
second-order effect. We see that topographic stresses, particularly normal
stress, is negatively correlated with slip magnitude, and we discuss this in
lines 248-255. However, any real discussion on this other than the observation
that it occurs is beyond what we can comfortably say at this time, without
being more speculative than we would wish. However, we believe it is an
important observation, and it is certainly one which we have already made, and
so it would be inappropriate to sweep it under the rug because we do not yet
understand it at publishable level. It may be that other researchers are
interested, or have better means to investigate it (i.e. they are experts in
dynamic rupture modeling), and we should not inhibit them.

## R12
> Overall, the manuscript, though well organized, seems to have an unbalanced
> emphasis. The specific details of the analytical methods are present, but
> overall the results should be more fully described and the discussion more
> fully developed. 

We feel that it is crucially important to fully describe the methods of our calculations and estimation stratagy,
We
chose this earthquake because it's well-documented and has a
complex coseismic slip distribution, and because it lies at the base of a very
large plateau that has been suggested to be expanding outward due to
topographic stresses. We looked into these effects, framed the investigation in
terms of questions (e.g., do topographic stresses promote or inhibit the
observed slip on the faults), and answered them.

Nevertheless, the results and the discussion make up the bulk of the paper. The
methods sections (2 and 4) are 6.5 'manuscript' pages in sum, which includes
many equations that take up a lot of space. The results sections (3 and 5) are
about 2 pages, and 6 of the 10 figures. The discussion is 8 pages, by far the
longest section.

## R13
> Line 24: Though I can see the appeal of the selected quotation, it would be
more appropriate for an oral presentation or a monograph on the subject. In
this context, it comes across as awkward and out of place.

We have removed it. 

## R14
> Section 1.1: additional relevant references to consider: Fialko, Rivera, and
Kanamori (2005 GJI), Ghosh et al (2006 Geology), Flesch et al (2007 GJI) 

We have added a reference to the Fialko paper. The Flesch and Ghosh papers
mentioned here are 'thin viscous sheet' type papers, similar to those already
mentioned in the review (including a later paper by Flesch); those types of
studies are of a much larger (orogen to global) scale than our study.

## R15
> Lines 224-230 describe the magnitudes of stress tensor components, but this
would be better explained with a figure. If not as its own figure, could Mzz at
least be incorporated into figure 3?

We have added vertical topographic stress to Figures 3 and 9. 


## R16
> Section 6.0 contrasts the methods of this study to those of Luttrell et al.
2011 study of the Maule earthquake. This is an understandable comparison, but
because the Wenchuan earthquake includes both strike-slip and dip-slip
components, it is actually more similar to the Luttrell and Sandwell (2012 JGR)
study of Mid Ocean Ridges that includes both strike-slip and normal earthquakes
as constraints. 

Actually, we feel that our manuscript is more similar to the Luttrell et al.
2011 paper because that paper uses a coseismic slip model in the stress
inversion, and because it involves a single event. The Luttrell and Sandwell
paper uses focal mechanisms, which are considered to represent constant coseismic slip over a planar fault plane corresponding to one of the nodal planes of the focal mechanism, and considers
multiple earthquakes. This is a bit more different with respect to our paper.

## R17
> The introduction lists 7 coseismic slip models of the Wenchuan earthquake (line 124), and then the analysis refers to 5 of them (line 213). As the authors noticed, all these models essentially draw from the same set of geodetic data, and all have essentially the same result, and thus all give this study essentially the same result (line 343). Is there a reason these particular models were chosen for analysis? Why not just choose one, or if they truly are different enough to influence these results, why not use them all? Some justification of this choice is warranted. 

We used all of the models that we could find that were available (i.e. the slip
model files themselves were published), had proper georeferencing, and seemed
to be of sufficiently high quality. There are many models that did not attempt
a good geometric fit to the available data--e.g. they consist of a single,
planar fault segment--or models with very poor coseismic slip resolution. We
did not feel it wise to include these.

We have added some discussion of the models used, and the criteria for
including them, to Section 2.3, as described in R10. We also reiterate here
that not all of these coseismic slip models relied on the same data,
approximated the fault geometry the same, or used the same inversion strategy
to infer the coseismic slip. As any of these coseismis slip models are just 
*models*, we do feel that basing our conclusions on just one particular model
makes for the most robust study. 


## R18
> --Typos 

> Lines 177 and 182: is z positive up or down? Clarify this 

> Line 258: earthquake, not fault, initiated 

> Line 274: "are" -> "and"? complete sentence with period 

> Line 509: typo, delete "to close" 

> Line 556: If you acknowledge some of your data sources, you should acknowledge all of your data sources (e.g., scientific drilling, WSM, etc) 

> Fig 3 and 9 need 33ºN label correction

All listed typos corrected. 
