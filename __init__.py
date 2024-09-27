bl_info = {
    "name": "EZRemeshes Far and Close",
    "author": "Snowyegret",
    "version": (1, 0, 0),
    "blender": (3, 6, 0),
    "location": "View3D > N-Panel > EZRemeshes",
    "description": "Automatically remesh objects to quads / tris using far or close vertex connection",
    "category": "Mesh",
}

import bpy
from . import ez_remeshes_panel
from . import ez_remeshes_operator_far
from . import ez_remeshes_operator_close

def register():
    ez_remeshes_panel.register()
    ez_remeshes_operator_far.register()
    ez_remeshes_operator_close.register()

def unregister():
    ez_remeshes_panel.unregister()
    ez_remeshes_operator_far.unregister()
    ez_remeshes_operator_close.unregister()

if __name__ == "__main__":
    register()
