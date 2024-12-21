import bpy

obj = bpy.context.object

if obj.data.shape_keys:

    shape_keys = obj.data.shape_keys.key_blocks
    
    for key in shape_keys:
        print(key.name)

        # key.mute = True