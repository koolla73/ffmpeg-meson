#### --- GENERATED --- ####

libavutil_x86_sources = files(
  'cpu.c',
)

libavutil_x86_x86asm_sources = files(
  # 'aes.asm', # MANUAL
  # 'aes_init.c', # MANUAL
  'cpuid.asm',
  'crc.asm',
  'fixed_dsp.asm',
  'fixed_dsp_init.c',
  'float_dsp.asm',
  'float_dsp_init.c',
  'imgutils.asm',
  'imgutils_init.c',
  'lls.asm',
  'lls_init.c',
  'tx_float.asm',
  'tx_float_init.c',
)

libavutil_x86_x86asm_optional_sources = {
  'mmx_external' : files('emms.asm'), # MANUAL
  'pixelutils' : files('pixelutils.asm','pixelutils_init.c'),
}

#### --- END GENERATED --- ####

if conf.get('aesni_external', 0) == 1
  libavutil_x86_x86asm_sources += files(
    'aes_init.c',
    'aes.asm',
  )
endif
