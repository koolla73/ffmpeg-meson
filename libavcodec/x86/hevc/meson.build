#### --- GENERATED --- ####

libavcodec_x86_hevc_optional_sources = {
  'hevc_decoder' : files('dsp_init.c'), # MANUAL
}

libavcodec_x86_hevc_x86asm_optional_sources = {
  'hevc_decoder' : files('dsp_init.c','add_res.asm','deblock.asm','dequant.asm','idct.asm','sao.asm','sao_10bit.asm'), # MANUAL
}

#### --- END GENERATED --- ####

if conf.get('x86_64', 0) == 1
  # Alternatively,
  # panic: ../libavcodec/x86/simple_idct10.asm: assertion cv8_state.source_files != NULL failed at output/codeview.c:512
  if conf.get('avx2_external', 0) == 1
    libavcodec_x86_hevc_x86asm_optional_sources += {
      'hevc_decoder': libavcodec_x86_hevc_x86asm_optional_sources ['hevc_decoder'] + files('mc.asm'),
    }
  endif
endif
