# text_summary.py

import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from heapq import nlargest

def summariser(text, ratio=0.3):
    if not text.strip():
        return "Input text is empty!", {}, 0, 0

    # Load spaCy model and preprocess
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Stopwords and punctuation
    stopwords = list(nlp.Defaults.stop_words)
    sentences = list(doc.sents)

    # TF-IDF vectorizer
    vectorizer = TfidfVectorizer(stop_words=stopwords)
    sentence_texts = [sent.text for sent in sentences]
    tfidf_matrix = vectorizer.fit_transform(sentence_texts)
    document_vector = tfidf_matrix.mean(axis=0).A1  # Convert to 1D array

    # Sentence scores
    sentence_scores = {}
    for i, sent in enumerate(sentences):
        score = 0

        # 1. TF-IDF Score
        sentence_vector = tfidf_matrix[i].toarray()  # Convert to array
        similarity = cosine_similarity(sentence_vector, document_vector.reshape(1, -1))
        score += similarity[0, 0]

        # 2. Named Entity Recognition (NER)
        for ent in sent.ents:
            if ent.label_ in {"PERSON", "ORG", "GPE", "DATE"}:
                score += 0.5

        # 3. Position Weight
        score += 0.1 * (1 / (i + 1))

        # Normalize by sentence length
        score /= (len(sent.text.split()) + 1e-3)

        sentence_scores[sent] = score

    # Select top sentences
    select_len = int(len(sentences) * ratio)
    selected_sentences = nlargest(select_len, sentence_scores, key=sentence_scores.get)

    # Prepare summary
    summary = " ".join([sent.text for sent in sorted(selected_sentences, key=lambda s: sentences.index(s))])

    # Return results
    return (
        summary,
        {sent.text: round(score, 4) for sent, score in sentence_scores.items()},
        len(text.split()),
        len(summary.split()),
    )



text =""" Python was conceived in the late 1980s[42] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,[43] capable of exception handling and interfacing with the Amoeba operating system.[12] Its implementation began in December 1989.[44] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's "benevolent dictator for life" (BDFL), a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker[45] (he has since come out of retirement and is self-titled "BDFL-emeritus"). In January 2019, active Python core developers elected a five-member Steering Council to lead the project.[46][47]

The name Python is said to come from the British comedy series Monty Python's Flying Circus.[48]

Python 2.0 was released on 16 October 2000, with many major new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support.[49] Python 2.7's end-of-life was initially set for 2015, then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3.[50][51] No further security patches or other improvements will be released for it.[52][53] While Python 2.7 and older versions are officially unsupported, a different unofficial Python implementation, PyPy, continues to support Python 2, i.e. "2.7.18+" (plus 3.10), with the plus meaning (at least some) "backported security updates".[54]

Python 3.0 was released on 3 December 2008, with some new semantics and changed syntax. At least every Python release since (now unsupported) 3.5 has added some syntax to the language, and a few later releases have dropped outdated modules, or changed semantics, at least in a minor way.

Since 7 October 2024, Python 3.13 is the latest stable release, and it and, for few more months, 3.12 are the only releases with active support including for bug fixes (as opposed to just for security) and Python 3.9,[55] is the oldest supported version of Python (albeit in the 'security support' phase), due to Python 3.8 reaching end-of-life.[56][57] Starting with 3.13, it and later versions have 2 years of full support (up from one and a half), followed by 3 years of security support (for same total support as before).

Security updates were expedited in 2021 (and again twice in 2022, and more fixed in 2023 and in September 2024 for Python 3.12.6 down to 3.8.20), since all Python versions were insecure (including 2.7[58]) because of security issues leading to possible remote code execution[59] and web-cache poisoning.[60]

Python 3.10 added the | union type operator[61] and the match and case keywords (for structural pattern matching statements). 3.11 expanded exception handling functionality. Python 3.12 added the new keyword type. Notable changes in 3.11 from 3.10 include increased program execution speed and improved error reporting.[62] Python 3.11 claims to be between 10 and 60% faster than Python 3.10, and Python 3.12 adds another 5% on top of that. It also has improved error messages (again improved in 3.14), and many other changes.

Python 3.13 introduces more syntax for types, a new and improved interactive interpreter (REPL), featuring multi-line editing and color support; an incremental garbage collector (producing shorter pauses for collection in programs with a lot of objects, and addition to the improved speed in 3.11 and 3.12), and an experimental just-in-time (JIT) compiler (such features, can/needs to be enabled specifically for the increase in speed),[63] and an experimental free-threaded build mode, which disables the global interpreter lock (GIL), allowing threads to run more concurrently, that latter feature enabled with python3.13t or python3.13t.exe."""
summary, doc, original_len, summary_len = summariser(text)

print("Original Length:", original_len)
print("Summary Length:", summary_len)
print("Summary:")
print(summary)