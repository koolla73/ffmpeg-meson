#### --- GENERATED --- ####

fftools_resources_sources = files(
  'resman.c',
)

#### --- END GENERATED --- ####

fftools_resources_resman_sources = files(
  'graph.html',
  'graph.css',
)

if conf.get('resource_compression') == 1
  gzip_gen = generator(
    gzip_exe,
    arguments: ['-nc9', '@INPUT@'],
    output: '@PLAINNAME@.gz',
    capture: true,
  )
  gz_objs = gzip_gen.process(fftools_resources_resman_sources)
  gen_objects = bin2c.process(gz_objs)
else
  gen_objects = bin2c_with_extension.process(fftools_resources_resman_sources)
endif
fftools_resources_sources += gen_objects
