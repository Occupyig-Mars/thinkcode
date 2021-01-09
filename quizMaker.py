import wikipedia
import spacy
import pytextrank
# YOU NEED TO run this in the command line: python3 -m spacy download en_core_web_sm

class Quiz:
    def __init__(self, topic):
        # The topic of the quiz
        self.topic = topic
        # Text
        self.text = self.gather_article()
        # Dictionary which stores all questions and respective answers
        self.questions = self.produce_questions(topic)


    def produce_questions(self, topic):
        questions = {}
        return questions

    def key_phrases(self, text):
        # example text
        text = text

        # load a spaCy model, depending on language, scale, etc.
        nlp = spacy.load("en_core_web_sm")

        # add PyTextRank to the spaCy pipeline
        tr = pytextrank.TextRank()
        nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

        doc = nlp(text)

        # examine the top-ranked phrases in the document
        #for p in doc._.phrases:
            #print("{:.4f} {:5d}  {}".format(p.rank, p.count, p.text))
            #print(p.chunks)

        print("STOPPED")

        for sent in doc._.textrank.summary(limit_phrases=1, limit_sentences=5):
            print("Sentence: ")
            print(sent)

    def key_word(self, phrase):
        pass

    def gather_article(self):
        raw_page = wikipedia.summary(self.topic)
        page = raw_page.partition("== See also ==")[0]
        print(page)
        return page

quiz = Quiz('Linked Lists')

quiz.key_phrases(quiz.text)