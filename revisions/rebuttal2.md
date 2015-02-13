
## General criticisms
>1 The grammar and spelling of the manuscript needs to be carefully checked.

In addition to errors caught by reviewers, we have rechecked and corrected
other errors.

>2 The fault geometry needs to be identified early in the manuscript. Right
now, the manuscript does not describe the fault dip anywhere, and this will
cause readers unnecessary difficulty.  These difficulties are particularly
apparent in section 3.

As described below, we have added descriptions of the faults in the text,
and made some figure annotations that we believe will be helpful. We state
here, as below, that the fault geometry is variable within each slip model
and between slip models, such that we cannot state a fault geometry as a
simple strike and dip.

>3 The manuscript confuses (or fails to clearly distinguish between) tractions
and stresses in several places. My experience is that this is common in the
Earth science community. It might be useful in an introductory section to state
that tractions are vectors that act on a particular plane, where as the stress
at a point is a tensor quantity.

We believe that most or all of our readers will know the difference
between tractions and stresses.  Stresses on faults are commonly
referred to as 'shear stress' and 'normal stress', instead of 'shear
traction' and 'normal traction'. One of us (EAH) has used both
terminologies in past papers. We also note that the influential paper
by Jim Rice ("Spatio-temporal complexities of slip on a fault", 1993,
JGR) uses "shear stress" for the stress acting on the fault, a
terminology that has become common in the "Rice school" of earthquake
dynamics.  Whether we are referring to tensors, vectors, or scalars
should be apparent and cause no confusion.

> 4 In several places I had difficulty telling whether the manuscript was
referring to points on the faults or to the fault as a whole. The manuscript
should make the distinction clear.

We have looked over the manuscript for this sort of problem but are not
sure where the reviewer is having trouble, beyond specific comments that are
addressed below.

> 5 The notation for stresses is unconventional, and that makes the manuscript
unnecessarily difficult to read. A more standard notation would be helpful.

We do not agree that it is quite so unconventional, and we have our reasons
for using the notation we chose; we have explained this below, and added some
discussion of this in the manuscript.

> 6 I think it would be better to describe certain distributions or functions
as posterior distributions or posterior functions rather than as “posteriors”
to avoid unintended reactions from some readers.

The term 'posteriors' has been well established in the literature for
decades and is unlikely to cause offense. Furthermore, the posteriors
we present in this paper are not function or distributions, but samples
of an unknown posterior PDF. We believe that our description of the
sampling methodology in section 4.2 makes this clear. We also note
that one of us was quite confused as what the the unintended reaction
from the term "posterior" might be.

> 7 The figures and the text need to be better coordinated so that readers can
easily verify points made in the text when the figures are referred to. Several
of the figures can be modified to make them more useful to the reader. These
modifications should not be time-consuming to make.

We have made some minor modifications to figures to address this issue.

> 8 A key modeling assumption seems to be that fault slip is not affected by
stress changes accompanying the fault rupture, but this assumption is not
stated. I think it should be.

We agree that this is important to state and did not realize we had
not in this manuscript. As stated, our model is  predicated
upon the Wallace-Bott assumption that fault slip occurs in the
direction of maximum shear stress, implicitly in that assumption is
that coseismic slip rake reflects accumulated shear stress on the
fault prior to earthquake nucleation, and that dynamic stresses do not
result in a significant re-orientation of coseismic slip. To make this
more clear, we have slightly modified the relevant sentence in the
abstract to:

"We estimate the tectonic stress needed to overcome topographic and
lithostatic stresses by assuming that the direction of maximum shear
accumulated on the faults is roughly collinear with the inferred
coseismic slip."

And in section 4.2, where we state the Wallace-Bott assumption, we
added "prior to the initiation of the earthquake" to make this clear.

> 9 The comparison of the Beichuan fault to an optimally oriented fault needs
to be clarified. This seems to be a key point, but the discussion of this point
is not sufficiently clear.

We have reworked some of this, based on the comments.  However, it does seem
that the reviewer missed the key point that friction on the Beichuan fault
is less than friction on the hypothetical optimally-oriented faults, though
this is quite clear in the text.

## Specific Comments

### Abstract

**CA.1**

> Do they mean the whole fault was verging on failure at the time of the
earthquake, or only part of it?

We have changed the relevant sentence to "We further estimate the static
friction and pore fluid pressure assuming that the fault was*, on average,* at
Mohr-Coulomb failure at the time of the Wenchuan earthquake."

**CA.2**

> Do they account for the topographic perturbation of the tectonic stresses in
coming up with this estimate? See for example Savage and Swolfs [1986].

We do not, because the method of Savage and Swolfs (as well as Liu and Zoback,
from whom we take our methods for topographic stress calculations) assume
an *a priori* tectonic stress value that is a constant. However, we assume that
tectonic stress is a tensor field that increases with depth; and we do not know
it *a priori*. Therefore, it is difficult to determine what the perturbation
to tectonic stresses is.

We have explained this more as part of the previous revisions.


### 1. Introduction

**C1.1**

> The only omission in literature coverage I am aware of is the work by
McGovern on topographic stresses associated with volcanoes. I think some of
McGovern’s papers from the 1990’s should be cited.

We have looked over these references, which are largely about volcanic
deformation on other planets, and have not found a good place to cite
them, without making a separate paragraph for discussions of
topographic stresses in volcanoes. This is far from our topic (the
interaction of topographic stresses and tectonics), and we did not
rely on these papers while developing the work presented in this
paper, so we don't feel it necessary to cite them.

**C1.2**

> This is the section of the manuscript where both the strike and dip of the
key faults should be stated.

We have added a paragraph and a half of description of the faults to the
introduction in the previous round of revisions.

**C1.3**

> (40-41) Referring to the Qur’an (or any other religious text) as one might
refer to a peer- reviewed scientific article is highly inappropriate. This
reference must be eliminated.

This reference has been eliminated, although we note that we feel it
 is unfortunate that these sorts of walls exist in scholarship. The
 history of ideas shouldn't be segregated so. We felt that the
 quotation was appropriate for the topic of this manuscript, and we
 did refer back to it later in the text. We are not sure that if we
 had chosen an opening quotation from a non-religious text, say James
 Joyce's Finnegans Wake, whether there would have been such a visceral
 reaction.  Finally, we did not refer to it 'as one might a
 peer-reviewed scientific article'. That all being said, we have
 removed the quotation.

### 2. Topographic stresses on the Longmen Shan faults 

**C2.1**

> This section came across well. I do think a description of the mechanics
behind equations 5 and 6 would be helpful though.

**C2.2**

> (169-170) The authors should be a bit more clear about some of the
limitations of the method of Liu and Zoback [1992]. That method cannot be used
to accurately calculate the topographically-induced stresses at shallow depths.
I think the method of Liu and Zoback is fine to use for the problem at hand,
but the method is not exact, and it does have its limitations. Those
limitations should be pointed out.

We change the sentence introducing the methods to "They show that the
topographic stress tensor field *beneath (but not within) topography*
can be determined by a convolution of topographic loading functions
with Green's functions describing the stresses in an elastic halfspace
due to a point load at the surface." (changes in
italics). Additionally, in Section 2.2 on the numerical implementation
of the methods, we mention that our calculations only apply to depths
below 851 m below sea level, which we take as our reference surface of
the half-space. We also now specifically state that z=0 corresponds to
mean sea level in our description of these calculations in Section
2.1.

**C2.3**

> (172) Why is M used to designate stress rather than $\sigma$, as is
conventional?  Some people might think M is for Moment. I strongly recommend
using σ for stresses.

Capital letters are quite commonly used to denote matrices, tensors, and
tensor fields. *M* is clearly defined in the manuscript.

See the response to Comment 3.9b, where we add text to the manuscript
explaining our notational usage.

**C2.4**

> (174) The line immediately after all the equations is indented and shouldn't
be. The indentations are supposed to signify the start of a new paragraph.

These are fixed.

**C2.5**

> (206-208) The open-source package is nice to make available to the community.

Yes, hopefully this will be useful for others in the future.

### 3. Results of topographic stress calculations on the Wenchuan faults

**C3.1**

> The manuscript needs to present figures and refer the reader to them to
verify the statements made in this section about the stresses. Right now
I can’t tell where to look to do this in several places in this section. Has
the manuscript omitted a figure?

No, the manuscript isn't missing any figures. Our results for this section
include each of the six stress tensor components, as well as the resolved
tractions ($\tau^M$, $\tau_d^M$, $\tau^M_s$, $\sigma_n^M$) for each of the six
coseismic slip models we've used. This would be 60 subfigures, clearly too many
to include as figures in the manuscript, so we have selected the most
illustrative results. All of the results are publicly available as .csv files
in the GitHub repository for project, and readers are welcome to download and
analyze these datasets if they wish to verify our claims, or otherwise inspect
the results. We have added a sentence informing readers of this to the end of
the first paragraph in Section 3:

"(Results not shown in figures are available as .csv files at
http://github.com/cossatot/wenchuan_topo_stress/)."

Additionally, in response to comments in the earlier round of revisions, we
have added vertical stresses to Figures 3 and 9.

**C3.2**

> Also, the manuscript needs a figure showing the model geometry. Also, I have
difficulty with the non-standard notation.

As mentioned in the response to Comment 1.2, we have added a descriptions of
the coseismic slip models used, and on the general geometry of the relevant
faults, to Section 2.3, as part of the previous rounds of revisions.

Additionally, as is evident in Figure 4, there is considerable variation in the
fault geometries assumed or inverted for by different researchers, so it is not
possible to accurately show a figure with model geometry, because there is no
real consensus on it. (To be clear, shallower than about 8 km depth, all of the
slip models we've used are quite similar in geometry and location, but below
this depth they start to diverge, as some models assume planar geometry and
others assume listric geometry, and so forth).

We have added some annotation of the dips and depths of various parts of the
slip models shown on Figure 4, in order to help readers.

The issue with notation is addressed in the response to Comment 3.9b.

**C3.3**

> Much of this section needs to be reworked so it is clear to the reader.

Specific criticisms of clarity are addressed in the following
comments and responses.

**C3.4a**

> (220) What is the purpose of the superscript M here for the traction
components? If does not seem to serve a purpose. Is it to designate tractions
due to topographic loads? If so, I recommend the authors be more explicit about
that.

Yes, the superscript M denotes the topographic origin for stresses. See the
response to Comment 3.9b.

**C3.4b**

> (220) See my comment on line 243 regarding the notation.

See our response to Comment 3.9b.

**C3.5a**

> (222-230) I can’t tell where to look to verify the statements about
stresses. Which figure, for example, shows Myz, the vertical normal stress?
Which figure shows Myz, the horizontal shear stress on a vertical plane that
strikes north?

See our response to Comment 3.1.

**C3.5b**

> (222-230) At what depth or location is the first sentence of the paragraph
referring to?

This sentence ("Topographic stresses on the Wenchuan faults are on the order
1-10s MPa") refers to the entirety of the faults, although it is a general
sentence and there are a few points on the faults where the stresses are below
this range.

**C3.6**

> (225-226)  Which figure shows the vertical normal stress? I can’t see a plot
in Fig. 3 or Fig. 4 that shows the vertical normal stress.

See our response to Comment 3.1.

**C3.7**

> (240-241) Which figure should the reader look at to see the faults in the
model?

We have added a reference to Figure 4b and c.

**C3.8**

> (242) Where are the locations being referred to here? What are their x,y,z
coordinates (or latitude, longitude, and depth)?

The Pengguan fault is shown on the maps (Figures 1, 3, 9). The flats in the
Beichuan fault are at the base of the southwestern part of the fault, as is
evident in Figure 4, which shows some of the fault models. We think that giving
'x,y,z' or other spatial coordinates would be quite unhelpful (particularly for
curved surfaces tens of kilometers in breadth), so we will not do this.  If
readers need to know this information, they can look at the .csv files on
GitHub or consult the sources for these published slip models.

**C3.9a**

> (243) What is the dip of the fault in question?

This varies in the different fault models considered. All of the
coseismic slip models we consider in this paper were developed by
other researchers (with the exception of Feng et al. (2010), of while
one of use is a co-author) and have been fully described in
peer-reviewed published papers. If the reader wants to know these
specifics, he or she is welcome to read the papers that have produced
the fault models we use.

**C3.9b**

> (243) The notation here, where M (with
double subscripts) refers to a stress, $\sigma$ (with a single subscript) to a
stress (but it would be more appropriately called a traction), and $\tau$ (with
a single subscript) to a stress (but again it would be more appropriately
called a traction) is very confusing to me. I strongly recommend using a
convention like so:

>$\sigma_{ij}$ = stress

>$\tau_n$= normal traction on a fault

>$\tau_s$ = strike-slip traction on a fault

>$\tau_d$ = dip-slip traction on a fault

>This is much more in keeping with standard usage and would be easier for
(most) readers to follow I think.


We use $\tau$ for shear stress (tractions), which is quite standard
and we define our usage in the paper.  We also use $\sigma_n$ as
normal stress (traction) which is also standard and defined in the
paper. We use *M* to denote the topographic stress tensor or tensor
field, and it is clearly defined as such. Capital letters are
commonly, although not exclusively, used to denote tensors and tensor
fields, in a variety of sources, spanning structural geology, fluid
dynamics, mathematics, and engineering disciplines.

We considered adopting the reviewer's suggestions (outside of using $\tau_n$
for normal stress) but in the end we do not use $\sigma$ to represent a stress
tensor or tensor field because we would have to exponentiate it to, for
example, $\sigma^{M^B}$ or $\sigma^{M,B}$ when referring to the stress tensor
field resulting from the convolution of topography with the Boussinesq Green's
functions. This is unwieldy. It would also be quite awkward to refer to the
normalized (dimensionless) tectonic stress field as $\sigma^{T^{\prime}}$ even
though it does not have values in Pa, or we could keep it as $T^\prime$ which
could further confuse readers as it is then one more step removed from *T*.

We have added an explanation of our notation to the first paragraph of Section
2.1:  "Note that in this work, we use capital letters (e.g., $M$, $T$) to
denote tensors and tensor fields (depending on context, which should be clear)
and Greek letters ($\tau$, $\sigma$) to denote stress components projected or
resolved on planes, which are more properly called tractions. We use
superscripts on these symbols to denote the origin of the stresses, and
subscripts to denote components of these tensors or stresses or tractions."


**C3.10**

> (244-245) Which figure should the reader look at to verify the statement
here?

We disagree that a figure is necessary, or particularly helpful, to verify a
claim that vertical stresses resolve more as normal stress than shear stress
on a plane with low dip. This should be apparent to readers who have taken a
course in Structural Geology or who have a continuum mechanics background,
which surely includes the vast majority of our readers. Readers without this
background will unfortunately have a quite difficult time with the paper, but
they are not our intended audience.

**C3.11**

> (249-251) I don't see where to look to verify the nature of the slip and the
tractions on Figure 4.  The blue background color of the slip magnitude figure
(upper left) looks very uniform, so I can't tell where the slip is high; also
note that the contour lines are not labeled with magnitudes. In the normal
stress plot in the upper right the red background color is very uniform, so
I can't tell where the normal traction is high (and the contour lines are not
labeled). This means I don't know how to compare the plots.

The colors shown are not simple 'background colors' but correspond to
the magnitudes of the stress component in question, this is stated in
the figure caption and the associated color bars in the figure. Where
they are uniform, stresses are uniform. Labeling the contours would
add unnecessary	 clutter to the figures, making them harder to
read. The relevant comparisons (for example, between high normal
stress and low slip) are still quite evident to us, both on the screen
and in print, and other viewers have not had problems with this.

**C3.12**

> Where are these other fault patches? How big are they? Can the authors point
the reader to a figure to show these patches?

The 'other' fault patches are those that are not the ones described (i.e. fault
segments that are not the southwestern portion of the Beichuan fault). Figure
4 (referenced immediately before the sentence in question) illustrates where
the observed correlation between slip and normal stress is strong and where
it is not.

### 4. Calculations of tectonic stress, fault friction and pore fluid pressure

**C4.1**

> This section reads fairly well, although a fuller description of the Bayesian
statistics would have helped me.

We believe that we have explained the mathematics involved in our
calculations (Bayes' rule, the misfit equation, and the likelihood
equation, which are equations 10-12 in the original submission and
equations 11-13 in the revised submission). These are uncomplicated
expressions, and we believe that they fully describe our estimation
strategy within a Bayesian sampling methodology.  We have tried to
define and explain each of the terms, but we do not feel that a more
basic and general introduction to Bayesian methods is appropriate in
this paper. We cited two excellent texts [Tarantola, 2005; Mosegaard
and Tarantola, 1995] that explain Bayesian estimation in more detail.

**C4.2**

> (256-257) The statement here should also account for cohesion, although the
frictional resistance could be much larger than any intrinsic cohesion

This is true; we have added "and assuming that cohesion is negligible"
to the sentence describing the Mohr-Coulomb failure envelope.
***NOTE: I will remove "rock strength" from the main text, since you are talking about a failure on a pre-existing fault, it is misleading, let's just leave as "cohesion".***

**C4.3**

> (258) I think the authors mean when the earthquake initiated, not the fault.
The fault is presumably millions of years old.

Yes, this is what we meant.  We have replaced 'fault' with 'earthquake' in this
sentence.

**C4.4a**

> (265) The phrase "posteriors of T" could have unanticipated (and undesirable)
reactions from some readers. I suggest using the alternative phrase "these
functions". 

The use of the word 'posterior' in statistics is well-established and
is fairly commonly used in geophysical research papers that utilize
Bayesian estimation or inferrence. Additionally, as described in
section 4.2, our sampling estimation strategy results in samples of
some unknown posterior probability density function, this is the
solution to the inverse problem in a Bayesian sense, and so refering
to these collections of posterior samples as "functions" would be
misleading.


**C4.4b**

> (265) Also, what is "T"?

*T* has been defined in this sentence as part of the previous revisions.

**C4.5**

> (274-275) The grammar and punctuation here need to be corrected.

We have fixed these problems as part of the previous revisions.

**C4.6**

> (276-287) Owing to my poor background in Bayesian statistics, I cannot
comment knowledgeably on the technical aspects of this paragraph except for one
point.  The authors should clarify whether the are evaluating the direction of
slip based on the conditions before the fault has begun to slip or as the fault
slips and the stress field around the slipped patch is evolving.

The direction of slip is given by the coseismic slip models, which are
the net slip from the earthquake; this is described in Section 4.2.
We think the reviewer is addressing whether under the Wallace-Bott
assumption the final coseismic slip rake is parallel to the direction
of maximum shear stress accumulated on the fault prior to slip
initiation, and that dynamic stresses do not affect the coseismic slip
rake. We address this point in comment 8 above.

**C4.7**

> (290) The authors need to clarify what orientations they are referring to
here.

We have clarified the orientations as stress orientations.

**C4.8**

> (291-292) The statement here is true, but only because the lithostatic
stresses are defined to have a horizontal components equal to the vertical
components. The <u>definition</u> of the tensor L thus plays a key role in the
results.

Yes it does, but we have been explicit in our definition of *L* (section 4.1).


**C4.9**

> (293-294) Is the maximum tectonic principal stress being referred to here? If
so, I think it would be a good idea to state it here, even though the topic
sentence of the paragraph deals with principal tectonic stresses. It is very
important that the critical thoughts in the manuscript at this point be crystal
clear to the reader.

We have added 'tectonic' to 'maximum principal *tectonic* stress' and 'minimum
principal *tectonic* stress' to clarify this in these sentences.

### 5. T, $\mu$, $\phi$ results

**C5.1**

> Owing to my poor background in Bayesian statistics, this section was
difficult for me to understand. Other readers might be in the same situation.
I think the section would be substantially improved if it concluded with a new
brief paragraph that was written “in plain English” that gave the key points
the reader should take away from this section.

We do not find our descriptions of the results to require much of a knowledge
of Bayesian statistics.  It might be that the notation (which is the standard
notation of conditional probabilities) is confusing, but this is defined in
the preceeding sections.

**C5.2**

> In spite of my shortcomings in Bayesian statistics, I am pretty sure the key
point that the reader should take away from this section is not provided by the
last sentence in the section (“On the other hand, it is not similarly sparse on
the low-μ side, suggesting that low values for μ are more robust.”).

The placement of the key points of a section to be in the last sentence of that
section is a stylistic preference, and not one that we share (why not put the
important information towards the top of the paragraphs rather than at the
end?). There is not really a 'key point' here per se; this is a description of
the results. The important results are discussed as such. 

**C5.3**

> (328-330) After this sentence, say what the significance of the peak in
T'(min) at 0.2 is, as was done in lines 326-328 for T'(max).

We don't view the value of the minimum tectonic stress to be as
significant as the value of the maximum stress, and there is no simple
statement that can summarize the importance of this value (i.e. it
does not directly affect much).  We do however discuss the results
more in the discussion.

**C5.4**

> (331-332) The described ‘linear decrease’ is not linear. The histograms have
an envelope that appears to be consistently concave up. In some work I've been
involved with the difference between a linear decay and an almost linear decay
is very significant. I don't know if that is the case here, but I still think
it is important not to call something "linear" when it isn't.

We have added a wiggle word ('somewhat') so that readers do not interpret these
descriptions too literally.

**C5.5**

> (336-340) The authors describe two sets of conditions that they consider
<u>unlikely</u>. I think it would be helpful for them to conclude here what
they do think is <u>likely</u>.

We think the most likely values in our results are the most likely. When we
stated the conditions that were unlikely, we were explaining why they
were not well represented in the posteriors.

**C5.6**

> (341-345) I can't see a peak in T'(Max) at ~0.6 in any of the plots on Fig.
8. Some additional explanation is needed, at least for me.

The highest values of the $T'_{\max}$ marginal histograms at around
0.6 are evident. This 'peak' (not our wording) is not particularly
sharp, but it is clearly there; there is a steep decrease in
probability to the left of the mode and a more gradual decrease to the
right of the mode. As stated in the response letter to the previous
revision, the likelihood at 2.5 (the upper boundary of $T'$ is 60% of
the mode at 0.6.  We have amended this sentence to read '0.6-0.8' so
it is clear that we do not mean a narrow range of high likelihoods
around a single value.

**C5.7**

> (346-355) I could not follow this paragraph. Although my background in
Bayesian statistics is poor, many other readers might be in the same boat.
I think I am able to follow the general drift of this paragraph up until line
351. At that point the paragraph could reference some figures to clarify
matters, but no figures aren’t referenced. To be specific, here is what I am
referring to:

>“However, pJ(μ|D) has a lower relative likelihood on the high-μ tail compared
to the constituent p(μ|D).”

> <u>By citing the specific subfigure on Fig. 8 that shows this, the reader
would be better positioned to verify this.</u>

We have changed the sentence to read: "However, $p_{\mathrm{J}}(\mu | D)$ has
a lower relative likelihood on the high-$\mu$ tail (Figure 8d) compared to
$p(\mu | D)$ of the constituent slip model results (Figure 7)."

> “This lower likelihood of m in the joint posterior is likely bec[au]se it is
the average μ of all slip models. On the other hand, it is not similarly sparse
on the low-μ side, suggesting that low values for μ are more robust.”

> <u>How low is "low"? Can the authors be quantitative here?</u>

We added a reference to the figure (mentioned in the last response).
We would prefer that readers look at the distribution itself, as this
is the quantitative solution of the inverse problem in a Bayesian
sense, rather than a number we throw out.


### 6. Discussion

**C6.1**

> The comparison of the Beichuan fault to an optimally oriented fault needs to
be clarified. This seems to be a key point, but the reasoning is not
sufficiently clear.

We address this in the comments below.

**C6.2**

> (356-363) This paragraph seems fine, but I do note that the structural
geology literature does contain some papers that discuss the effect of stress
variations on fault slip (e.g., Cooke, 1997; Cooke and Underwood, 2001; Martel
and Shacat, 2007; Savage and Cooke, 2010; Kaven et al., 2013). These papers
contain quasi-static analyses, not dynamic analyses, but they appear as though
they might be relevant to the discussion of lines 356-363.

We have looked through these papers and do not see an easy connection to our
work.

**C6.3**

> This paragraph looks fine to me.

excellent.

**C6.7**

> (389-390) I recommend that this concluding point of the paragraph be
developed a bit more.

It is sufficiently self-explanatory, and unimportant, that we don't feel it
warrants further discussion.

**C6.8**

> (391) How does a spatial variation decrease with frequency? Space and time
seem to be being mixed here. Also, what is the amplitude that is referred to
here? Do the authors mean that the spatial variation of topographic stresses at
various depths depends on the amplitude and wavelength of the topography?

We have clarified this sentence:

"The spatial variation of topographic stresses decreases in frequency and
amplitude with depth" is now: "The spatial variation of topographic stresses
increases in wavelength and decreases in magnitude with depth."

**C6.9**

> (399) What does "this" refer to? I encourage the authors to review the topic
sentence of this paragraph as they address this question of mine.

We have replaced "this" with "the relationship between stress variation, slip
variation, and depth", which is the topic of the paragraph.

**C6.10**

> (402) Neither the dip nor the dip direction of the Beichuan fault has been
described, so the reader cannot verify the statement here. The strike and dip
of all the key faults need to be identified.

As stated in response to Comment 1.2, we have added a section in the
introduction describing the faults and coseismic slip models.

**C6.11**

> (403-404) The authors should be very careful with the wording here. They have
just described the magnitude and orientation of Tmin, and many readers might
interpret the phrase “This stress configuration ... is in close agreement
[with] pre-earthquake stress measurements...” to mean that the measurements
include magnitude and orientation. Fig. 9, however, shows only orientation
data, not orientation and magnitude data. To my knowledge, borehole breakout
data have not proven yet to be reliable indicators of stress magnitudes.

We have changed the sentence from "pre-earthquake stress measurements" to
"pre-earthquake stress orientation measurements".

**C6.12**

> (413-414) Cite a figure to buttress the statement here.

A reference to Figure 8 has been added.

**C6.13**

> (415) What does the word “This” refer to? Again, I think referring to
a figure would help here considerably.

'This' changed to 'These results'.

**C6.14**

> (421-422) Check the grammar here. A word seems to be missing.

We have added 'any' which makes the sentence a bit more parseable.

**C6.15**

> (423-424) I'm not quite sure what the authors are trying to say here. I think
the wording here should be revised to clarify the sentence.

We have modified this sentence, which now reads "The orientation of both the
tectonic and total stresses near the Wenchuan faults shows a larger difference
with patterns of strain from elsewhere in the orogen *than in the Longmen Shan
region*." (changes in italics) which hopefuly clarifies our meaning.

**C6.16**

> (436-437) Need to revise the grammar here.

Revised.


**C6.17**

> (451) Where would these more optimally oriented faults be located, and how
would they be oriented?

As we state in the paper, these calculations apply to each point in the
coseismic slip model, so the optimal faults would be collocated with the
points of the slip model. Because we treat each point independently and
the comparisons are of local stresses, it doesn't make a difference that
with different orientations, the optimal faults wouldn't align into a single
plane.

**C6.18**

> (434-479) The conclusions of this paragraph, that the Beichuan fault is more
likely to slip than an optimally-oriented fault, will strike most readers as
impossible. How could the Beichuan fault be more optimally oriented for slip
than a fault that has the optimal orientation for slip? The "best" (in terms of
slip probability) that could be hoped for is that the Beichuan fault has the
orientation (and position) of the optimally-oriented fault, and therefore is
the optimally-oriented fault. How is it possible that slip on the Beichuan
fault is favored by a factor of as much as 1000 (the anti-log of 3) over the
optimally-oriented fault? I think the answer lies in the definition of what
constitutes the optimally-oriented fault. This needs to be more clearly and
completely explained to avoid confusing readers.

As described in the manuscript, the 'optimally-oriented fault' has a
canonical value of friction of 0.6 (lines 466-469 of the submitted
manuscript). In contrast, our model results indicate that the faults
that are thought to have ruptured in this event have a much lower
coefficient of static friction.  As is shown in Table 2, the
coefficient of friction on the fault has a strong influence on the
favorability of slip on the Wenchuan faults vs. optimally oriented
faults of the stress parameters studied.  This is stated repeatedly
throughout this section, so we do not believe that we are unclear
about this point.

Additionally, when we did the log transformation of the y-axis of Figure 10,
we used the base-*e* log, not base-10; the anti-log of 3 in this case is ~20,
which is far more reasonable value than 1000. We have updated the text and
figure captions so that 'log' now reads 'ln' to avoid this confusion.

Nonetheless, we have reviewed our code and found a slight error in how
the optimal slip plane was calculated; essentially, the algorithm
assumed that dip slip faulting would be favored (where the optimal
plane strikes perpendicular to the trend of $\sigma_1$) but produces
an incorrect orientation otherwise.  We have fixed the bug, which has
changed these results slightly (the bug only affected these
calculations; that particular function was not used in the rest of the
study). The new Figure 10 shows that more of the data plot in the
favorability region for optimal faulting than previously; however,
most of the data (with low friction values) still plot in the
favorability region for the Wenchuan faults.

We have also added some discussion of how the calculated ratios relate to the
parameters:  

"It is clear that both $T^\prime_{xx}$ and $\mu$ are strongly correlated with
$\mathrm{CFR}_o / \mathrm{CFR}_f$, and $\phi$ is to a lesser degree; nonetheless,
all significantly affect the relative ease of faulting on the Wenchuan faults
versus optimal faults. In particular, lower values for any of them favor slip
on the Wenchuan faults. The lowest $\mathrm{CFR}_o / \mathrm{CFR}_f$ value
($\sim$ 0.057, $\sim$ -2.9 in log space ) corresponds to the lowest value of
$\mu$ ($\sim$ 0.038), and is approximately the ratio of $\mu$ in the model to
0.6."


**C6.19**

> (480) I find more and more careful writers are reserving the term
"significant" to discuss "statistically significant" matters. That is not quite
how the term is being used here, even though the manuscript deals quite a bit
with statistics. I think the term "substantial" would be a better choice here.

This is an excellent suggestion.

**C6.20**

> (488) Cite a reference on deformation in Tibet to support this point.

We have added three references here.

**C6.21**

> (493-496) This sentence needs to be revised. The punctuation and/or grammar
here needs some revision (the semicolon is what initially caught my attention),
but the sentence contains too many incomplete thoughts without saying what the
main thought is. Also, if “much work has been done”, then wouldn’t it be
appropriate to cite more than one reference at the end of the sentence? See my
suggestion for rewording.

Grammatical changes to the manuscript were made as part of the previous round
of revisions. We have added a few more references to the sentence.

**C6.22**

> (499) I think a new paragraph should be started after the word "crust" here.
The sentence that starts with the word "However" does not really constitute the
conclusion of this paragraph as well as it perhaps serves as the topic sentence
for the next paragraph.

We disagree with this stylistic point. That paragraph discusses how the
treatment of large topographic or orogenic features as smooth and homogeneous
is an oversimplification, and the 'however' statement serves as a
counter-argument. It is also meant to lead to the next paragraph.

**C6.23**

> (504) Cite a reference. Say who noted this point.

This sentence clearly discusses our results.  We have added a reference to
Section 3.

**C6.24**

> (509-510) I think this statement is a bit too general considering what Fig.
3 shows. Near the southeast end of the fault trace, the most compressive
horizontal stress trends nearly normal to the fault trace. Near the northeast
of the fault trace, the most compressive horizontal stress trends nearly 60
degrees counterclockwise from the fault trace. So the relative orientation of
the most compressive stress relative to the fault trace trend varies with
position along the fault, not just the position perpendicular to the fault
trace. The relative orientation changes more along a traverse perpendicular to
the fault at the SW end of the fault than the NE end (I see little variation in
the stress trajectories there along a traverse normal to the fault trace.
I think the authors should be a bit more nuanced with their statement here.

We disagree with the reviewer's interpretation of the results in Figure 3.  The
orientation of maximum topographic stress in the southwest (the fault strikes
SW-NE and has no 'southeast end') rotates nearly 90 degrees from under the high
Longmen Shan across the fault into the Sichuan Basin. Close to the fault, the
orientations change very little along strike.

Additionally, this part of the paragraph concerns the loading of thrust flats
in the southwestern Beichuan fault. The coseismic slip models in this study
do not have these kinds of structures in the northeast, so the situation there
is not relevant.

**C6.25**

> (510-511) The direction of the most compressive principal stress apparently
is being equated with the direction of the greatest displacement. That
equivalence is incorrect. If the fault exhibits thrust slip, a displacement
component will exist normal to the trace of the fault.

If the fault exhibits a thrust slip, it will also have a component of the
greatest principal stress normal to the fault trace...  We are not sure of what
this comment is really referencing or what an appropriate revision would be.

**C6.26**

> (514) I think the authors need to say just what a "channel" is.

We reference several studies discussing channel flow in Tibet in this paragraph
and in preceeding ones. This part of the discussion is sort of an ancillary
section relating our results to several popular ideas about orogenic dynamics
and development; readers who are interested may look at those, but suffice it
to say that no strict definition of what an orogenic channel is exists beyond
the basic definition of a channel as an area of increased velocity and/or
decreased viscosity in between more rigid walls.

**C6.27**

> (517-519) think the thoughts in this sentence might come across more clearly
if the sentence is broken into two pieces. This sentence constrains more
thoughts than easily fit into one sentence.


I think this sentence was actually too unconstrained by thoughts, because it
doesn't make much sense several months later. I have rewritten the sentence to: 

Our calculations of $\mu$ and $\phi$ are based on $T$, which is biased towards
the high slip patches in the upper crust (Equation 11).  The resulting low
values of $\mu$ and low to moderate values of $\phi$, probably yield stress
conditions insufficient for slip at high pressures found at depths > 10 km.


**C6.28**

> (524) Good paragraph.

Thanks!


### 7. Conclusions

**C7.1**

> The conclusions are straightforward and follow from the preceding material.
Please note, however, my comments on lines 544-547.

**C7.2**

> (536) Why are the absolute value bars included here?

Our convention in this paper is that positive values for $\tau$ indicate
reverse to right-lateral shear while negative values indicate normal to
left-lateral shear (Section 3). The absolute values are there because we
see shear stresses with both signs up to that magnitude.

**C7.3a**

> I don't think the data support going to four significant figures here. Two
significant figures seem more appropriate.

Changed.

**C7.3b**

> Stress has dimensions of MPa, not MPa/km.

In this study, we parameterize tectonic stress as a function of depth.
We have changed 'MPa km$^{-1}$' to 'MPa per kilometer of depth' to make this
more clear.

**C7.4**

> (544-547) It seems odd to give the most compressive stress to four
significant figures, and then in the next sentence describe the least
compressive stress qualitatively (no significant figures). I recommend that the
authors give quantitative values for both.

We have reworded this sentence for clarity, and given the results with both
more quantitative and less precise values, as suggested.

**C7.5**

> (550-551) I find that avoiding one-sentence paragraphs generally is good
procedure. I suggest expanding this final paragraph to at least two sentences,
or else merging it with the preceding paragraph.

We have merged it with the preceding paragraph.

### Appendices

**CAp1**

> I can't read equation (A9) because it is overwritten by the date.

This is a LaTeX problem which we couldn't easily fix and won't be
an issue with the final version.

**CAp2**

> Equations (A4)-(A6) match the solutions in Mal and Singh (1991), but
equations (A1)-(A2) do not match and have errors. Owing to the different
elastic coefficients Mal and Singh use, I can’t tell if equation (A3) is
correct or not. Also note that G must have dimensions of force/area, which
equations (A4)-(A6) do, but the lead terms in square brackets in equations (A1)
and (A2) do not. Aside from those differences, the elastic coefficients need to
be defined. Similarly, equations (A10) and (A12) match the solutions in Mal and
Singh (1991), but I can’t tell whether equations (A7)-(A9) do because of the
different elastic coefficients. Since the authors did not derive these
equations, they could simply cite a reference and they would not need to
include an Appendix, although they should check to make sure the errors in
equations (A1) and (A2) did not spill over to their codes.

The equations have been amended (a *z* was missing in the numerator of
the first term in the brackets). The mistake is not found in the code.
This fixes the unit problem mentioned.  We reproduce the equations
from Liu and Zoback [1992] here for completeness. Since we define
these equations using different notation, we beleive that if we just
referred to Liu and Zoback [1992] there might be some confusion for
readers trying to reproduce our results. We thank the reviewer for
catching the typo in equations (A1) and (A2).

**CAp3**

> For equation (6), what is σ B? Should it be M B? Also, shouldn't the
subscripts for F be h,y yy yy instead of h,yz?

Yes, $\sigma^B$ should be $M^B$, and $F_h,y$ instead of $F_h,yz$.

**CAp4**

> In equation (5) why are all three terms on the right side of the equal sign
in the first row multiplied by dh/dx? I can see why the ρgh term is, because if
the surface has a slope, then the slope will impart a horizontal shear stress.
I don’t understand why Mxx and Txx are multiplied by dh/dx though, because Mxx
and Txx already act horizontally. Similarly, why are Mxy and Txy multiplied by
dh/dy in the second row of the equation? Analogous comments apply to equation
(6). An explanation of this would be helpful.

Liu and Zoback [1992] devote some attention to the horizontal loading
function (primarily, see the "Effect of Topography on Tectonic Stress"
Section in their paper). While we do state in the beginning of the
section that we use methods derived by Liu and Zoback [1992], we
realized that we should also cite their paper where we give the
horizontal loading function, and we have edited the sentence equation
(5) to state that these loading functions are derived by Liu and
Zoback [1992].

Yes, Mxx, Txx, Mxy, and Txy act horizontally, but they represent
normal tractions in horizontal directions on vertical planes, and not
tractions on the free surface. Mxx, etc, above the reference level,
here taken to be mean sea level, only excite shear traction on the
free surface (warranting their inclusion into the horizontal loading
function) if topography varies. We think of this as due to the fact
that you are changing the total size of the vertical planes that
tractions resulting from Mxx, etc, are acting upon. This change in
horizontal normal tration results in a shear stress on the reference
surface and stresses are propagated into the half-space via the
Cerruti solutions.

### References

**CR1**

> I have not checked all the references because of time constraints.
I recommend adding at least one reference by McGovern and some of the suggested
references mentioned regarding lines 356-363.

We have not found any of these references to be appropriate.

### Figures and Captions

**CF1**

> Is the “Grey box” mentioned in the last sentence of the caption referring to
the small box in the inset figure in the lower right corner?

No, it's the oblique hollow grey rectangle in the center of the figure, labeled
'Figs. 3,9' (which is also referenced in the caption).

**CF2**

> What do the red and blue areas represent? They are what immediately attract
the reader’s eye, not the traction arrows. The emphasis should be on the
traction arrows in my opinion.

They represent crystalline rocks (in pink) and sedimentary basins (in blue).
The colors were chosen to match some of the geologic maps of the region.
We have explained the colors in the caption.

**CF3a**

> The explanation should define all the symbols on the map, including the
traces of the thrust faults. 

The thrust fault symbols are standard across geology and geophysics and have
been for decades.

**CF3b**

> Are the fault traces shown the traces of real faults or model faults?

These are real faults.  As described in the caption for Figure 1, they are
active structures taken from Styron et al., 2010.

**CF4**

> I can’t tell what the plots in this figure represent. Are they plots of the
slip and various stresses on the plane(s) of the model faults? The caption
needs to be very clear about what these figures represent. 

The first sentence of the caption reads: "Southwest-looking views of
topographic stress and coseismic slip on selected slip models." This should
clearly answer the reviewer's question here affirmatively.

**CF4a**

> The sub-figures here need to be labeled, and the subfigure in the upper
right or “normal stress” needs to describe the orientation of this normal
stress component. 

Normal stress is by definition oriented perpendicular to the fault. It's not
customary to describe it with other orientations, as far we we are aware.

**CF4b**

> Say what the dip of the model fault is here. 

The dips of the faults are variable throughout these models. We have annotated
the dips on the figure.

**CF4c**

> The caption is cut off in the pdf file I received.

There should have been a version of the manuscript without figures that clearly
displays the caption available through GEMS; at least it was visible to us.

**CF4d**

> The figure caption should say what the dip of the model fault is.

The dips of the faults are variable throughout these models. We have added
some annotation with dips in various places on the figure.

**CF4e**

> Is the slip being modeled in this manuscript, or is this the slip that
was modeled by others? If the slip is being modeled here, the manuscript needs
to say what the boundary conditions are along the model faults. 

No, the slip is not being modeled here, and we are quite clear that we use
published coseismic slip models.

**CF4f**

> Where to the “selected slip models” come from?

From the sources listed in the caption.

**CF5**

> Fine.

**CF6a**

> What do the subfigure labels (e.g., “Zhang”, “Feng”, etc.) mean? Are they
faults? Authors of publications? Types of statistics (e.g., Qi rough and Qi
smooth)? 

They are the authors of the slip models used in this study. 'Qi rough' and
'Qi smooth' describe the slip models, using different smoothing techniques,
as described in the *Qi et al* paper cited repeatedly in this manuscript.

**CF6b**

> The meanings of the subplots need to be described better. Each of the
6 subplots (e.g., Zhang, Feng, etc.) has four sub-subplots. Neither the caption
nor the text describe what the upper left sub-subplot is or what the lower
right sub-subplot is. Both of these sub-subplots are solid blue. They look like
histograms, and perhaps they give the number of points in bins that represent
thin columns or rows that extend from the apparent histograms. In any event,
I’ve never seen a plot like this – and I might not be the only person in this
situation – so a more complete description of these sub- subplots would be most
helpful.

We have changed the term 'marginals' to 'histograms of the marginal
distributions' which will hopefully give the uninitiated reader some help,
or at least some more precise or formal terms which will be more conducive to
searching.  It is rather basic statistical terminology and presentation.

**CF7**

> I don’t really understand how the contour lines were drawn in this figure.
Some clarification on this would help. See also my comments on Fig. 6.

We have added that the contours 'are constructed through kernel density
estimation' to the caption for Figure 7.

**CF8a**

> What are “marginals”? I don’t know what they are, and they are not defined.

We have changed the term 'marginals' to 'marginal distributions'. This is a
common statistical term and doesn't need to be defined here, any more than
we would define 'standard deviation'.

**CF8b**

> I can’t match up the number 0.6 in line 345 with a peak in the apparent
histograms at 0.6 in this figure. Is 0.6 the correct number? If it is, could
the subfigure that shows the peak at 0.6 be labeled so the reader can see where
to look?

We have changed that line to '0.6-0.8' to make it more clear that it is not
a 'peak' but a wide area at the top of the histogram.

**CF8c**

> The histogram of azimuths” is called a rose diagram earlier in the
manuscript. Why not call Fig. 8c a rose diagram?

Would it smell sweeter if we did?  The two have the same meaning, and we are
free to use both names.

**CF9**

> The wording "Topographic and tectonic horizontal stresses" implies that the
figure shows (a) topographic stresses, and (b) tectonic stresses, yet the
figure does not show them. The blue arrows show total stresses (topographic
+ tectonic + gravity) as do the purple arrows. The red-and-black crosses show
topographic + tectonic stresses, not total stresses, and not just topographic 
or tectonic. The description of just what this figure shows needs to be more
carefully described – this might involve the text and the caption.

And' in the first sentence is more appropriate than either writing out 'plus'
or putting a plus sign in a sentence.  The blue and purple arrows are clearly
defined as stress orientations in the caption.  We don't see where this
causes any confusion, and it does not seem that the reviewer is confused
either; rather he or she has an overly restrictive view of the meaning of
'and'.


**CF10**

> The figure and its caption look fine to me.

No changes.


## Additional changes

Introduction:

We have added "We then use the Mohr-Coulomb failure criterion
to bracket the tectonic stress field, pore fluid pressure, and static friction
of the fault*, so that these parameters are consistent with the toopographic
stresses and coseismic slip on the Wenchuan earthquake faults*." to the last
sentence of the third paragraph of the Introduction, where we describe the work
(changes in italics).


Section 'Tectonic stresses in eastern Tibet'

We have changed a clause from "$T_{\mathrm{min}}$... is slightly larger than
lithostatic pressure" to $T_{\mathrm{min}}$... is a small fraction of
lithostatic pressure", as the previous statement was incorrect.
