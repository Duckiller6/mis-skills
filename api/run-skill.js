const fs = require('fs');
const path = require('path');

const SKILLS = {
  'prueba-propuestas-modificacion-clases': 'prueba-propuestas-modificacion-clases/SKILL.md',
  'aeat-explicador-entrenador-test': 'aeat-explicador-entrenador-test/SKILL.md',
  'analizador-subastas-aeat-boe': 'analizador-subastas-aeat-boe/SKILL.md',
};

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Método no permitido.' });
  }

  if (!process.env.OPENAI_API_KEY) {
    return res.status(500).json({
      error: 'Falta configurar OPENAI_API_KEY en Vercel → Project Settings → Environment Variables.'
    });
  }

  try {
    const { skill, prompt } = req.body || {};
    if (!skill || !SKILLS[skill]) {
      return res.status(400).json({ error: 'Skill no válida.' });
    }
    if (!prompt || !String(prompt).trim()) {
      return res.status(400).json({ error: 'Escribí una consulta para ejecutar la skill.' });
    }

    const skillPath = path.join(process.cwd(), SKILLS[skill]);
    const instructions = fs.readFileSync(skillPath, 'utf8');
    const model = process.env.OPENAI_MODEL || 'gpt-5.6-luna';

    const response = await fetch('https://api.openai.com/v1/responses', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,
      },
      body: JSON.stringify({
        model,
        instructions,
        input: String(prompt).trim(),
      }),
    });

    const data = await response.json();
    if (!response.ok) {
      return res.status(response.status).json({
        error: data?.error?.message || 'Error al ejecutar la skill con OpenAI.'
      });
    }

    const output = Array.isArray(data.output)
      ? data.output
          .flatMap(item => Array.isArray(item.content) ? item.content : [])
          .filter(item => item.type === 'output_text' && item.text)
          .map(item => item.text)
          .join('\n\n')
      : '';

    return res.status(200).json({
      output: output || 'La respuesta no trajo texto.',
      model,
    });
  } catch (err) {
    return res.status(500).json({ error: err?.message || 'Error interno.' });
  }
};
