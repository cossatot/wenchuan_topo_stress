wenchuan_topo_stress
====================

Work repository for topographic stresses and the 2008 Wenchuan earthquake.

This is a messy work folder for a scientific project, not really a software 
package per se.  But it is text-based data and code, and it is 'open source'.

Much of this project is [published in Journal of Geophysical
Research][jgr_url].  For folks who want to inspect or reproduce the
calculations there, the work is roughly laid out like this:

[jgr_url]: http://onlinelibrary.wiley.com/doi/10.1002/2014JB011338/abstract

```
wenchuan_topo_stress/
 |
 |--- /scripts: e_asia_bouss.py, e_asia_cerruty.py: Run these (bouss, then cerr)
 |                                                  to calculate regional topo
 |                                                  stresses.
 |
 |--- /slip models: folders for each model, containing a 
 |                  'calc_xx_fault_stresses.py' script to get calculate topo 
 |                  stresses on the slip models (where xx is the slip model).
 |
 |--- /tect_stress/scripts: scripts for tectonic stress inversions for each slip
 |                          model.
 |
 |--- /notebooks:  Various notebooks for things; 'cfr_calcs_revised' may be
                   the only one that has calculations actually used in the paper.

```

The code uses a Python module I wrote called [halfspace] to do almost all of
the calculations.  The code is done using `halfspace` v.0.1.5 (well, much
of it was done with previous versions but this is the least buggy and is
backwards-compatible).  I plan on some serious refactors of `halfspace` coming
up, so go to the 'versions' page and get v.0.1.5 if you want to reproduce this
work.


[halfspace]: https://github.com/cossatot/halfspace



