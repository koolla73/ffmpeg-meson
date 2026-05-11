#### --- GENERATED --- ####

libavfilter_x86_optional_sources = {
  'noise_filter' : files('vf_noise.c'),
  'spp_filter' : files('vf_spp.c'),
}

libavfilter_x86_x86asm_optional_sources = {
  'afir_filter' : files('af_afir.asm','af_afir_init.c'),
  'anlmdn_filter' : files('af_anlmdn.asm','af_anlmdn_init.c'),
  'atadenoise_filter' : files('vf_atadenoise_init.c'), # MANUAL
  'blackdetect_filter' : files('vf_blackdetect_init.c'), # MANUAL
  'blend_filter' : files('vf_blend.asm','vf_blend_init.c'),
  'bwdif_filter' : files('vf_bwdif.asm','vf_bwdif_init.c'),
  'colordetect_filter' : files('vf_colordetect.asm','vf_colordetect_init.c'),
  'colorspace_filter' : files('colorspacedsp.asm','colorspacedsp_init.c'),
  'convolution_filter' : files('vf_convolution.asm','vf_convolution_init.c'),
  'ebur128_filter' : files('f_ebur128_init.c'), # MANUAL
  'eq_filter' : files('vf_eq.asm','vf_eq_init.c'),
  'framerate_filter' : files('vf_framerate.asm','vf_framerate_init.c'),
  'fspp_filter' : files('vf_fspp.asm','vf_fspp_init.c'),
  'gblur_filter' : files('vf_gblur.asm','vf_gblur_init.c'),
  'gradfun_filter' : files('vf_gradfun.asm','vf_gradfun_init.c'),
  'haldclut_filter' : files('vf_lut3d_init.c'),
  'hflip_filter' : files('vf_hflip.asm','vf_hflip_init.c'),
  'hqdn3d_filter' : files('vf_hqdn3d.asm','vf_hqdn3d_init.c'),
  'idet_filter' : files('vf_idetdsp.asm','vf_idetdsp_init.c'),
  'interlace_filter' : files('vf_interlace.asm','vf_tinterlace_init.c'),
  'limiter_filter' : files('vf_limiter.asm','vf_limiter_init.c'),
  'lut3d_filter' : files('vf_lut3d.asm','vf_lut3d_init.c'),
  'maskedclamp_filter' : files('vf_maskedclamp.asm','vf_maskedclamp_init.c'),
  'maskedmerge_filter' : files('vf_maskedmerge.asm','vf_maskedmerge_init.c'),
  'nlmeans_filter' : files('vf_nlmeans_init.c'),
  'overlay_filter' : files('vf_overlay.asm','vf_overlay_init.c'),
  'pp7_filter' : files('vf_pp7.asm','vf_pp7_init.c'),
  'psnr_filter' : files('vf_psnr.asm','vf_psnr_init.c'),
  'pullup_filter' : files('vf_pullup.asm','vf_pullup_init.c'),
  'removegrain_filter' : files('vf_removegrain.asm','vf_removegrain_init.c'),
  'scene_sad' : files('scene_sad.asm','scene_sad_init.c'),
  'showcqt_filter' : files('avf_showcqt.asm','avf_showcqt_init.c'),
  'sobel_filter' : files('vf_convolution.asm','vf_convolution_init.c'),
  'ssim_filter' : files('vf_ssim.asm','vf_ssim_init.c'),
  'stereo3d_filter' : files('vf_stereo3d.asm','vf_stereo3d_init.c'),
  'tblend_filter' : files('vf_blend.asm','vf_blend_init.c'),
  'threshold_filter' : files('vf_threshold.asm','vf_threshold_init.c'),
  'tinterlace_filter' : files('vf_interlace.asm','vf_tinterlace_init.c'),
  'transpose_filter' : files('vf_transpose.asm','vf_transpose_init.c'),
  'v360_filter' : files('vf_v360_init.c'),
  'volume_filter' : files('af_volume.asm','af_volume_init.c'),
  'w3fdif_filter' : files('vf_w3fdif.asm','vf_w3fdif_init.c'),
  'xpsnr_filter' : files('vf_psnr.asm','vf_psnr_init.c'),
  'yadif_filter' : files('vf_yadif.asm','yadif-16.asm','yadif-10.asm','vf_yadif_init.c'),
}

#### --- END GENERATED --- ####

# This file results in empty codegen and empty PDB generation otherwise.
# https://bugzilla.nasm.us/show_bug.cgi?id=3392738
# https://developercommunity.visualstudio.com/t/MSVC-Hangs-when-compiling-ffmpeg-When-l/10233953
if conf.get('x86_64', 0) == 1
  # Alternatively,
  # panic: ../libavcodec/x86/simple_idct10.asm: assertion cv8_state.source_files != NULL failed at output/codeview.c:512
  conditionally_empty_asms = {
    'atadenoise_filter' : files('vf_atadenoise.asm'),
    'ebur128_filter': files('f_ebur128.asm'),
    'haldclut_filter': files('vf_lut3d.asm'),
  }

  foreach k, v : conditionally_empty_asms
    libavfilter_x86_x86asm_optional_sources += {
      k: libavfilter_x86_x86asm_optional_sources[k] + v
    }
  endforeach

  if conf.get('avx2_external', 0) == 1
    conditionally_empty_asms = {
      'nlmeans_filter': files('vf_nlmeans.asm'),
    }

    foreach k, v : conditionally_empty_asms
      libavfilter_x86_x86asm_optional_sources += {
        k: libavfilter_x86_x86asm_optional_sources[k] + v
      }
    endforeach
  endif
endif

if conf.get('avx2_external', 0) == 1
  # Alternatively,
  # panic: ../libavcodec/x86/simple_idct10.asm: assertion cv8_state.source_files != NULL failed at output/codeview.c:512
  conditionally_empty_asms = {
    'blackdetect_filter': files('vf_blackdetect.asm'),
    'v360_filter' : files('vf_v360.asm'),
  }

  foreach k, v : conditionally_empty_asms
    libavfilter_x86_x86asm_optional_sources += {
      k: libavfilter_x86_x86asm_optional_sources[k] + v
    }
  endforeach
endif

if conf.get('avx2_external', 0) == 1 or conf.get('avx512icl_external', 0) == 1
  # Alternatively,
  # panic: ../libavcodec/x86/simple_idct10.asm: assertion cv8_state.source_files != NULL failed at output/codeview.c:512
  conditionally_empty_asms = {
    'colordetect_filter': files('vf_colordetect.asm'),
  }

  foreach k, v : conditionally_empty_asms
    libavfilter_x86_x86asm_optional_sources += {
      k: libavfilter_x86_x86asm_optional_sources[k] + v
    }
  endforeach
endif

