project('shiggy', 'c',
    version: '1.0',
    meson_version: '>= 1.1.0'
)

pymod = import('python')
python = pymod.find_installation('python3', required: true)

ar = find_program('ar')
cc = meson.get_compiler('c')

iggy_object_files = [
    'ORBIS_rrAtomics.obj',
    'ORBIS_rrCpu.obj',
    'ORBIS_rrThreads.obj',
    'ORBIS_rrTime.obj',
    'as3_component_helpers.obj',
    'as3vm.obj',
    'as3vm_abc_decode.obj',
    'as3vm_abc_dump.obj',
    'as3vm_class.obj',
    'as3vm_classes_base_dummy.obj',
    'as3vm_classes_flash_dummy.obj',
    'as3vm_convert.obj',
    'as3vm_create.obj',
    'as3vm_debugger_interface.obj',
    'as3vm_dump_value.obj',
    'as3vm_gc.obj',
    'as3vm_imp_array.obj',
    'as3vm_imp_math.obj',
    'as3vm_imp_misc.obj',
    'as3vm_imp_string.obj',
    'as3vm_interpreter.obj',
    'as3vm_names.obj',
    'as3vm_op_strings.obj',
    'as3vm_property.obj',
    'as3vm_util.obj',
    'as3vm_verifier.obj',
    'avm2_microcode.obj',
    'dtoa.obj',
    'gr_strokepath.obj',
    'iggy_allocation.obj',
    'iggy_api_functions.obj',
    'iggy_api_functions_global.obj',
    'iggy_arena_allocator.obj',
    'iggy_debug.obj',
    'iggy_file_reader.obj',
    'iggy_font_provider.obj',
    'iggy_main.obj',
    'iggy_mixer.obj',
    'iggy_platform_audio.obj',
    'iggy_platform_deps.obj',
    'iggy_sound.obj',
    'iggy_unicode.obj',
    'radss_orbis.obj',
    'rrCore.obj',
    'rrMath.obj',
    'rrMem.obj',
    'rrSyncCheck.obj',
    'rrstring.obj',
    'stb_truetype_wrapper.obj',
    'swf_as3_bitmap_data.obj',
    'swf_as3_misc.obj',
    'swf_as3_textfield.obj',
    'swf_as3vm.obj',
    'swf_as3vm_flash_display.obj',
    'swf_as3vm_flash_events.obj',
    'swf_cache.obj',
    'swf_decode.obj',
    'swf_draw.obj',
    'swf_draw_filltype.obj',
    'swf_draw_filter.obj',
    'swf_draw_interface.obj',
    'swf_draw_lib.obj',
    'swf_draw_renderstate.obj',
    'swf_draw_shape.obj',
    'swf_draw_text.obj',
    'swf_draw_texture.obj',
    'swf_draw_triangulate.obj',
    'swf_fontcache.obj',
    'swf_jpeg.obj',
    'swf_math.obj',
    'swf_play.obj',
    'swf_playhead.obj',
    'swf_polygonalize.obj',
    'swf_state.obj',
    'triangulate_ears.obj',
    'zlib.obj',
]

patched_object_files = []
foreach file : iggy_object_files
    patched_object_files += file.replace('.obj', '.o')
endforeach

unpacked_objects = custom_target(
    'unpack-archive',
    input: meson.project_source_root() / 'libs' / 'libiggy_orbis.a',
    output: iggy_object_files,
    command: [
        ar,
        'x',
        '@INPUT@'
    ],
)

patched_relocations = custom_target(
    'patch-relocations',
    input: unpacked_objects,
    output: patched_object_files,
    command: [
        python, meson.project_source_root() / 'scripts/patch_relocations.py',
        '@INPUT@',
    ],
)

shiggy_dep = declare_dependency(
    link_with: static_library(
        'shiggy',
        meson.project_source_root() / 'src' / 'shims.c',
        include_directories : include_directories('include'),
        objects: patched_relocations,
    )
)