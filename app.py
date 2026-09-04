from pathlib import Path
import os
import threading
import tkinter as tk
from tkinter import ttk, messagebox

from openai import OpenAI

ROOT = Path(__file__).resolve().parent
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6-sol")


def find_skills():
    skills = []
    for p in sorted(ROOT.glob("*/SKILL.md")):
        skills.append((p.parent.name, p))
    return skills


class SkillRunner(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Skills de Pato · Runner")
        self.geometry("980x760")
        self.minsize(820, 620)

        self.skills = find_skills()
        if not self.skills:
            messagebox.showerror("Sin skills", "No encontré carpetas con SKILL.md en este repo.")
            self.destroy()
            return

        self.skill_map = {name: path for name, path in self.skills}
        self.skill_var = tk.StringVar(value=self.skills[0][0])
        self.model_var = tk.StringVar(value=DEFAULT_MODEL)
        self.status_var = tk.StringVar(value="Listo")

        self._build_ui()

    def _build_ui(self):
        outer = ttk.Frame(self, padding=16)
        outer.pack(fill="both", expand=True)

        top = ttk.Frame(outer)
        top.pack(fill="x")

        ttk.Label(top, text="Skill:").grid(row=0, column=0, sticky="w", padx=(0, 8))
        skill_box = ttk.Combobox(
            top,
            textvariable=self.skill_var,
            values=[name for name, _ in self.skills],
            state="readonly",
            width=42,
        )
        skill_box.grid(row=0, column=1, sticky="ew", padx=(0, 16))

        ttk.Label(top, text="Modelo:").grid(row=0, column=2, sticky="w", padx=(0, 8))
        ttk.Entry(top, textvariable=self.model_var, width=22).grid(row=0, column=3, sticky="ew")
        top.columnconfigure(1, weight=1)

        ttk.Label(outer, text="Tu consulta:").pack(anchor="w", pady=(18, 6))
        self.prompt = tk.Text(outer, height=10, wrap="word")
        self.prompt.pack(fill="x")
        self.prompt.insert("1.0", "")

        controls = ttk.Frame(outer)
        controls.pack(fill="x", pady=12)

        self.run_btn = ttk.Button(controls, text="Ejecutar skill", command=self.run_skill)
        self.run_btn.pack(side="left")
        ttk.Button(controls, text="Limpiar", command=self.clear_all).pack(side="left", padx=(8, 0))
        ttk.Label(controls, textvariable=self.status_var).pack(side="right")

        ttk.Label(outer, text="Respuesta:").pack(anchor="w", pady=(6, 6))
        self.output = tk.Text(outer, wrap="word", state="disabled")
        self.output.pack(fill="both", expand=True)

        note = (
            "Necesitás definir OPENAI_API_KEY en tu PC antes de ejecutar. "
            "La clave no se guarda en este repo."
        )
        ttk.Label(outer, text=note).pack(anchor="w", pady=(10, 0))

    def clear_all(self):
        self.prompt.delete("1.0", "end")
        self._set_output("")
        self.status_var.set("Listo")

    def _set_output(self, text):
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", text)
        self.output.configure(state="disabled")

    def run_skill(self):
        user_prompt = self.prompt.get("1.0", "end").strip()
        if not user_prompt:
            messagebox.showwarning("Falta consulta", "Escribí qué querés pedirle a la skill.")
            return

        if not os.getenv("OPENAI_API_KEY"):
            messagebox.showerror(
                "Falta OPENAI_API_KEY",
                "Definí OPENAI_API_KEY en la terminal antes de ejecutar.\n\n"
                "PowerShell (solo esta sesión):\n$env:OPENAI_API_KEY=\"tu_clave\"",
            )
            return

        skill_path = self.skill_map[self.skill_var.get()]
        instructions = skill_path.read_text(encoding="utf-8")
        model = self.model_var.get().strip() or DEFAULT_MODEL

        self.run_btn.configure(state="disabled")
        self.status_var.set("Ejecutando…")
        self._set_output("")

        threading.Thread(
            target=self._call_openai,
            args=(instructions, user_prompt, model),
            daemon=True,
        ).start()

    def _call_openai(self, instructions, user_prompt, model):
        try:
            client = OpenAI()
            response = client.responses.create(
                model=model,
                instructions=instructions,
                input=user_prompt,
            )
            text = response.output_text or "(La respuesta no trajo texto.)"
            self.after(0, lambda: self._finish(text, None))
        except Exception as e:
            self.after(0, lambda: self._finish("", str(e)))

    def _finish(self, text, error):
        self.run_btn.configure(state="normal")
        if error:
            self.status_var.set("Error")
            self._set_output(error)
        else:
            self.status_var.set("Listo")
            self._set_output(text)


if __name__ == "__main__":
    SkillRunner().mainloop()
