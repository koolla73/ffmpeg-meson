#### --- GENERATED --- ####

libavfilter_vulkan_optional_sources = {
  'bwdif_vulkan_filter' : files('bwdif.comp'),
  'scale_vulkan_filter' : files('debayer.comp'),
}

#### --- END GENERATED --- ####

foreach k, v: libavfilter_vulkan_optional_sources
  libavfilter_optional_sources += {
    k: libavfilter_optional_sources.get(k, []) + source2c.process(v)
  }
endforeach
