#### --- GENERATED --- ####

libavcodec_vulkan_optional_sources = {
  'ffv1_vulkan_encoder' : files('common.comp','rangecoder.comp','ffv1_vlc.comp','ffv1_common.comp','ffv1_reset.comp','ffv1_enc_rct.comp','ffv1_enc_setup.comp','ffv1_rct_search.comp','ffv1_enc.comp'),
  'ffv1_vulkan_hwaccel' : files('common.comp','rangecoder.comp','ffv1_vlc.comp','ffv1_common.comp','ffv1_reset.comp','ffv1_dec_setup.comp','ffv1_dec.comp'),
  'prores_raw_vulkan_hwaccel' : files('common.comp','prores_raw.comp'),
}

#### --- END GENERATED --- ####

foreach k, v: libavcodec_vulkan_optional_sources
  libavcodec_optional_sources += {
    k: libavcodec_optional_sources.get(k, []) + source2c.process(v)
  }
endforeach
