# Zocker-Assignment

# Web Content Extractor and Summarizer

This Python script retrieves the content from a specified URL, extracts the text from the paragraphs, and generates a concise summary of the content. It utilizes the BeautifulSoup library for web scraping and SpaCy for natural language processing.

## Features

- Fetches and displays the title of the webpage.
- Extracts and displays all paragraph text in a structured format.
- Generates a concise summary of the extracted content.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `spacy` library
- `en_core_web_sm` SpaCy model

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/web-content-extractor.git
   cd web-content-extractor ```

## Install the required libraries:
```
pip install requests beautifulsoup4 spacy
```

## Download the SpaCy model:
```
python -m spacy download en_core_web_sm
```

Run the script:
```
python AI.py
```

# Example 
Please enter the URL:  https://en.wikipedia.org/wiki/Natural_language_processing
--- Web Page Title ---
Natural language processing - Wikipedia

--- Extracted Content ---
Paragraph 1: Natural language processing (NLP) is a subfield of computer science and especially artificial intelligence. It is primarily concerned with providing computers with the ability to process data encoded in natural language and is thus closely related to information retrieval, knowledge representation and computational linguistics, a subfield of linguistics. Typically data is collected in text corpora, using either rule-based, statistical or neural-based approaches in machine learning and deep learning.


Paragraph 2: Major tasks in natural language processing are speech recognition, text classification, natural-language understanding, and natural-language generation.


Paragraph 3: Natural language processing has its roots in the 1950s.[1] Already in 1950, Alan Turing published an article titled "Computing Machinery and Intelligence" which proposed what is now called the Turing test as a criterion of intelligence, though at the time that was not articulated as a problem separate from artificial intelligence. The proposed test includes a task that involves the automated interpretation and generation of natural language.


Paragraph 4: The premise of symbolic NLP is well-summarized by John Searle's Chinese room experiment: Given a collection of rules (e.g., a Chinese phrasebook, with questions and matching answers), the computer emulates natural language understanding (or other NLP tasks) by applying those rules to the data it confronts.


Paragraph 5: Up until the 1980s, most natural language processing systems were based on complex sets of hand-written rules.  Starting in the late 1980s, however, there was a revolution in natural language processing with the introduction of machine learning algorithms for language processing.  This was due to both the steady increase in computational power (see Moore's law) and the gradual lessening of the dominance of Chomskyan theories of linguistics (e.g. transformational grammar), whose theoretical underpinnings discouraged the sort of corpus linguistics that underlies the machine-learning approach to language processing.[8]


Paragraph 6: In 2003, word n-gram model, at the time the best statistical algorithm, was outperformed by a multi-layer perceptron (with a single hidden layer and context length of several words trained on up to 14 million of words with a CPU cluster in language modelling) by Yoshua Bengio with co-authors.[9]


Paragraph 7: In 2010, Tomáš Mikolov (then a PhD student at Brno University of Technology) with co-authors applied a simple recurrent neural network with a single hidden layer to language modelling,[10] and in the following years he went on to develop Word2vec. In the 2010s, representation learning and deep neural network-style (featuring many hidden layers) machine learning methods became widespread in natural language processing. That popularity was due partly to a flurry of results showing that such techniques[11][12] can achieve state-of-the-art results in many natural language tasks, e.g., in language modeling[13] and parsing.[14][15] This is increasingly important in medicine and healthcare, where NLP helps analyze notes and text in electronic health records that would otherwise be inaccessible for study when seeking to improve care[16] or protect patient privacy.[17]


Paragraph 8: Symbolic approach, i.e., the hand-coding of a set of rules for manipulating symbols, coupled with a dictionary lookup, was historically the first approach used both by AI in general and by NLP in particular:[18][19] such as by writing grammars or devising heuristic rules for stemming.


Paragraph 9: Machine learning approaches, which include both statistical and neural networks, on the other hand, have many advantages over the symbolic approach: 


Paragraph 10: Although rule-based systems for manipulating symbols were still in use in 2020, they have become mostly obsolete with the advance of LLMs in 2023. 


Paragraph 11: Before that they were commonly used:


Paragraph 12: In the late 1980s and mid-1990s, the statistical approach ended a period of AI winter, which was caused by the inefficiencies of the rule-based approaches.[20][21]


Paragraph 13: The earliest decision trees, producing systems of hard if–then rules, were still very similar to the old rule-based approaches.
Only the introduction of hidden Markov models, applied to part-of-speech tagging, announced the end of the old rule-based approach.


Paragraph 14: A major drawback of statistical methods is that they require elaborate feature engineering. Since 2015,[22] the statistical approach has been replaced by the neural networks approach, using semantic networks[23] and word embeddings to capture semantic properties of words.  


Paragraph 15: Intermediate tasks (e.g., part-of-speech tagging and dependency parsing) are not needed anymore. 


Paragraph 16: Neural machine translation, based on then-newly invented sequence-to-sequence transformations, made obsolete the intermediate steps, such as word alignment, previously necessary for statistical machine translation.


Paragraph 17: The following is a list of some of the most commonly researched tasks in natural language processing. Some of these tasks have direct real-world applications, while others more commonly serve as subtasks that are used to aid in solving larger tasks.


Paragraph 18: Though natural language processing tasks are closely intertwined, they can be subdivided into categories for convenience. A coarse division is given below.


Paragraph 19: Based on long-standing trends in the field, it is possible to extrapolate future directions of NLP. As of 2020, three trends among the topics of the long-standing series of CoNLL Shared Tasks can be observed:[46]


Paragraph 20: Most higher-level NLP applications involve aspects that emulate intelligent behaviour and apparent comprehension of natural language. More broadly speaking, the technical operationalization of increasingly advanced aspects of cognitive behaviour represents one of the developmental trajectories of NLP (see trends among CoNLL shared tasks above).


Paragraph 21: Cognition refers to "the mental action or process of acquiring knowledge and understanding through thought, experience, and the senses."[47] Cognitive science is the interdisciplinary, scientific study of the mind and its processes.[48] Cognitive linguistics is an interdisciplinary branch of linguistics, combining knowledge and research from both psychology and linguistics.[49] Especially during the age of symbolic NLP, the area of computational linguistics maintained strong ties with cognitive studies.


Paragraph 22: As an example, George Lakoff offers a methodology to build natural language processing (NLP) algorithms through the perspective of cognitive science, along with the findings of cognitive linguistics,[50] with two defining aspects:


Paragraph 23: Ties with cognitive linguistics are part of the historical heritage of NLP, but they have been less frequently addressed since the statistical turn during the 1990s. Nevertheless, approaches to develop cognitive models towards technically operationalizable frameworks have been pursued in the context of various frameworks, e.g., of cognitive grammar,[53] functional grammar,[54] construction grammar,[55] computational psycholinguistics and cognitive neuroscience (e.g., ACT-R), however, with limited uptake in mainstream NLP (as measured by presence on major conferences[56] of the ACL). More recently, ideas of cognitive NLP have been revived as an approach to achieve explainability, e.g., under the notion of "cognitive AI".[57] Likewise, ideas of cognitive NLP are inherent to neural models multimodal NLP (although rarely made explicit)[58] and developments in artificial intelligence, specifically tools and technologies using large language model approaches[59] and new directions in artificial general intelligence based on the free energy principle[60] by British neuroscientist and theoretician at University College London Karl J. Friston.

--- Summary ---
Natural language processing (NLP) is a subfield of computer science and especially artificial intelligence. It is primarily concerned with providing computers with the ability to process data encoded in natural language and is thus closely related to information retrieval, knowledge representation and computational linguistics, a subfield of linguistics. Typically data is collected in text corpora, using either rule-based, statistical or neural-based approaches in machine learning and deep learning.
 .
