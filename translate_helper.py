#!/usr/bin/env python3
"""
帮助脚本：用于将英文README翻译成其他语言的完整版本
这个脚本提供了一个框架，可以手动完成翻译或使用翻译工具
"""

# 语言配置
LANGUAGES = {
    'pt': {
        'name': 'Português',
        'intro_title': '## 🎬 Introdução',
        'what_is': '### O que é o Sora 2?',
        'collection': '## 📊 Coleção de Prompts',
        'featured': '## 🎥 Prompts em Destaque',
        'complete_table': '## 📋 Tabela Completa de Prompts',
        'categories': '## 🎯 Categorias de Prompts',
        'tips': '## 💡 Dicas para Criar Prompts Eficazes',
        'resources': '## 🔗 Recursos',
        'contribute': '## 🤝 Contribuir',
        'license': '## 📜 Licença',
        'other_langs': '## 🌐 Outros Idiomas',
    },
    'ru': {
        'name': 'Русский',
        'intro_title': '## 🎬 Введение',
        'what_is': '### Что такое Sora 2?',
        'collection': '## 📊 Коллекция промптов',
        'featured': '## 🎥 Избранные промпты',
        'complete_table': '## 📋 Полная таблица промптов',
        'categories': '## 🎯 Категории промптов',
        'tips': '## 💡 Советы по созданию эффективных промптов',
        'resources': '## 🔗 Ресурсы',
        'contribute': '## 🤝 Вклад',
        'license': '## 📜 Лицензия',
        'other_langs': '## 🌐 Другие языки',
    },
    'fr': {
        'name': 'Français',
        'intro_title': '## 🎬 Introduction',
        'what_is': '### Qu\'est-ce que Sora 2 ?',
        'collection': '## 📊 Collection de Prompts',
        'featured': '## 🎥 Prompts en Vedette',
        'complete_table': '## 📋 Tableau Complet des Prompts',
        'categories': '## 🎯 Catégories de Prompts',
        'tips': '## 💡 Conseils pour Créer des Prompts Efficaces',
        'resources': '## 🔗 Ressources',
        'contribute': '## 🤝 Contribuer',
        'license': '## 📜 Licence',
        'other_langs': '## 🌐 Autres Langues',
    },
    'de': {
        'name': 'Deutsch',
        'intro_title': '## 🎬 Einführung',
        'what_is': '### Was ist Sora 2?',
        'collection': '## 📊 Prompt-Sammlung',
        'featured': '## 🎥 Hervorgehobene Prompts',
        'complete_table': '## 📋 Vollständige Prompt-Tabelle',
        'categories': '## 🎯 Prompt-Kategorien',
        'tips': '## 💡 Tipps zum Erstellen effektiver Prompts',
        'resources': '## 🔗 Ressourcen',
        'contribute': '## 🤝 Beitragen',
        'license': '## 📜 Lizenz',
        'other_langs': '## 🌐 Andere Sprachen',
    },
    'ar': {
        'name': 'العربية',
        'intro_title': '## 🎬 مقدمة',
        'what_is': '### ما هو Sora 2؟',
        'collection': '## 📊 مجموعة المطالبات',
        'featured': '## 🎥 المطالبات المميزة',
        'complete_table': '## 📋 جدول المطالبات الكامل',
        'categories': '## 🎯 فئات المطالبات',
        'tips': '## 💡 نصائح لإنشاء مطالبات فعالة',
        'resources': '## 🔗 موارد',
        'contribute': '## 🤝 المساهمة',
        'license': '## 📜 الترخيص',
        'other_langs': '## 🌐 لغات أخرى',
    },
}

print("""
=======================================================
Sora 2 Prompt 多语言翻译助手
=======================================================

此脚本显示需要翻译的语言结构。

要完成翻译，您可以：
1. 使用专业翻译工具（Google Translate API, DeepL等）
2. 手动翻译每个部分
3. 使用AI翻译助手

当前配置的语言：
""")

for lang_code, config in LANGUAGES.items():
    print(f"  - {config['name']} (README_{lang_code}.md)")

print("""
=======================================================
建议的翻译流程：
=======================================================

1. 从 README.md 或 README_zh-CN.md 复制完整内容
2. 逐节翻译（保持prompts原文不变）
3. 仅翻译描述、说明和导航文本
4. 保留所有markdown格式和链接
5. 保留emoji和表格结构

需要翻译的主要部分：
- 标题和简介
- 分类说明
- 效果描述
- 使用技巧
- 贡献指南

不需要翻译的部分：
- Prompt原文（保持英文）
- 链接URL
- 代码块
- 徽章标记

=======================================================
""")

