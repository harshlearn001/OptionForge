from pytest import raises

from optionforge.knowledge.rules.knowledge_rule import KnowledgeRule


def test_rule_is_abstract():

    with raises(TypeError):

        KnowledgeRule()