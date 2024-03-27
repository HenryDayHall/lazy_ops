try:
    from lazy_ops.lazy_loading import DatasetView
    from lazy_ops.lazy_loading import lazy_transpose
except ImportError:
    from .lazy_loading import DatasetView
    from .lazy_loading import lazy_transpose

from .version import version as __version__
