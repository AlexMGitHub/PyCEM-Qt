"""Dictionary containing FDTD scenario GUI text."""
# %% Imports
from modules.fdtd_scenarios import (
    RickerTMz2D,
    TFSFSource,
    TFSFPlate,
    TFSFDisk,
    TFSFCornerReflector,
    TFSFMinefield,
)


# %% Scenarios
fdtd_scenario_dict = {
    'ricker': {'title': 'Ricker Wavelet',
               'description': 'This scenario simulates a Ricker Wavelet source'
               ' at the center of a 2D grid. The edges of the grid have a '
               'perfect electric conductor (PEC) boundary that reflects the '
               'radiated waves.',
               'scenario': RickerTMz2D,
               },
    'tfsf': {'title': 'TF/SF',
             'description': 'This scenario simulates a Total Field/Scattered '
             'Field wave traveling across a 2D grid. The edges of the grid '
             'have an absorbing boundary condition (ABC) to capture the '
             'radiated waves.',
             'scenario': TFSFSource,
             },
    'tfsf_plate': {'title': 'TF/SF Plate',
                   'description': 'This scenario simulates a Total Field/Scattered'
                   ' Field wave impinging on a vertical PEC plate. The edges of '
                   'the grid have an absorbing boundary condition (ABC) to '
                   'capture the radiated waves.',
                   'scenario': TFSFPlate,
                   },
    'tfsf_disk': {'title': 'TF/SF Disk',
                  'description': 'This scenario simulates a Total Field/Scattered'
                  ' Field wave impinging on a circular PEC desk. The edges of '
                  'the grid have an absorbing boundary condition (ABC) to '
                  'capture the radiated waves.',
                  'scenario': TFSFDisk,
                  },
    'tfsf_corner': {'title': 'TF/SF Corner Reflector',
                    'description': 'This scenario simulates a Total Field/Scattered'
                    ' Field wave impinging on a corner reflector. The edges of the'
                    ' grid have an absorbing boundary condition (ABC) to capture '
                    'the radiated waves. ',
                    'scenario': TFSFCornerReflector,
                    },
    'tfsf_minefield': {'title': 'TF/SF Minefield Scatterers',
                       'description': 'This scenario simulates a Total Field/Scattered'
                       ' Field wave impinging on multiple circular scatterers. The '
                       'edges of the grid have an absorbing boundary condition (ABC) '
                       'to capture the radiated waves.',
                       'scenario': TFSFMinefield,
                       },
}
