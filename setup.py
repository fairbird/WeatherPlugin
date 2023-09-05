# -*- coding: utf-8 -*-
from distutils.core import setup
import setup_translate

pkg = 'Extensions.WeatherPlugin'
setup(name='enigma2-plugin-extensions-weatherplugin',
       version='2.1',
       description='Weather plugin',
       packages=[pkg],
       package_dir={pkg: 'usr'},
       package_data={pkg: ['weather.png', '*/*.png', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass, # for translation
      )
