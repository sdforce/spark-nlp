from test.annotators import *
from test.misc import *

# Annotator tests
unittest.TextTestRunner().run(BasicAnnotatorsTestSpec())
unittest.TextTestRunner().run(RegexMatcherTestSpec())
unittest.TextTestRunner().run(TokenizerTestSpec())
unittest.TextTestRunner().run(ChunkTokenizerTestSpec())
unittest.TextTestRunner().run(LemmatizerTestSpec())
unittest.TextTestRunner().run(DateMatcherTestSpec())
unittest.TextTestRunner().run(TextMatcherTestSpec())

unittest.TextTestRunner().run(PerceptronApproachTestSpec())
unittest.TextTestRunner().run(ChunkerTestSpec())
unittest.TextTestRunner().run(ChunkDocSerializingTestSpec())

unittest.TextTestRunner().run(PragmaticSBDTestSpec())
unittest.TextTestRunner().run(PragmaticScorerTestSpec())
unittest.TextTestRunner().run(PipelineTestSpec())
unittest.TextTestRunner().run(SpellCheckerTestSpec())
unittest.TextTestRunner().run(SymmetricDeleteTestSpec())
# unittest.TextTestRunner().run(ContextSpellCheckerTestSpec())
unittest.TextTestRunner().run(ParamsGettersTestSpec())
unittest.TextTestRunner().run(DependencyParserTreeBankTestSpec())
unittest.TextTestRunner().run(DependencyParserConllUTestSpec())
unittest.TextTestRunner().run(TypedDependencyParserConll2009TestSpec())
unittest.TextTestRunner().run(TypedDependencyParserConllUTestSpec())
unittest.TextTestRunner().run(DeepSentenceDetectorTestSpec())
unittest.TextTestRunner().run(SentenceEmbeddingsTestSpec())
unittest.TextTestRunner().run(StopWordsCleanerTestSpec())
unittest.TextTestRunner().run(NGramGeneratorTestSpec())
unittest.TextTestRunner().run(ChunkEmbeddingsTestSpec())
unittest.TextTestRunner().run(EmbeddingsFinisherTestSpec())

# Misc tests
unittest.TextTestRunner().run(UtilitiesTestSpec())
unittest.TextTestRunner().run(SerializersTestSpec())

