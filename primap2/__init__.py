"""The PRIMAP2 climate policy analysis package."""

__author__ = """Mika Pflüger"""
__email__ = "mika.pflueger@pik-potsdam.de"
__version__ = "0.2.1"

import pint
import pint_xarray

from . import accessors
from ._data_format import open_dataset
from ._units import ureg
