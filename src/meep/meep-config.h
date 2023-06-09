/* compile-time configuration of meep that affects user linkage */

// Enable single precision builds.
#ifndef MEEP_SINGLE
#define MEEP_SINGLE 0
#endif

// Enable SWIG threads for Python. When enabled, the GIL is released for
// all SWIG wrapped calls by defaults.
#ifndef MEEP_SWIG_PYTHON_THREADS
#define MEEP_SWIG_PYTHON_THREADS 0
#endif

// Enable debugging for SWIG wrapped calls for Python. When enabled, all
// SWIG wrapped python calls are logged.
#ifndef MEEP_SWIG_PYTHON_DEBUG
#define MEEP_SWIG_PYTHON_DEBUG 0
#endif
