# Native utterance generator

INSTALL
pip install <choose_your_python_version>.whl

EXAMPLE
import regextor
regextor.run('(take|drive) (me|) to (Seattle|Vancouver)')

['drive  to Vancouver', 'drive  to Seattle', 'drive me to Vancouver', 
 'drive me to Seattle', 'take  to Vancouver', 'take  to Seattle', 
 'take me to Vancouver', 'take me to Seattle']


