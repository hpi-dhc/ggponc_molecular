import spacy

@spacy.registry.callbacks("set_custom_tokenizer")
def set_custom_tokenizer():
    def set_infixes(nlp):
        infixes = nlp.Defaults.infixes + [r'([-])']
        nlp.tokenizer.infix_finditer = spacy.util.compile_infix_regex(infixes).finditer
    return set_infixes