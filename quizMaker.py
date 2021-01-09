import wikipedia
import spacy
import pytextrank
from rake_nltk import Rake

# run in command line to install the following necessary package: python3 -m spacy download en_core_web_sm

class Quiz:
    def __init__(self, topic):
        # The topic of the quiz
        self.topic = topic
        # Text
        self.text = self.gather_article()
        # Dictionary which stores all questions and respective answers
        self.questions = self.produce_questions()


    def produce_questions(self):
        sentences = self.key_phrases()
        questions = {}

        for i in range(len(sentences)):
            keyword = self.key_word(sentences[i]).strip(".").strip(")").strip(" ")
            complete_sentence = sentences[i]
            question = sentences[i].replace(keyword, "BLANK")

            questions[i] = {
                'completeSentence': complete_sentence,
                'question' : question,
                'answer' : keyword
            }

        return questions

    def key_phrases(self):
        # example text
        text = self.text

        # load a spaCy model, depending on language, scale, etc.
        nlp = spacy.load("en_core_web_sm")

        # add PyTextRank to the spaCy pipeline
        tr = pytextrank.TextRank()
        nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

        doc = nlp(text)

        # to examine the top-ranked phrases in the document:
        #for p in doc._.phrases:
            #print("{:.4f} {:5d}  {}".format(p.rank, p.count, p.text))
            #print(p.chunks)

        sentences = []

        for sentence in doc._.textrank.summary(limit_phrases=1, limit_sentences=5):
            sentences.append(str(sentence).replace("\n", ""))

        return sentences

    def key_word(self, sentence):
        r = Rake()
        r.extract_keywords_from_text(sentence)
        ranked_phrases = [x for x in r.get_ranked_phrases() if x.count(" ") < 2]  # Keyword phrases ranked highest to lowest.
        return ranked_phrases[0]

    def gather_article(self):
        # returns a summary on the topic from wikipedia
        return wikipedia.summary(self.topic)

"""
Example:
quiz = Quiz('Linked Lists')

final_quiz = quiz.produce_questions()

for i in final_quiz.values():
    print("Fill in the blank: ")
    print(i['question'])
    print("Answer: ")
    print(i['answer'])
"""