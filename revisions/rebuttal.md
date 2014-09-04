
## R1
> The complete stress tensor is divided into contributions from topography,
> tectonic, and lithostatic stress (eq 9). The tectonic stress is then assumed
> to increase linearly with depth "so that the entire crust is near the critical
> failure envelope" (line 247), referencing Towend and Zoback 2000. This is
> essentially just a statement of Byerlee's law, in which brittle failure occurs
> in the upper crust at a stress level approximately equal to the lithostatic
> pressure applied to the rock scaled by ~0.6 (this study's parameter T'?).
> However, this means that the formulation expressed in equation 9 is counting
> the lithostatic contribution of stress twice. The Towend paper derives its
> results from deep drilling studies, so it would be more appropriate to assume
> that the total stress S increases linearly with depth in this manner. 

(add whole tensor thing)


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

In these comments, the reviewer basically asserts that we claim that is
significant that our model's predictions match the observations, and then gives
several example lines (401, 407, 417). Though this is not the interpretation of
the paragraph that we had intended, it is apparent how this interpretation
could be made. Nonetheless, the specific lines seem to be off the mark in this:

Line 401 is basically a quick description of the results (E-W maximum principal
tectonic stress produces oblique shear on the fault), and is not really a claim
about the significance of the results.

Line 407 is a comparison of our estimated maximum principal stress and stress
measurements from the WFSD drill hole at that location; the drill hole stress
measurements were not used in our inversion, and therefore this is an 
independent confirmation of our results, not a tautological statement.

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

This was something we puzzled over for a while. Ultimately, we chose our
approach because it is less than obvious how to incorporate a depth-dependent
tectonic stress into the calculations. The horizontal loading functions
specify horizontal surface loads that are then propagated into the subsurface using Cerruti's solutions [eq. xx]. The Liu and Zoback formulations of the loading
functions seems to require a fixed tectonic stress, or the tectonic stress at
zero depth. Because we assume that tectonic stress increases linearly from zero
with depth, the tectonic stress at zero depth (sea level) is zero.

## R4
> Line 193 assumes a "Poisson halfspace", presumably meaning an elastic
> halfspace made up of a Poisson solid with Poisson ratio of 0.25. While this
> is an oft-made assumption, in this situation it has more impact. Figure 2
> nicely illustrates how the topography loading on the fault planes can change
> sign depending on how effective the vertical load is at generating horizontal
> stresses, which is precisely what the Poisson ratio governs. It would be
> helpful, therefore, to know how robust these results are to choice of
> Poisson ratio. 

This is a valid point, but it wasn't something that we had tested much because
of the computational effort required, both in terms of programmer time and CPU
time. However, in the intervening months since submitting this manuscript, we
have streamlined the analysis so that the programmer time required is much
less.

[test this].

## R5
> Line 292: do both the tectonic stresses have to be positive? Vertical 
> principal stress could still be the least compressive if Tmin were negative 
> and Tmax were positive, right? This would increase the available permitted 
> parameter space.

In general, neither of the tectonic stresses have to be positive. However,
vertical stress cannot be least compressive if $T_{min}$ were negative, unless
topographic stress produced a strong horizontal compression in the direction of
$T_{min}$ and less strong vertical compression.

To restate this mathematically, for clarity:
Let's consider $T_{min}$ to be aligned N-S, i.e. it is in the $xx$ direction.
The equation for total stress is $S = M + T + L$ (equation 9), and we consider
tectonic stress $T$ to be only horizontal stresses. So the vertical stress is
$M + L$. $L$ is isotropic, so we can ignore it here. The only way that 
$M_{xx} + T_{min} > $M_{zz}$, where $T_{min} < 0$, is to have 
$M_{xx} > M_{zz} - T_{min}$. Given that typically $M_{zz} > M_{xx}$ in our 
results (Section 3, lines 224-225 of the original manuscript), it is not
possible in this case to have a negative $T_{min}$ and still have vertical
stress ($S_{zz}$) as the least compressive stress (which is required by reverse
fault slip).

Furthermore, 


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

The reviewer is absolutely correct in his or her assessment of the ability of
the Bayesian inversion to capture the maximum tectonic stresses for this
particular earthquake, and we are up front about this (lines 323-326). (For
other events with less of a the thrust component, we can constrain maximum
tectonic stress).

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

This was something else that we spent some time on. The issue with picking
stresses independently is that they're not independent, because $T_{min}$ *has
to* < $T_{max}$. So they can't be sampled indendently, and there are two
approaches that can be taken. One of them is to take a random Nx2 array and
sort each row, so that one column is $T_{max}$ and the other is $T_{min}$.
This approach yields a uniform joint prior probability density over the
available half of the $T_{min}$ x $T_{max}$ parameter space, but gives strongly
nonuniform marginal priors for either $T_{max}$ (which linearly increases from
0 at T=0 to max) or $T_{min}$ (with a commensurate linear decrease).

The other is to do what we did, and take a random Nx1 array for T$_{max}$, and
then take $T_{min}$ as some random value from [0,1) of $T_{max}$. This gives
a uniform prior PDF for $T_{max}$, the same prior for $T_{min}$ as the first
option, and a higher joint probability density towards the low $T_{max}$ end.

So, although the joint probability density is higher towards the low $T_{max}$
end (visible in Figures 6 and 8a) in our approach, the marginal priors for
$T_{max}$ would be much more strongly biased in the first approach, but
$T_{min}$ is unaffected by the sampling strategy. Overall, we feel that our
approach is less biased.

On further reflection, it would be possible to pick a uniform $T_{min}$ and
then build $T_{max}$ around that, but then $T_{max}$ would be non-uniform. We
can think of no particular reason to favor this approach, since researchers are
generally more interested in estimating maximum principal tectonic stress than
minimum.



## R8
> The caption for Figure 4 is truncated on p 43, and is not present anywhere
> else in the text. The figure itself is not self-explanatory, and the details
> aren't sufficiently explained in the results section 3. This seems to be an
> unfortunate LaTEX mishap, but since this model is the primary finding of this
> study and the basis for the subsequent analysis, the reader unfortunately
> cannot just "read past" the omitted details. Some of the obvious gaps are
> noted below. 


## R9
> It is not entirely clear which faults are shown in 4a, and not at all clear
> what faults or regions of space are represented in 4b-c (by the way, a b and
> c are not labeled either). What depths are represented in these models? The
> visible portion of the caption notes "same lateral extent, but different
> perspectives", but it is not clear what this means. And why is the maximum
> slip magnitude in "A" 7m, but the maximum component slips in "B" and "C" are
> 14m and 10m? 


## R10
> Also, as section 3 represents the principal findings of this study, the 
> reader would benefit from some additional discussion here of the relevant
> features of the models. For example, the text on lines 237-239 and lines
> 244-247 seem to represent and important result worthy of more attention and
> discussion. 

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

This study does indeed 


## R12
> Overall, the manuscript, though well organized, seems to have an unbalanced emphasis. The specific details of the analytical methods are present, but overall the results should be more fully described and the discussion more fully developed. 


## R13
> Line 24: Though I can see the appeal of the selected quotation, it would be more appropriate for an oral presentation or a monograph on the subject. In this context, it comes across as awkward and out of place. 

## R14
> Section 1.1: additional relevant references to consider: Fialko, Rivera, and Kanamori (2005 GJI), Ghosh et al (2006 Geology), Flesch et al (2007 GJI) 


## R15
> Lines 224-230 describe the magnitudes of stress tensor components, but this would be better explained with a figure. If not as its own figure, could Mzz at least be incorporated into figure 3? 


## R16
> Section 6.0 contrasts the methods of this study to those of Luttrell et al. 2011 study of the Maule earthquake. This is an understandable comparison, but because the Wenchuan earthquake includes both strike-slip and dip-slip components, it is actually more similar to the Luttrell and Sandwell (2012 JGR) study of Mid Ocean Ridges that includes both strike-slip and normal earthquakes as constraints. 

That study doesn't use coseismic slip models.

## R17
> The introduction lists 7 coseismic slip models of the Wenchuan earthquake (line 124), and then the analysis refers to 5 of them (line 213). As the authors noticed, all these models essentially draw from the same set of geodetic data, and all have essentially the same result, and thus all give this study essentially the same result (line 343). Is there a reason these particular models were chosen for analysis? Why not just choose one, or if they truly are different enough to influence these results, why not use them all? Some justification of this choice is warranted. 



## R18
> --Typos 
> Lines 177 and 182: is z positive up or down? Clarify this 
> Line 258: earthquake, not fault, initiated 
> Line 274: "are" -> "and"? complete sentence with period 
> Line 509: typo, delete "to close" 
> Line 556: If you acknowledge some of your data sources, you should acknowledge all of your data sources (e.g., scientific drilling, WSM, etc) 
> Fig 3 and 9 need 33ºN label correction 
