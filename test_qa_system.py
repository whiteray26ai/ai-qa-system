import sys
sys.path.insert(0, '.')

from ai_qa_system import extract_keywords, match_question, knowledge_base

def test_extract_keywords():
    print("测试关键词提取功能...")
    
    test_cases = [
        ("什么是人工智能？", {"人工智能", "AI", "定义"}),
        ("Python在AI中的作用", {"Python", "编程语言", "AI", "作用"}),
        ("机器学习和深度学习有什么区别", {"机器学习", "深度学习", "区别"}),
        ("什么是自然语言处理", {"自然语言处理", "NLP", "定义"}),
    ]
    
    passed = 0
    for text, expected in test_cases:
        result = extract_keywords(text)
        if result & expected:
            print(f"  ✓ '{text}' -> {result}")
            passed += 1
        else:
            print(f"  ✗ '{text}' -> {result} (期望包含: {expected})")
    
    print(f"关键词提取测试: {passed}/{len(test_cases)} 通过\n")
    return passed == len(test_cases)

def test_match_question():
    print("测试问题匹配功能...")
    
    test_cases = [
        ("人工智能是什么", "什么是人工智能？"),
        ("Python在人工智能中的作用", "Python在人工智能中的作用？"),
        ("机器学习和深度学习有什么不同", "机器学习和深度学习的区别？"),
        ("深度学习的定义", "深度学习是什么？"),
        ("什么是监督学习", "监督学习和无监督学习的区别？"),
        ("TensorFlow框架", "什么是TensorFlow？"),
        ("过拟合是什么", "什么是过拟合？"),
    ]
    
    passed = 0
    for user_input, expected in test_cases:
        result = match_question(user_input)
        if result == expected:
            print(f"  ✓ '{user_input}' -> '{result}'")
            passed += 1
        else:
            print(f"  ✗ '{user_input}' -> '{result}' (期望: '{expected}')")
    
    print(f"问题匹配测试: {passed}/{len(test_cases)} 通过\n")
    return passed == len(test_cases)

def test_knowledge_base():
    print("测试知识库完整性...")
    
    print(f"  ✓ 知识库包含 {len(knowledge_base)} 个问题")
    
    required_questions = [
        "什么是人工智能？",
        "Python在人工智能中的作用？",
        "机器学习和深度学习的区别？",
    ]
    
    all_found = True
    for q in required_questions:
        if q in knowledge_base:
            print(f"  ✓ 包含问题: '{q}'")
        else:
            print(f"  ✗ 缺少问题: '{q}'")
            all_found = False
    
    print("知识库测试完成\n")
    return all_found

def main():
    print("=" * 60)
    print("      AI问答系统单元测试")
    print("=" * 60 + "\n")
    
    results = []
    results.append(test_extract_keywords())
    results.append(test_match_question())
    results.append(test_knowledge_base())
    
    if all(results):
        print("=" * 60)
        print("  所有测试通过！✓")
        print("=" * 60)
        return 0
    else:
        print("=" * 60)
        print("  部分测试失败！✗")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())