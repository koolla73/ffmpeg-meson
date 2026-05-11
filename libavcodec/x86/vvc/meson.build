#### --- GENERATED --- ####

libavcodec_x86_vvc_x86asm_optional_sources = {
  'vvc_decoder' : files('dsp_init.c'), # MANUAL
}

#### --- END GENERATED --- ####

if conf.get('x86_64', 0) == 1
  # Alternatively,
  # panic: ../libavcodec/x86/simple_idct10.asm: assertion cv8_state.source_files != NULL failed at output/codeview.c:512
  libavcodec_x86_vvc_x86asm_optional_sources += {
    'vvc_decoder': libavcodec_x86_vvc_x86asm_optional_sources ['vvc_decoder'] + files('alf.asm', 'dmvr.asm', 'of.asm', 'sad.asm'),
  }

  if conf.get('avx2_external', 0) == 1
    libavcodec_x86_vvc_x86asm_optional_sources += {
      'vvc_decoder': libavcodec_x86_vvc_x86asm_optional_sources ['vvc_decoder'] + files('mc.asm'),
    }
  endif
endif

if conf.get('avx2_external', 0) == 1
  libavcodec_x86_vvc_x86asm_optional_sources += {
    'vvc_decoder': libavcodec_x86_vvc_x86asm_optional_sources ['vvc_decoder'] + files('sao.asm','sao_10bit.asm'),
  }
endif
