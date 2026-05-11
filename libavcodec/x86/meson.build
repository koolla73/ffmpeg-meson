#### --- GENERATED --- ####

libavcodec_x86_sources = files(
  'constants.c',
)

libavcodec_x86_optional_sources = {
  'fdctdsp' : files('fdctdsp_init.c','fdct.c'),
  'llvidencdsp' : files('lossless_videoencdsp_init.c'),
  'lpc' : files('lpc_init.c'),
  'mlp_decoder' : files('mlpdsp_init.c'),
  'mpeg4_decoder' : files('mpeg4videodsp.c'),
  'mpegaudiodsp' : files('mpegaudiodsp.c'),
  'mpegvideo' : files('mpegvideo.c'),
  'mpegvideoenc' : files('mpegvideoenc.c'),
  'mpegvideoencdsp' : files('mpegvideoencdsp_init.c'),
  'snow_decoder' : files('snowdsp.c'),
  'snow_encoder' : files('snowdsp.c'),
  'truehd_decoder' : files('mlpdsp_init.c'),
  'xmm_clobber_test' : files('w64xmmtest.c'),
}

libavcodec_x86_x86asm_optional_sources = {
  'aac_decoder' : files('aacpsdsp_init.c','sbrdsp_init.c','aacpsdsp.asm','sbrdsp.asm'),
  'aac_encoder' : files('aacencdsp_init.c','aacencdsp.asm'),
  'ac3dsp' : files('ac3dsp_init.c','ac3dsp.asm','ac3dsp_downmix.asm'),
  'adpcm_g722_decoder' : files('g722dsp_init.c','g722dsp.asm'),
  'adpcm_g722_encoder' : files('g722dsp_init.c','g722dsp.asm'),
  'alac_decoder' : files('alacdsp_init.c','alacdsp.asm'),
  'apng_decoder' : files('pngdsp_init.c','pngdsp.asm'),
  'apv_decoder' : files('apv_dsp_init.c',), # MANUAL
  'audiodsp' : files('audiodsp_init.c','audiodsp.asm'),
  'blockdsp' : files('blockdsp_init.c','blockdsp.asm'),
  'bswapdsp' : files('bswapdsp_init.c','bswapdsp.asm'),
  'cavs_decoder' : files('cavsdsp.c','cavsidct.asm','cavs_qpel.asm'),
  'cfhd_decoder' : files('cfhddsp_init.c','cfhddsp.asm'),
  'cfhd_encoder' : files('cfhdencdsp_init.c',), # MANUAL
  'dca_decoder' : files('dcadsp_init.c','synth_filter_init.c','dcadsp.asm','synth_filter.asm'),
  'dirac_decoder' : files('diracdsp_init.c','dirac_dwt_init.c','diracdsp.asm','dirac_dwt.asm'),
  'dnxhd_encoder' : files('dnxhdenc_init.c','dnxhdenc.asm'),
  'exr_decoder' : files('exrdsp_init.c','exrdsp.asm'),
  'flac_decoder' : files('flacdsp_init.c','flacdsp.asm'),
  'flac_encoder' : files('flacencdsp_init.c','flac_dsp_gpl.asm'),
  'fmtconvert' : files('fmtconvert_init.c','fmtconvert.asm'),
  'h263dsp' : files('h263dsp_init.c','h263_loopfilter.asm'),
  'h264chroma' : files('h264chroma_init.c','h264_chromamc.asm','h264_chromamc_10bit.asm'),
  'h264dsp' : files('h264dsp_init.c','h264_deblock.asm','h264_deblock_10bit.asm','h264_idct.asm','h264_idct_10bit.asm','h264_weight.asm','h264_weight_10bit.asm'),
  'h264pred' : files('h264_intrapred_init.c','h264_intrapred.asm','h264_intrapred_10bit.asm'),
  'h264qpel' : files('h264_qpel.c','h264_qpel_8bit.asm','h264_qpel_10bit.asm','fpel.asm','qpel.asm'),
  'hpeldsp' : files('hpeldsp_init.c','fpel.asm','hpeldsp.asm'),
  'huffyuvdsp' : files('huffyuvdsp_init.c','huffyuvdsp.asm'),
  'huffyuvencdsp' : files('huffyuvencdsp_init.c','huffyuvencdsp.asm'),
  'idctdsp' : files('idctdsp_init.c','idctdsp.asm'), # MANUAL
  'jpeg2000_decoder' : files('jpeg2000dsp_init.c','jpeg2000dsp.asm'),
  'llauddsp' : files('lossless_audiodsp_init.c','lossless_audiodsp.asm'),
  'llviddsp' : files('lossless_videodsp_init.c','lossless_videodsp.asm'),
  'llvidencdsp' : files('lossless_videoencdsp.asm'),
  'lpc' : files('lpc.asm'),
  'lscr_decoder' : files('pngdsp_init.c','pngdsp.asm'),
  'me_cmp' : files('me_cmp_init.c','me_cmp.asm'),
  'mlp_decoder' : [], # MANUAL
  'mpeg4_decoder' : files('xvididct_init.c','xvididct.asm'),
  'mpegaudiodsp' : files('dct32.asm','imdct36.asm'),
  'mpegvideoencdsp' : files('mpegvideoencdsp.asm'),
  'opus_decoder' : files('opusdsp_init.c','opusdsp.asm'),
  'opus_encoder' : files('celt_pvq_init.c','celt_pvq_search.asm'),
  'pixblockdsp' : files('pixblockdsp_init.c','pixblockdsp.asm'),
  'png_decoder' : files('pngdsp_init.c','pngdsp.asm'),
  'prores_decoder' : files('proresdsp_init.c'), # MANUAL
  'prores_raw_decoder' : files('proresdsp_init.c'), # MANUAL
  'qpeldsp' : files('qpeldsp_init.c','qpeldsp.asm','fpel.asm','qpel.asm'),
  'rv34dsp' : files('rv34dsp_init.c','rv34dsp.asm'),
  'rv40_decoder' : files('rv40dsp_init.c','rv40dsp.asm'),
  'sbc_encoder' : files('sbcdsp_init.c','sbcdsp.asm'),
  'svq1_encoder' : files('svq1enc_init.c','svq1enc.asm'),
  'tak_decoder' : files('takdsp_init.c','takdsp.asm'),
  'truehd_decoder' : [], # MANUAL
  'tta_decoder' : files('ttadsp_init.c','ttadsp.asm'),
  'tta_encoder' : files('ttaencdsp_init.c','ttaencdsp.asm'),
  'utvideo_decoder' : files('utvideodsp_init.c','utvideodsp.asm'),
  'v210_decoder' : files('v210-init.c','v210.asm'),
  'v210_encoder' : files('v210enc_init.c','v210enc.asm'),
  'vc1dsp' : files('vc1dsp_init.c','vc1dsp_mmx.c','vc1dsp_loopfilter.asm','vc1dsp_mc.asm','fpel.asm'),
  'videodsp' : files('videodsp_init.c','videodsp.asm'),
  'vorbis_decoder' : files('vorbisdsp_init.c','vorbisdsp.asm'),
  'vp3dsp' : files('vp3dsp_init.c','vp3dsp.asm'),
  'vp6_decoder' : files('vp6dsp_init.c','vp6dsp.asm'),
  'vp8dsp' : files('vp8dsp_init.c','vp8dsp.asm','vp8dsp_loopfilter.asm'),
  'vp9_decoder' : files('vp9dsp_init.c','vp9dsp_init_10bpp.c','vp9dsp_init_12bpp.c','vp9dsp_init_16bpp.c','vp9intrapred.asm','vp9intrapred_16bpp.asm','vp9itxfm.asm','vp9itxfm_16bpp.asm','vp9lpf.asm','vp9lpf_16bpp.asm','vp9mc.asm','vp9mc_16bpp.asm'), # MANUAL
}

#### --- END GENERATED --- ####

subdir('hevc')
subdir('vvc')

libavcodec_x86_optional_sources += libavcodec_x86_hevc_optional_sources

libavcodec_x86_x86asm_optional_sources += libavcodec_x86_hevc_x86asm_optional_sources

libavcodec_x86_x86asm_optional_sources += libavcodec_x86_vvc_x86asm_optional_sources

# This file results in empty codegen and empty PDB generation otherwise.
# https://bugzilla.nasm.us/show_bug.cgi?id=3392738
# https://developercommunity.visualstudio.com/t/MSVC-Hangs-when-compiling-ffmpeg-When-l/10233953
if conf.get('x86_32', 0) == 1
  libavcodec_x86_x86asm_optional_sources += {
    'idctdsp': libavcodec_x86_x86asm_optional_sources ['idctdsp'] + files('simple_idct.asm')
  }
elif conf.get('x86_64', 0) == 1
  # Alternatively,
  # panic: ../libavcodec/x86/simple_idct10.asm: assertion cv8_state.source_files != NULL failed at output/codeview.c:512
  libavcodec_x86_x86asm_optional_sources += {
    'apv_decoder': libavcodec_x86_x86asm_optional_sources['apv_decoder'] + files('apv_dsp.asm'),
    'idctdsp': libavcodec_x86_x86asm_optional_sources ['idctdsp'] + files('simple_idct10.asm'),
    'cfhd_encoder': libavcodec_x86_x86asm_optional_sources ['cfhd_encoder'] + files('cfhdencdsp.asm'),
    'mlp_decoder': libavcodec_x86_x86asm_optional_sources ['mlp_decoder'] + files('mlpdsp.asm'),
    'prores_decoder': libavcodec_x86_x86asm_optional_sources ['prores_decoder'] + files('proresdsp.asm'),
    'prores_raw_decoder': libavcodec_x86_x86asm_optional_sources ['prores_raw_decoder'] + files('proresdsp.asm'),
    'truehd_decoder': libavcodec_x86_x86asm_optional_sources ['truehd_decoder'] + files('mlpdsp.asm'),
  }

  if conf.get('avx2_external', 0) == 1
    libavcodec_x86_x86asm_optional_sources += {
      'vp9_decoder': libavcodec_x86_x86asm_optional_sources ['vp9_decoder'] + files('vp9itxfm_avx2.asm',),
    }
  endif

  if conf.get('avx512icl_external', 0) == 1
    libavcodec_x86_x86asm_optional_sources += {
      'vp9_decoder': libavcodec_x86_x86asm_optional_sources ['vp9_decoder'] + files('vp9itxfm_avx512.asm', 'vp9itxfm_16bpp_avx512.asm',),
    }
  endif

  if conf.get('hevc_decoder') == 1
    libavcodec_x86_optional_sources += {
      'hevc_decoder': libavcodec_x86_optional_sources ['hevc_decoder'] + files('h26x/h2656dsp.c')
    }
    libavcodec_x86_x86asm_optional_sources += {
      'hevc_decoder': libavcodec_x86_x86asm_optional_sources ['hevc_decoder'] + files('h26x/h2656_inter.asm')
    }
  elif conf.get('vvc_decoder') == 1
    libavcodec_x86_optional_sources += {
      'vvc_decoder': libavcodec_x86_optional_sources ['vvc_decoder'] + files('h26x/h2656dsp.c')
    }
    libavcodec_x86_x86asm_optional_sources += {
      'vvc_decoder': libavcodec_x86_x86asm_optional_sources ['vvc_decoder'] + files('h26x/h2656_inter.asm')
    }
  endif
endif
