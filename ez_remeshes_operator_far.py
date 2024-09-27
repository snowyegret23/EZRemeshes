import bpy
import bmesh
from mathutils import Vector

class EZRemeshesOperatorFar(bpy.types.Operator):
    bl_idname = "mesh.ez_remeshes_operator_far"
    bl_label = "EZRemeshes Far Operator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        if obj.type != 'MESH':
            self.report({'WARNING'}, "Active object is not a mesh")
            return {'CANCELLED'}

        bpy.ops.object.mode_set(mode='EDIT')
        
        iterations = 0
        while self.process_mesh(obj):
            iterations += 1
        
        self.report({'INFO'}, f"Finished: Processed {iterations} iterations")
        return {'FINISHED'}

    def process_mesh(self, obj):
        bm = bmesh.from_edit_mesh(obj.data)
        bm.faces.ensure_lookup_table()

        bpy.ops.mesh.select_all(action='DESELECT')
        for face in bm.faces:
            if len(face.verts) > 4:
                face.select = True

        if not any(face.select for face in bm.faces):
            return False

        selected_faces = [f for f in bm.faces if f.select]

        for face in selected_faces:
            self.subdivide_face(bm, face)

        bmesh.update_edit_mesh(obj.data)
        return True

    def subdivide_face(self, bm, face):
        verts = face.verts
        if len(verts) <= 4:
            return

        longest_distance = 0
        v1, v2 = None, None
        for i in range(len(verts)):
            for j in range(i+2, len(verts)):
                if j != (i-1) % len(verts):
                    dist = (verts[i].co - verts[j].co).length
                    if dist > longest_distance:
                        longest_distance = dist
                        v1, v2 = verts[i], verts[j]

        if v1 and v2:
            bmesh.ops.connect_verts(bm, verts=[v1, v2])

def register():
    bpy.utils.register_class(EZRemeshesOperatorFar)

def unregister():
    bpy.utils.unregister_class(EZRemeshesOperatorFar)

if __name__ == "__main__":
    register()