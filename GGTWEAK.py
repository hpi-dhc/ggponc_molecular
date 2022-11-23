# Imports

import spacy, re
from spacy.tokens import Span, DocBin
from spacy_transformers import Transformer
from spacy_transformers.pipeline_component import DEFAULT_CONFIG
from skweak import heuristics, gazetteers, generative, utils, base
from skweak.base import SpanAnnotator
from skweak.heuristics import SpanEditorAnnotator, VicinityAnnotator, SpanConstraintAnnotator
from skweak.analysis import LFAnalysis
import pandas as pd
import numpy as np
import ipynb
import string
import sklearn.metrics
from thefuzz import fuzz
from thefuzz import process


from ipynb.fs.full.my_functions import evaluate, get_results, compute_raw_numbers, _get_probs, show_errors


nlp.tokenizer.infix_finditer = spacy.util.compile_infix_regex(infixes).finditer
nlp.add_pipe('sentencizer')
doc_bin = DocBin()
spacy.require_gpu()
nlp = spacy.load('de_core_news_md')
infixes = nlp.Defaults.infixes + [r'([-])']
