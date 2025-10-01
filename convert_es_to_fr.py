#!/usr/bin/env python3
"""
将西班牙语版本转换为法语版本
"""

replacements = [
    # 标题
    ('Galería de Prompts de Sora 2', 'Galerie de Prompts Sora 2'),
    ('## 🎬 Introducción', '## 🎬 Introduction'),
    ('### ¿Qué es Sora 2?', '### Qu\'est-ce que Sora 2 ?'),
    ('## 📊 Colección de Prompts', '## 📊 Collection de Prompts'),
    ('## 🎥 Prompts Destacados', '## 🎥 Prompts en Vedette'),
    ('### Animación y Estilo Anime', '### Animation et Style Anime'),
    ('### Realista y Cinematográfico', '### Réaliste et Cinématographique'),
    ('### Fantasía y Criaturas', '### Fantaisie et Créatures'),
    ('### Efectos Cameo', '### Effets Cameo'),
    ('## 📋 Tabla Completa de Prompts', '## 📋 Tableau Complet des Prompts'),
    ('## 🎯 Categorías de Prompts', '## 🎯 Catégories de Prompts'),
    ('### 🎨 Animación y Estilos Artísticos', '### 🎨 Animation et Styles Artistiques'),
    ('### 🌍 Realista y Cinematográfico', '### 🌍 Réaliste et Cinématographique'),
    ('### 🐉 Fantasía y Criaturas', '### 🐉 Fantaisie et Créatures'),
    ('### 👤 Tecnología Cameo', '### 👤 Technologie Cameo'),
    ('### 🏙️ Urbano y Arquitectura', '### 🏙️ Urbain et Architecture'),
    ('### 🌿 Naturaleza y Vida Silvestre', '### 🌿 Nature et Faune'),
    ('### 🎭 Cultural y Actuaciones', '### 🎭 Culturel et Performances'),
    ('### 🍳 Artes Culinarias', '### 🍳 Arts Culinaires'),
    ('### 🔬 Científico y Educativo', '### 🔬 Scientifique et Éducatif'),
    ('### 🎬 Acción y Aventura', '### 🎬 Action et Aventure'),
    ('### 🎨 Artesanía', '### 🎨 Artisanat'),
    ('## 💡 Consejos para Crear Prompts Efectivos', '## 💡 Conseils pour Créer des Prompts Efficaces'),
    ('## 🔗 Recursos', '## 🔗 Ressources'),
    ('## 🤝 Contribuir', '## 🤝 Contribuer'),
    ('## 📜 Licencia', '## 📜 Licence'),
    ('## 🌐 Otros Idiomas', '## 🌐 Autres Langues'),
    
    # 常见短语
    ('Bienvenido a la', 'Bienvenue dans la'),
    ('colección completa', 'collection complète'),
    ('Esta colección incluye:', 'Cette collection comprend :'),
    ('prompts oficiales', 'prompts officiels'),
    ('prompts adicionales', 'prompts supplémentaires'),
    ('fuentes comunitarias', 'sources communautaires'),
    ('Descripción', 'Description'),
    ('Fuente', 'Source'),
    ('Enlace', 'Lien'),
    ('Comunidad', 'Communauté'),
    
    # 描述
    ('es el modelo', 'est le modèle'),
    ('puede crear', 'peut créer'),
    ('Comprende', 'Comprend'),
    ('puede producir', 'peut produire'),
    ('calidad cinematográfica', 'qualité cinématographique'),
    
    # 表格
    ('Descripción del Efecto', 'Description de l\'Effet'),
    
    # 贡献
    ('Damos la bienvenida a contribuciones', 'Nous accueillons les contributions'),
    ('Haz fork de este repositorio', 'Forkez ce dépôt'),
    ('Agrega tus prompts', 'Ajoutez vos prompts'),
    ('archivos README', 'fichiers README'),
    ('idioma apropiado', 'langue appropriée'),
    ('Envía un pull request', 'Soumettez une pull request'),
    
    # 许可证
    ('Este repositorio es para fines educativos', 'Ce référentiel est à des fins éducatives'),
    ('Todo el contenido generado', 'Tout le contenu généré'),
    ('pertenece a sus respectivos creadores', 'appartient à ses créateurs respectifs'),
    
    # 语言
    ('(Inglés)', '(Anglais)'),
    ('(Chino Simplificado)', '(Chinois Simplifié)'),
    ('(Chino Tradicional)', '(Chinois Traditionnel)'),
    ('(Español)', '(Espagnol)'),
    ('(Árabe)', '(Arabe)'),
    ('(Portugués)', '(Portugais)'),
    ('(Ruso)', '(Russe)'),
    ('(Francés)', '(Français)'),
    ('(Alemán)', '(Allemand)'),
    
    # 技巧
    ('Sea Específico', 'Soyez Spécifique'),
    ('Incluya detalles', 'Incluez des détails'),
    ('escenario', 'décor'),
    ('iluminación', 'éclairage'),
    ('ángulos de cámara', 'angles de caméra'),
    ('ambiente', 'ambiance'),
    ('Use Lenguaje Descriptivo', 'Utilisez un Langage Descriptif'),
    ('transmitir', 'transmettre'),
    ('visión exacta', 'vision exacte'),
    ('desea', 'souhaitez'),
    ('Especifique el Estilo', 'Spécifiez le Style'),
    ('Mencione estilos artísticos', 'Mentionnez les styles artistiques'),
    ('Incluya Detalles Técnicos', 'Incluez des Détails Techniques'),
    ('Tipo de cámara', 'Type de caméra'),
    ('película', 'film'),
    ('composición de plano', 'composition du plan'),
    ('Describa el Movimiento', 'Décrivez le Mouvement'),
    ('Especifique cómo', 'Spécifiez comment'),
    ('objetos', 'objets'),
    ('personajes', 'personnages'),
    ('moverse', 'bouger'),
    ('Establezca la Atmósfera', 'Établissez l\'Atmosphère'),
    ('clima', 'météo'),
    ('hora del día', 'heure de la journée'),
    ('condiciones de iluminación', 'conditions d\'éclairage'),
    ('Agregue Contexto', 'Ajoutez du Contexte'),
    ('Elementos de fondo', 'Éléments d\'arrière-plan'),
    ('comportamiento de multitudes', 'comportement de la foule'),
    ('detalles ambientales', 'détails environnementaux'),
    
    # 资源
    ('Sitio Web Oficial', 'Site Officiel'),
    ('Galería de Prompts', 'Galerie de Prompts'),
    ('Colecciones Comunitarias', 'Collections Communautaires'),
    ('Varios repositorios', 'Divers dépôts'),
    ('sitios comunitarios', 'sites communautaires'),
    
    # 结束语
    ('Impulsado por la comunidad Sora', 'Propulsé par la communauté Sora'),
    ('Última actualización', 'Dernière mise à jour'),
    ('Octubre 2025', 'Octobre 2025'),
]

# 读取文件
with open('/Users/spark/gitlab/Sora2-Prompt/README_fr.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 应用替换
for old, new in replacements:
    content = content.replace(old, new)

# 写回文件
with open('/Users/spark/gitlab/Sora2-Prompt/README_fr.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 法语版本已更新完成！")
print(f"文件大小: {len(content)} 字符")
print(f"行数: {content.count(chr(10)) + 1} 行")

