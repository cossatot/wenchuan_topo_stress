wenchuan_topo_stress
====================

Work repository for topographic stresses and the 2008 Wenchuan earthquake.

This is a messy work folder for a scientific project, not really a software 
package per se.  But it is text-based data and code, and it is 'open source'.

Much of this project is currently in revision with Journal of Geophysical
Research.  For folks who want to inspect or reproduce the calculations there,
the work is roughly laid out like this:

```
wenchuan_topo_stress/
 |
 |--- /scripts: e_asia_bouss.py, e_asia_cerruty.py: Run these (bouss, then cerr)
 |                                                  to calculate regional topo
 |                                                  stresses.
 |
 |--- /slip models: folders for each model, containing a 
 |                  'calc_xx_fault_stresses.py' script to get calculate topo 
 |                  stresses on the slip models.
 |
 |--- /tect_stress/scripts: scripts for tectonic stress inversions for each slip
                            model.


```
