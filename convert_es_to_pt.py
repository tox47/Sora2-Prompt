#!/usr/bin/env python3
"""
将西班牙语版本转换为葡萄牙语版本
"""

import re

# 西班牙语到葡萄牙语的关键词映射
replacements = [
    # 标题和部分
    ('Galería de Prompts de Sora 2', 'Galeria de Prompts do Sora 2'),
    ('## 🎬 Introducción', '## 🎬 Introdução'),
    ('### ¿Qué es Sora 2?', '### O que é o Sora 2?'),
    ('## 📊 Colección de Prompts', '## 📊 Coleção de Prompts'),
    ('## 🎥 Prompts Destacados', '## 🎥 Prompts em Destaque'),
    ('### Animación y Estilo Anime', '### Animação e Estilo Anime'),
    ('### Realista y Cinematográfico', '### Realista e Cinematográfico'),
    ('### Fantasía y Criaturas', '### Fantasia e Criaturas'),
    ('### Efectos Cameo', '### Efeitos Cameo'),
    ('## 📋 Tabla Completa de Prompts', '## 📋 Tabela Completa de Prompts'),
    ('## 🎯 Categorías de Prompts', '## 🎯 Categorias de Prompts'),
    ('### 🎨 Animación y Estilos Artísticos', '### 🎨 Animação e Estilos Artísticos'),
    ('### 🐉 Fantasía y Criaturas', '### 🐉 Fantasia e Criaturas'),
    ('### 🎭 Cultural y Actuaciones', '### 🎭 Cultural e Apresentações'),
    ('### 🍳 Artes Culinarias', '### 🍳 Artes Culinárias'),
    ('### 🔬 Científico y Educativo', '### 🔬 Científico e Educacional'),
    ('### 🎬 Acción y Aventura', '### 🎬 Ação e Aventura'),
    ('### 🎨 Artesanía', '### 🎨 Artesanato'),
    ('## 💡 Consejos para Crear Prompts Efectivos', '## 💡 Dicas para Criar Prompts Eficazes'),
    ('## 🔗 Recursos', '## 🔗 Recursos'),
    ('## 🤝 Contribuir', '## 🤝 Contribuir'),
    ('## 📜 Licencia', '## 📜 Licença'),
    ('## 🌐 Otros Idiomas', '## 🌐 Outros Idiomas'),
    
    # 常见短语
    ('Bienvenido a la', 'Bem-vindo à'),
    ('colección completa', 'coleção completa'),
    ('Esta colección incluye:', 'Esta coleção inclui:'),
    ('prompts oficiales', 'prompts oficiais'),
    ('prompts adicionales', 'prompts adicionais'),
    ('fuentes comunitarias', 'fontes comunitárias'),
    ('Descripción', 'Descrição'),
    ('Fuente', 'Fonte'),
    ('Enlace', 'Link'),
    ('Comunidad', 'Comunidade'),
    
    # 描述词
    ('es el modelo', 'é o modelo'),
    ('puede crear', 'pode criar'),
    ('Comprende', 'Compreende'),
    ('puede producir', 'pode produzir'),
    ('calidad cinematográfica', 'qualidade cinematográfica'),
    
    # 表格标题
    ('Descripción del Efecto', 'Descrição do Efeito'),
    ('Escena', 'Cena'),
    ('con ', 'com '),
    (' y ', ' e '),
    
    # 常见动词和形容词
    ('ejecutando', 'executando'),
    ('demostrando', 'demonstrando'),
    ('modelado', 'modelagem'),
    ('físico', 'física'),
    ('complejo', 'complexa'),
    ('perfecto', 'perfeito'),
    ('Hermoso', 'Belo'),
    ('espectáculo', 'espetáculo'),
    ('impresionante', 'impressionante'),
    ('inspirada', 'inspirada'),
    ('estilo', 'estilo'),
    ('dibujado', 'desenhado'),
    ('Encantadora', 'Encantadora'),
    ('animación', 'animação'),
    ('sincronizada', 'sincronizada'),
    ('cinematográfica', 'cinematográfica'),
    ('dramática', 'dramática'),
    ('efectos visuales', 'efeitos visuais'),
    
    # 西班牙特殊字符
    ('épica', 'épica'),
    ('histórica', 'histórica'),
    ('realista', 'realista'),
    ('académico', 'acadêmico'),
    ('iluminación', 'iluminação'),
    ('atmósfera', 'atmosfera'),
    ('Icónica', 'Icônica'),
    ('reflejos', 'reflexos'),
    ('prehistórica', 'pré-histórica'),
    ('detallada', 'detalhada'),
    ('fotografía', 'fotografia'),
    ('humorística', 'humorística'),
    ('criatura', 'criatura'),
    ('fantasiosa', 'fantasiosa'),
    ('coloridos', 'coloridos'),
    ('viento', 'vento'),
    ('partículas', 'partículas'),
    ('hielo', 'gelo'),
    ('ejecutando', 'executando'),
    ('movimientos', 'movimentos'),
    ('gimnásticos', 'ginásticos'),
    ('complejos', 'complexos'),
    ('simulación', 'simulação'),
    ('avanzada', 'avançada'),
    
    # 最后修正
    ('Patinadora artística profesional', 'Patinadora artística profissional'),
    ('salto triple axel', 'salto triplo axel'),
    ('equilibrado', 'equilibrado'),
    ('cabeza', 'cabeça'),
    
    # 结束语
    ('Impulsado por la comunidad Sora', 'Desenvolvido pela comunidade Sora'),
    ('Última actualización', 'Última atualização'),
    ('Octubre 2025', 'Outubro 2025'),
    
    # 贡献部分
    ('Damos la bienvenida a contribuciones', 'Damos as boas-vindas a contribuições'),
    ('Haz fork de este repositorio', 'Faça um fork deste repositório'),
    ('Agrega tus prompts', 'Adicione seus prompts'),
    ('archivos README', 'arquivos README'),
    ('idioma apropiado', 'idioma apropriado'),
    ('Envía un pull request', 'Envie um pull request'),
    
    # 许可证
    ('Este repositorio es para fines educativos', 'Este repositório é para fins educacionais'),
    ('Todo el contenido generado', 'Todo o conteúdo gerado'),
    ('pertenece a sus respectivos creadores', 'pertence aos seus respectivos criadores'),
    
    # 其他语言列表
    ('(Inglés)', '(Inglês)'),
    ('(Chino Simplificado)', '(Chinês Simplificado)'),
    ('(Chino Tradicional)', '(Chinês Tradicional)'),
    ('(Español)', '(Espanhol)'),
    ('(Árabe)', '(Árabe)'),
    ('(Portugués)', '(Português)'),
    ('(Ruso)', '(Russo)'),
    ('(Francés)', '(Francês)'),
    ('(Alemán)', '(Alemão)'),
    
    # 技巧部分
    ('Sea Específico', 'Seja Específico'),
    ('Incluya detalles', 'Inclua detalhes'),
    ('escenario', 'cenário'),
    ('ángulos de cámara', 'ângulos de câmera'),
    ('ambiente', 'atmosfera'),
    ('Use Lenguaje Descriptivo', 'Use Linguagem Descritiva'),
    ('Adjetivos ricos', 'Adjetivos ricos'),
    ('transmitir', 'transmitir'),
    ('visión exacta', 'visão exata'),
    ('desea', 'deseja'),
    ('Especifique el Estilo', 'Especifique o Estilo'),
    ('Mencione estilos artísticos', 'Mencione estilos artísticos'),
    ('Incluya Detalles Técnicos', 'Inclua Detalhes Técnicos'),
    ('Tipo de cámara', 'Tipo de câmera'),
    ('película', 'filme'),
    ('composición de plano', 'composição do plano'),
    ('Describa el Movimiento', 'Descreva o Movimento'),
    ('Especifique cómo', 'Especifique como'),
    ('objetos', 'objetos'),
    ('personajes', 'personagens'),
    ('moverse', 'mover'),
    ('Establezca la Atmósfera', 'Defina a Atmosfera'),
    ('clima', 'clima'),
    ('hora del día', 'hora do dia'),
    ('condiciones de iluminación', 'condições de iluminação'),
    ('Agregue Contexto', 'Adicione Contexto'),
    ('Elementos de fondo', 'Elementos de fundo'),
    ('comportamiento de multitudes', 'comportamento de multidões'),
    ('detalles ambientales', 'detalhes ambientais'),
    
    # 资源
    ('Sitio Web Oficial', 'Site Oficial'),
    ('Galería de Prompts', 'Galeria de Prompts'),
    ('Colecciones Comunitarias', 'Coleções Comunitárias'),
    ('Varios repositorios', 'Vários repositórios'),
    ('sitios comunitarios', 'sites comunitários'),
]

# 读取文件
with open('/Users/spark/gitlab/Sora2-Prompt/README_pt.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 应用替换
for old, new in replacements:
    content = content.replace(old, new)

# 写回文件
with open('/Users/spark/gitlab/Sora2-Prompt/README_pt.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 葡萄牙语版本已更新完成！")
print(f"文件大小: {len(content)} 字符")
print(f"行数: {content.count(chr(10)) + 1} 行")

