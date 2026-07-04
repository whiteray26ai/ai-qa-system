import tkinter as tk
from tkinter import scrolledtext, messagebox

# ============================================
# 模块1：知识库管理模块
# 功能：存储、预处理和索引预设的问答对
# ============================================

# 问答对字典：以问题为键，答案为值
knowledge_base = {
    "什么是人工智能？": "人工智能（Artificial Intelligence，简称AI）是计算机科学的一个分支，致力于研究、开发用于模拟、延伸和扩展人的智能的理论、方法、技术及应用系统。它涉及机器学习、自然语言处理、计算机视觉等多个领域。",
    "Python在人工智能中的作用？": "Python是人工智能领域最常用的编程语言，拥有丰富的库和框架如TensorFlow、PyTorch、Scikit-learn等，语法简洁易读，适合快速原型开发和数据处理，是AI开发者的首选语言。",
    "机器学习和深度学习的区别？": "机器学习是人工智能的子集，通过算法让计算机从数据中学习模式；深度学习是机器学习的子集，使用多层神经网络模拟人脑处理信息，能自动学习特征，在图像识别、语音识别等领域表现优异。",
    "什么是机器学习？": "机器学习是人工智能的核心技术之一，它使计算机系统能够从数据中学习并改进性能，而无需进行明确编程。主要包括监督学习、无监督学习和强化学习三种类型。",
    "深度学习是什么？": "深度学习是一种特殊的机器学习方法，使用多层人工神经网络来模拟人脑的学习过程。它能够自动从原始数据中学习特征表示，在复杂任务如图像识别、自然语言处理等方面取得突破性成果。",
    "什么是神经网络？": "神经网络是模仿人脑神经元结构和功能的计算模型，由大量相互连接的节点（神经元）组成。每个神经元接收输入，进行计算后输出到下一层，通过训练调整权重来学习数据模式。",
    "监督学习和无监督学习的区别？": "监督学习使用标注数据进行训练，输入数据带有明确的标签；无监督学习使用未标注数据，算法自动发现数据中的模式和结构，如聚类分析。",
    "什么是自然语言处理？": "自然语言处理（NLP）是人工智能的一个分支，研究如何让计算机理解、处理和生成人类语言。应用包括机器翻译、情感分析、聊天机器人等。",
    "计算机视觉是什么？": "计算机视觉是人工智能领域，研究如何使计算机能够'看'和理解图像及视频。应用包括图像识别、目标检测、人脸识别、自动驾驶等。",
    "什么是强化学习？": "强化学习是机器学习的一种范式，智能体通过与环境交互获得奖励信号来学习最优行为策略。常用于游戏AI、机器人控制、资源管理等领域。",
    "什么是TensorFlow？": "TensorFlow是Google开发的开源机器学习框架，用于构建和训练各种机器学习和深度学习模型。支持分布式训练，可部署在多种平台上。",
    "PyTorch是什么？": "PyTorch是Facebook开发的开源深度学习框架，以动态计算图和Pythonic风格著称，易于调试和灵活使用，是学术界和工业界广泛使用的框架。",
    "什么是数据挖掘？": "数据挖掘是从大量数据中发现模式、规律和知识的过程。它结合统计学、机器学习、数据库技术等，用于商业智能、预测分析等领域。",
    "人工智能的应用领域有哪些？": "人工智能广泛应用于医疗健康、金融科技、自动驾驶、智能家居、智能制造、教育、娱乐等众多领域，正在深刻改变人们的生活和工作方式。",
    "什么是算法？": "算法是解决特定问题的一系列明确步骤和规则。在人工智能中，算法是核心，如决策树、随机森林、神经网络等，用于数据处理和模型训练。",
    "什么是模型训练？": "模型训练是指使用数据调整机器学习模型参数的过程。通过迭代优化，使模型能够准确预测或分类新数据。训练过程包括前向传播、计算损失、反向传播和参数更新。",
    "什么是过拟合？": "过拟合是指模型在训练数据上表现很好，但在测试数据或新数据上表现较差的现象。原因是模型过于复杂，学习了训练数据中的噪声和细节。",
    "什么是欠拟合？": "欠拟合是指模型在训练数据和测试数据上都表现较差的现象。原因是模型过于简单，无法捕捉数据中的复杂模式和关系。",
    "什么是特征工程？": "特征工程是指从原始数据中提取、选择和转换有意义特征的过程。好的特征能显著提高模型性能，是机器学习项目成功的关键步骤之一。",
    "人工智能的发展历程？": "人工智能发展经历了多个阶段：1956年达特茅斯会议诞生，符号主义时期，机器学习兴起，深度学习革命（2012年AlexNet），以及当前大语言模型时代，技术不断突破创新。"
}

# 问题关键词映射：每个问题对应的核心关键词集合
question_keywords_map = {
    "什么是人工智能？": {"人工智能", "AI", "定义"},
    "Python在人工智能中的作用？": {"Python", "编程语言", "AI", "作用"},
    "机器学习和深度学习的区别？": {"机器学习", "深度学习", "区别"},
    "什么是机器学习？": {"机器学习", "定义"},
    "深度学习是什么？": {"深度学习", "定义"},
    "什么是神经网络？": {"神经网络", "定义"},
    "监督学习和无监督学习的区别？": {"监督学习", "无监督学习", "区别"},
    "什么是自然语言处理？": {"自然语言处理", "NLP", "定义"},
    "计算机视觉是什么？": {"计算机视觉", "定义"},
    "什么是强化学习？": {"强化学习", "定义"},
    "什么是TensorFlow？": {"TensorFlow", "框架"},
    "PyTorch是什么？": {"PyTorch", "框架"},
    "什么是数据挖掘？": {"数据挖掘", "定义"},
    "人工智能的应用领域有哪些？": {"人工智能", "应用", "领域"},
    "什么是算法？": {"算法", "定义"},
    "什么是模型训练？": {"模型训练", "定义"},
    "什么是过拟合？": {"过拟合", "定义"},
    "什么是欠拟合？": {"欠拟合", "定义"},
    "什么是特征工程？": {"特征工程", "定义"},
    "人工智能的发展历程？": {"人工智能", "发展", "历程"}
}

# 全局关键词集合：所有问题关键词的去重并集
global_keywords_set = set()
for keywords in question_keywords_map.values():
    global_keywords_set.update(keywords)

# 倒排索引：关键词到问题的映射，用于快速筛选候选问题
keyword_index = {}
for question, keywords in question_keywords_map.items():
    for kw in keywords:
        if kw not in keyword_index:
            keyword_index[kw] = []
        if question not in keyword_index[kw]:
            keyword_index[kw].append(question)

# ============================================
# 模块2：问答匹配引擎模块
# 功能：将用户问题映射到知识库中的问题，返回答案
# ============================================

def extract_keywords(text):
    """
    从用户输入文本中提取关键词集合
    参数：text - 用户输入的原始文本
    返回：提取到的关键词集合
    """
    keywords = set()
    # 将文本转换为小写，便于匹配
    text_lower = text.lower()
    
    # 遍历全局关键词集合，检查是否出现在用户输入中
    for keyword in global_keywords_set:
        if keyword.lower() in text_lower:
            keywords.add(keyword)
    
    # 如果没有匹配到预设关键词，尝试提取2个及以上字符的连续中文或英文
    if not keywords:
        import re
        pattern = r'[\u4e00-\u9fa5]{2,}|[a-zA-Z]{2,}'
        matches = re.findall(pattern, text)
        for match in matches:
            keywords.add(match)
    
    return keywords

def match_answer(user_input):
    """
    根据用户输入匹配知识库中的问题，返回最佳答案
    参数：user_input - 用户输入的问题
    返回：匹配到的答案，或未找到提示
    """
    # 步骤1：提取用户问题中的关键词集合
    user_kw_set = extract_keywords(user_input)
    
    # 如果未提取到关键词，直接返回未找到提示
    if not user_kw_set:
        return "抱歉，未找到相关答案，请尝试其他问题。", None, None
    
    # 步骤2：利用倒排索引快速筛选候选问题
    candidate_questions = set()
    for kw in user_kw_set:
        if kw in keyword_index:
            candidate_questions.update(keyword_index[kw])
    
    # 如果候选问题集合为空，返回未找到提示
    if not candidate_questions:
        return "抱歉，未找到相关答案，请尝试其他问题。", None, None
    
    # 步骤3：计算匹配度，选择最优答案
    best_score = -1
    best_question = None
    for q in candidate_questions:
        q_kw_set = question_keywords_map[q]
        # 匹配度 = 用户关键词集合与问题关键词集合的交集元素个数
        score = len(user_kw_set & q_kw_set)
        if score > best_score:
            best_score = score
            best_question = q
    
    # 如果最高匹配度为0，返回未找到提示
    if best_score <= 0:
        return "抱歉，未找到相关答案，请尝试其他问题。", None, None
    
    # 返回匹配结果
    matched_keywords = user_kw_set & question_keywords_map[best_question]
    return knowledge_base[best_question], best_question, matched_keywords

# ============================================
# 模块3：用户交互界面模块（基于tkinter）
# 功能：提供可视化交互界面，支持用户提问和答案展示
# ============================================

class AIQASystemGUI:
    """AI基础问答系统图形界面类"""
    
    def __init__(self, root):
        """初始化界面"""
        self.root = root
        self.root.title("AI基础问答系统")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # 用户提问历史记录列表
        self.user_history = []
        
        # 创建界面组件
        self.create_widgets()
    
    def create_widgets(self):
        """创建界面组件"""
        # 顶部标题标签
        self.title_label = tk.Label(
            self.root, 
            text="欢迎使用人工智能基础问答系统",
            font=("微软雅黑", 14, "bold"),
            bg="#4a90d9",
            fg="white",
            padx=10,
            pady=10
        )
        self.title_label.pack(fill=tk.X)
        
        # 顶部输入区域框架 - 添加亮显背景色（移到标题下方）
        self.input_frame = tk.Frame(self.root, bg="#e8f4fd", padx=8, pady=8)
        self.input_frame.pack(fill=tk.X, padx=10, pady=(10, 5))
        
        # 输入框 - 添加高亮边框和背景色
        self.input_entry = tk.Entry(
            self.input_frame,
            font=("微软雅黑", 11),
            width=40,
            bg="white",
            fg="#333333",
            relief=tk.GROOVE,
            bd=2,
            highlightthickness=2,
            highlightcolor="#4a90d9",
            highlightbackground="#b3d9f5",
            insertbackground="#4a90d9"
        )
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.input_entry.bind("<Return>", self.handle_send)  # 绑定回车键
        
        # 发送按钮
        self.send_btn = tk.Button(
            self.input_frame,
            text="发送",
            font=("微软雅黑", 11),
            bg="#4a90d9",
            fg="white",
            command=self.handle_send,
            padx=15
        )
        self.send_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        # 清空按钮
        self.clear_btn = tk.Button(
            self.input_frame,
            text="清空",
            font=("微软雅黑", 11),
            bg="#999999",
            fg="white",
            command=self.clear_history,
            padx=15
        )
        self.clear_btn.pack(side=tk.LEFT)
        
        # 对话历史显示区域（移到输入区域下方）
        self.history_text = scrolledtext.ScrolledText(
            self.root,
            font=("微软雅黑", 11),
            wrap=tk.WORD,
            state=tk.DISABLED,
            bg="#f5f5f5",
            padx=10,
            pady=10
        )
        self.history_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(5, 10))
        
        # 底部状态栏
        self.status_bar = tk.Label(
            self.root,
            text="就绪 - 请输入问题，输入'退出'结束对话",
            font=("微软雅黑", 10),
            bg="#e0e0e0",
            fg="#666666",
            padx=10,
            pady=5,
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X)
    
    def append_message(self, sender, content, extra_info=None):
        """
        向对话历史区域追加消息
        参数：sender - 发送者（"你"或"系统"）
              content - 消息内容
              extra_info - 附加信息（如匹配关键词，可选）
        """
        self.history_text.config(state=tk.NORMAL)
        
        if sender == "你":
            # 用户消息：蓝色标签
            self.history_text.insert(tk.END, f"你：{content}\n", "user")
        else:
            # 系统消息：绿色标签
            self.history_text.insert(tk.END, f"系统：{content}\n", "system")
            # 如果有附加信息，以灰色小字显示
            if extra_info:
                self.history_text.insert(tk.END, f"    {extra_info}\n", "extra")
        
        self.history_text.insert(tk.END, "\n")
        self.history_text.config(state=tk.DISABLED)
        self.history_text.see(tk.END)  # 自动滚动到最后
    
    def handle_send(self, event=None):
        """处理发送按钮点击或回车键事件"""
        user_input = self.input_entry.get().strip()
        
        if not user_input:
            messagebox.showwarning("提示", "请输入问题！")
            return
        
        # 检查是否为退出指令
        if user_input in ["退出", "exit", "EXIT"]:
            self.append_message("你", user_input)
            self.append_message("系统", "对话结束，感谢使用！")
            self.input_entry.config(state=tk.DISABLED)
            self.send_btn.config(state=tk.DISABLED)
            self.status_bar.config(text="对话已结束")
            return
        
        # 将用户提问加入历史记录
        self.user_history.append(user_input)
        
        # 显示用户消息
        self.append_message("你", user_input)
        
        # 调用匹配引擎获取答案
        answer, matched_question, matched_keywords = match_answer(user_input)
        
        # 准备附加信息
        extra_info = ""
        if matched_question and matched_keywords:
            extra_info = f"（匹配问题：{matched_question}，匹配关键词：{', '.join(matched_keywords)}）"
        
        # 显示系统答案
        self.append_message("系统", answer, extra_info)
        
        # 更新状态栏
        self.status_bar.config(text=f"已回答第 {len(self.user_history)} 个问题")
        
        # 清空输入框
        self.input_entry.delete(0, tk.END)
    
    def clear_history(self):
        """清空对话历史"""
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        self.history_text.config(state=tk.DISABLED)
        self.user_history.clear()
        self.status_bar.config(text="对话历史已清空")

# ============================================
# 主程序入口
# ============================================

if __name__ == "__main__":
    # 创建主窗口
    root = tk.Tk()
    # 创建问答系统界面实例
    app = AIQASystemGUI(root)
    # 启动主事件循环
    root.mainloop()