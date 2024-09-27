import bpy

class EZRemeshesPanel(bpy.types.Panel):
    bl_label = "EZRemeshes Far and Close"
    bl_idname = "VIEW3D_PT_ez_remeshes"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'EZRemeshes'

    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.ez_remeshes_operator_far", text="Run EZRemeshes Far")
        layout.operator("mesh.ez_remeshes_operator_close", text="Run EZRemeshes Close")

def register():
    bpy.utils.register_class(EZRemeshesPanel)

def unregister():
    bpy.utils.unregister_class(EZRemeshesPanel)

if __name__ == "__main__":
    register()