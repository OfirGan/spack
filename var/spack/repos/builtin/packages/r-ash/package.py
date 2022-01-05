# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class RAsh(RPackage):
    """David Scott's ASH routines ported from S-PLUS to R."""

    cran = 'ash'

    version('1.0-15', sha256='8b0a7bc39dd0ce2172f09edc5b5e029347d041a4d508bbff3f3fd6f69450c2ab')