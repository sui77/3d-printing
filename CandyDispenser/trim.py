import bpy

bpy.data.objects["OriginalText"].data.body = "Naschkatze"
bpy.data.objects["OriginalText"].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects['OriginalText']
bpy.ops.object.convert(target="MESH")

bpy.data.objects["OriginalText"].name = "DifferenceObject"


bpy.data.objects["Ring.001"].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects['Ring.001']
bpy.ops.export_mesh.stl(filepath=str(('test.stl')),   use_selection=True)