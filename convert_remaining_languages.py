#!/usr/bin/env python3
"""
批量转换剩余语言版本
"""

# 德语替换
de_replacements = [
    ('Galería de Prompts de Sora 2', 'Sora 2 Prompt Galerie'),
    ('## 🎬 Introducción', '## 🎬 Einführung'),
    ('### ¿Qué es Sora 2?', '### Was ist Sora 2?'),
    ('Bienvenido a la', 'Willkommen in der'),
    ('colección completa', 'umfassenden Sammlung'),
    ('## 📊 Colección de Prompts', '## 📊 Prompt-Sammlung'),
    ('Esta colección incluye:', 'Diese Sammlung umfasst:'),
    ('prompts oficiales', 'offizielle Prompts'),
    ('prompts adicionales', 'zusätzliche Prompts'),
    ('fuentes comunitarias', 'Community-Quellen'),
    ('## 🎥 Prompts Destacados', '## 🎥 Hervorgehobene Prompts'),
    ('### Animación y Estilo Anime', '### Animation und Anime-Stil'),
    ('### Realista y Cinematográfico', '### Realistisch und Kinematografisch'),
    ('### Fantasía y Criaturas', '### Fantasy und Kreaturen'),
    ('### Efectos Cameo', '### Cameo-Effekte'),
    ('## 📋 Tabla Completa de Prompts', '## 📋 Vollständige Prompt-Tabelle'),
    ('Descripción', 'Beschreibung'),
    ('Fuente', 'Quelle'),
    ('Enlace', 'Link'),
    ('## 🎯 Categorías de Prompts', '## 🎯 Prompt-Kategorien'),
    ('## 💡 Consejos para Crear Prompts Efectivos', '## 💡 Tipps zum Erstellen effektiver Prompts'),
    ('## 🔗 Recursos', '## 🔗 Ressourcen'),
    ('## 🤝 Contribuir', '## 🤝 Beitragen'),
    ('## 📜 Licencia', '## 📜 Lizenz'),
    ('## 🌐 Otros Idiomas', '## 🌐 Andere Sprachen'),
    ('(Inglés)', '(Englisch)'),
    ('(Español)', '(Spanisch)'),
    ('(Alemán)', '(Deutsch)'),
    ('Impulsado por la comunidad Sora', 'Unterstützt von der Sora-Community'),
    ('Última actualización', 'Letzte Aktualisierung'),
    ('Octubre 2025', 'Oktober 2025'),
]

# 俄语替换
ru_replacements = [
    ('Galería de Prompts de Sora 2', 'Галерея промптов Sora 2'),
    ('## 🎬 Introducción', '## 🎬 Введение'),
    ('### ¿Qué es Sora 2?', '### Что такое Sora 2?'),
    ('Bienvenido a la', 'Добро пожаловать в'),
    ('colección completa', 'всеобъемлющую коллекцию'),
    ('## 📊 Colección de Prompts', '## 📊 Коллекция промптов'),
    ('Esta colección incluye:', 'Эта коллекция включает:'),
    ('prompts oficiales', 'официальных промптов'),
    ('prompts adicionales', 'дополнительных промптов'),
    ('fuentes comunitarias', 'источников сообщества'),
    ('## 🎥 Prompts Destacados', '## 🎥 Избранные промпты'),
    ('### Animación y Estilo Anime', '### Анимация и стиль аниме'),
    ('### Realista y Cinematográfico', '### Реалистичный и кинематографический'),
    ('### Fantasía y Criaturas', '### Фэнтези и существа'),
    ('### Efectos Cameo', '### Эффекты камео'),
    ('## 📋 Tabla Completa de Prompts', '## 📋 Полная таблица промптов'),
    ('Descripción', 'Описание'),
    ('Fuente', 'Источник'),
    ('Enlace', 'Ссылка'),
    ('Comunidad', 'Сообщество'),
    ('## 🎯 Categorías de Prompts', '## 🎯 Категории промптов'),
    ('## 💡 Consejos para Crear Prompts Efectivos', '## 💡 Советы по созданию эффективных промптов'),
    ('## 🔗 Recursos', '## 🔗 Ресурсы'),
    ('## 🤝 Contribuir', '## 🤝 Вклад'),
    ('## 📜 Licencia', '## 📜 Лицензия'),
    ('## 🌐 Otros Idiomas', '## 🌐 Другие языки'),
    ('(Inglés)', '(Английский)'),
    ('(Español)', '(Испанский)'),
    ('(Ruso)', '(Русский)'),
    ('Impulsado por la comunidad Sora', 'При поддержке сообщества Sora'),
    ('Última actualización', 'Последнее обновление'),
    ('Octubre 2025', 'Октябрь 2025'),
]

# 阿拉伯语替换
ar_replacements = [
    ('Galería de Prompts de Sora 2', 'معرض مطالبات Sora 2'),
    ('## 🎬 Introducción', '## 🎬 مقدمة'),
    ('### ¿Qué es Sora 2?', '### ما هو Sora 2؟'),
    ('Bienvenido a la', 'مرحبًا بك في'),
    ('colección completa', 'مجموعة شاملة'),
    ('## 📊 Colección de Prompts', '## 📊 مجموعة المطالبات'),
    ('Esta colección incluye:', 'تتضمن هذه المجموعة:'),
    ('prompts oficiales', 'مطالبات رسمية'),
    ('prompts adicionales', 'مطالبات إضافية'),
    ('fuentes comunitarias', 'مصادر مجتمعية'),
    ('## 🎥 Prompts Destacados', '## 🎥 المطالبات المميزة'),
    ('### Animación y Estilo Anime', '### الرسوم المتحركة وأسلوب الأنمي'),
    ('### Realista y Cinematográfico', '### واقعي وسينمائي'),
    ('### Fantasía y Criaturas', '### الخيال والمخلوقات'),
    ('### Efectos Cameo', '### تأثيرات الظهور الخاص'),
    ('## 📋 Tabla Completa de Prompts', '## 📋 جدول المطالبات الكامل'),
    ('Descripción', 'الوصف'),
    ('Fuente', 'المصدر'),
    ('Enlace', 'رابط'),
    ('Comunidad', 'المجتمع'),
    ('## 🎯 Categorías de Prompts', '## 🎯 فئات المطالبات'),
    ('## 💡 Consejos para Crear Prompts Efectivos', '## 💡 نصائح لإنشاء مطالبات فعالة'),
    ('## 🔗 Recursos', '## 🔗 موارد'),
    ('## 🤝 Contribuir', '## 🤝 المساهمة'),
    ('## 📜 Licencia', '## 📜 الترخيص'),
    ('## 🌐 Otros Idiomas', '## 🌐 لغات أخرى'),
    ('(Inglés)', '(الإنجليزية)'),
    ('(Español)', '(الإسبانية)'),
    ('(Árabe)', '(العربية)'),
    ('Impulsado por la comunidad Sora', 'مدعوم من مجتمع Sora'),
    ('Última actualización', 'آخر تحديث'),
    ('Octubre 2025', 'أكتوبر 2025'),
]

def convert_language(filename, replacements):
    with open(f'/Users/spark/gitlab/Sora2-Prompt/{filename}', 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
    
    with open(f'/Users/spark/gitlab/Sora2-Prompt/{filename}', 'w', encoding='utf-8') as f:
        f.write(content)
    
    lines = content.count('\n') + 1
    print(f"✅ {filename} 已更新完成！行数: {lines}")

# 转换所有语言
print("开始批量转换...")
convert_language('README_de.md', de_replacements)
convert_language('README_ru.md', ru_replacements)
convert_language('README_ar.md', ar_replacements)
print("\n🎉 所有语言版本转换完成！")

