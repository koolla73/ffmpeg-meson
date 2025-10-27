#### --- GENERATED --- ####

fftools_sources = files(
  'textformat/avtextformat.c',
  'textformat/tf_compact.c',
  'textformat/tf_default.c',
  'textformat/tf_flat.c',
  'textformat/tf_ini.c',
  'textformat/tf_json.c',
  'textformat/tf_mermaid.c',
  'textformat/tf_xml.c',
  'textformat/tw_avio.c',
  'textformat/tw_buffer.c',
  'textformat/tw_stdout.c',
  'cmdutils.c',
  'opt_common.c',
)

fftools_optional_sources = {
  'ffmpeg' : files('ffmpeg_dec.c','ffmpeg_demux.c','ffmpeg_enc.c','ffmpeg_filter.c','ffmpeg_hw.c','ffmpeg_mux.c','ffmpeg_mux_init.c','ffmpeg_opt.c','ffmpeg_sched.c','graph/graphprint.c','sync_queue.c','thread_queue.c','textformat/avtextformat.c','textformat/tf_compact.c','textformat/tf_default.c','textformat/tf_flat.c','textformat/tf_ini.c','textformat/tf_json.c','textformat/tf_mermaid.c','textformat/tf_xml.c','textformat/tw_avio.c','textformat/tw_buffer.c','textformat/tw_stdout.c'),
  'ffplay' : files('ffplay_renderer.c'),
}

#### --- END GENERATED --- ####

subdir('resources')

ffmpeg_sources = fftools_resources_sources + files(
  'ffmpeg.c',
)

ffplay_sources = fftools_resources_sources + files(
  'ffplay.c',
)

ffprobe_sources = files(
  'ffprobe.c'
)

if host_machine.system() == 'windows'
  fftoolsres = windows.compile_resources(files('fftoolsres.rc'),
    depend_files: files('fftools.manifest'),
    include_directories: include_directories('.')
  )

  fftools_sources += fftoolsres
endif
