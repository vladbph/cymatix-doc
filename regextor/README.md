# NLP utterance generator

NLP tool to unwind word level regular expression-like strings:
 '(take|drive) (me|) to (Seattle|Vancouver)' => 
 
  'drive  to Vancouver', 'drive  to Seattle', 'drive me to Vancouver', 
  'drive me to Seattle', 'take  to Vancouver', 'take  to Seattle', 
  'take me to Vancouver', 'take me to Seattle'
  
 NOTE, expression '(me|)' => ['me', '']
 
 This is _the_ tool for semi-automated training set generation

# INSTALL

```
pip install <choose_your_python_version>.whl
```
# EXAMPLE

```
import regextor
regextor.run('(take|drive) (me|) to (Seattle|Vancouver)')

['drive  to Vancouver', 'drive  to Seattle', 'drive me to Vancouver', 
 'drive me to Seattle', 'take  to Vancouver', 'take  to Seattle', 
 'take me to Vancouver', 'take me to Seattle']
```

