#! /usr/bin/env python
##########################################################################
# NSAp - Copyright (C) CEA, 2013
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

# pyConnectomist current version
version_major = 1
version_minor = 1
version_micro = 0

# Expected by setup.py: string of form "X.Y.Z"
__version__ = "{0}.{1}.{2}".format(version_major, version_minor, version_micro)

# Define default PyFreesurfer path for the package
DEFAULT_FREESURFER_PATH = "/i2bm/local/freesurfer/SetUpFreeSurfer.sh"
DEFAULT_FSL_PATH = "/etc/fsl/5.0/fsl.sh"
DEFAULT_WORKBENCH_PATH = "/usr/bin"
DEFAULT_TEMPLATE_SYM_PATH = "/i2bm/local/freesurfer/subjects/fsaverage_sym"

# Define FreeSurfer supported version
FREESURFER_RELEASE = "5.3.0"

# Expected by setup.py: the status of the project
CLASSIFIERS = ["Development Status :: 5 - Production/Stable",
               "Environment :: Console",
               "Environment :: X11 Applications :: Qt",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering",
               "Topic :: Utilities"]

# Project descriptions
description = """
[pyFreeSurfer]
This package provides common scripts:

* pyfreesurfer_reconall: FreeSurfer cortical and subcortical segmentation.
* pyfreesurfer_datacheck: check FreeSurfer 'reconall' produced data integrity.
* pyfreesurfer_conversion:  convert FreeSurfer volume, mesh , annotations
  to the native space. The produced meshes will also be aligned across
  subjects.
* pyfreesurfer_qualitycheck: check FreeSurfer 'reconall' produced data quality.
* pyfreesurfer_stats: summarize the FreeSurfer 'reconall' individual
  statistics.
* pyfreesurfer_textures: build texture arrays aligned across subjects.
"""
long_description = """
======================
pyFreeSurfer
======================

Python wrappers for FreeSurfer: wrap the FreeSurfer software and simplify
scripting calls. Such calls can be performed through the use of a
dedicated function of the package.
"""

# Main setup parameters
NAME = "pyFreeSurfer"
ORGANISATION = "CEA"
MAINTAINER = "Antoine Grigis"
MAINTAINER_EMAIL = "antoine.grigis@cea.fr"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "https://github.com/neurospin/pyfreesurfer"
DOWNLOAD_URL = "https://github.com/neurospin/pyfreesurfer"
LICENSE = "CeCILL-B"
CLASSIFIERS = CLASSIFIERS
AUTHOR = "pyFreeSurfer developers"
AUTHOR_EMAIL = "antoine.grigis@cea.fr"
PLATFORMS = "OS Independent"
ISRELEASE = True
VERSION = __version__
PROVIDES = ["pyfreesurfer"]
REQUIRES = [
    "numpy>=1.6.1",
    "nibabel>=1.1.0",
    "matplotlib>=1.3.1"
]
EXTRA_REQUIRES = {}
