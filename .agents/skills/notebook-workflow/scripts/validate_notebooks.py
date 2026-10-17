#!/usr/bin/env python3
"""Herramienta de inspección, auditoría y ejecución de notebooks para data_science_henry."""

import argparse
import glob
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def find_notebooks(filter_str: str | None = None) -> list[Path]:
    paths = sorted(ROOT.glob("clase_*/notebooks/*.ipynb"))
    if filter_str:
        paths = [p for p in paths if filter_str in str(p)]
    return paths


def inspect_notebook(path: Path) -> None:
    with open(path, encoding="utf-8") as f:
        nb = json.load(f)
    cells = nb.get("cells", [])
    rel = path.relative_to(ROOT)
    print(f"================ {rel} (total cells: {len(cells)}) ================")
    for i, c in enumerate(cells):
        ctype = c.get("cell_type")
        src = "".join(c.get("source", []))
        print(f"--- Cell {i} [{ctype}] ---")
        print(src)
        for out in c.get("outputs", []):
            otype = out.get("output_type")
            if otype == "error":
                print(f"  [ERROR]: {out.get('ename')}: {out.get('evalue')}")
            elif otype == "stream":
                name = out.get("name", "stdout")
                txt = "".join(out.get("text", [])).strip()
                if txt:
                    print(f"  [{name.upper()}]: {txt[:500]}")
            elif otype in ("execute_result", "display_data"):
                data = out.get("data", {})
                if "image/png" in data:
                    print("  [PLOT: image/png]")
                elif "text/plain" in data:
                    txt = "".join(data["text/plain"]).strip()
                    print(f"  [RESULT]: {txt[:400]}")
    print()


def execute_notebook(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    print(f"⏳ Ejecutando {rel} ...")
    jupyter_bin = ROOT / ".venv" / "bin" / "jupyter"
    cmd = [
        str(jupyter_bin),
        "nbconvert",
        "--to",
        "notebook",
        "--execute",
        "--inplace",
        "--ExecutePreprocessor.timeout=300",
        path.name,
    ]
    res = subprocess.run(cmd, cwd=path.parent, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"❌ Error ejecutando {rel}:\n{res.stderr}")
        return False
    print(f"✅ Ejecutado {rel}")
    return True


def audit_notebook(path: Path) -> list[str]:
    issues: list[str] = []
    rel = path.relative_to(ROOT)
    with open(path, encoding="utf-8") as f:
        nb = json.load(f)
    cells = nb.get("cells", [])
    if not cells:
        return [f"{rel}: Notebook vacío"]

    md_count = 0
    code_count = 0
    expected_exec = 1
    is_consulta = "clase_11_consulta" in str(rel)

    for i, c in enumerate(cells):
        ctype = c.get("cell_type")
        src = "".join(c.get("source", []))
        if "#gemini" in src.lower():
            issues.append(f"{rel} [Cell {i}]: Contiene etiqueta prohibida '#gemini'")

        if ctype == "markdown":
            md_count += 1
        elif ctype == "code":
            code_count += 1
            if src.strip() and not is_consulta:
                ec = c.get("execution_count")
                if ec is None:
                    issues.append(f"{rel} [Cell {i}]: Celda de código sin ejecutar (execution_count=None)")
                elif ec != expected_exec:
                    issues.append(
                        f"{rel} [Cell {i}]: execution_count={ec} no es secuencial (esperado {expected_exec})"
                    )
                expected_exec += 1

            for out in c.get("outputs", []):
                if out.get("output_type") == "error":
                    issues.append(
                        f"{rel} [Cell {i}]: Output con error {out.get('ename')}: {out.get('evalue')}"
                    )
                elif out.get("name") == "stderr":
                    txt = "".join(out.get("text", [])).strip()
                    if txt:
                        issues.append(f"{rel} [Cell {i}]: Output con stderr/warning: {txt[:120]}")

    if md_count < code_count:
        issues.append(
            f"{rel}: Menos celdas Markdown ({md_count}) que de código ({code_count}); revisar explicaciones"
        )

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Audita, inspecciona y ejecuta notebooks del curso.")
    parser.add_argument("--inspect", metavar="FILTRO", help="Inspecciona celdas de notebooks que coincidan")
    parser.add_argument("--execute", nargs="?", const="ALL", metavar="FILTRO", help="Re-ejecuta notebooks")
    parser.add_argument("--audit", action="store_true", help="Audita reglas técnicas y pedagógicas")
    args = parser.parse_args()

    if not ( args.inspect or args.execute or args.audit ):
        parser.print_help()
        return 0

    if args.inspect:
        for p in find_notebooks(None if args.inspect == "ALL" else args.inspect):
            inspect_notebook(p)

    if args.execute:
        filt = None if args.execute == "ALL" else args.execute
        ok = True
        for p in find_notebooks(filt):
            if not execute_notebook(p):
                ok = False
        if not ok:
            return 1

    if args.audit:
        all_nbs = find_notebooks()
        print(f"🔍 Auditando {len(all_nbs)} notebooks...")
        all_issues: list[str] = []
        for p in all_nbs:
            all_issues.extend(audit_notebook(p))
        if all_issues:
            print(f"⚠️ Se encontraron {len(all_issues)} observaciones:")
            for iss in all_issues:
                print(f"  - {iss}")
            return 1
        print("✅ Todos los notebooks cumplen 100% las reglas de AGENTS.md (0 errores, 0 warnings, 0 tags residuales).")

    return 0


if __name__ == "__main__":
    sys.exit(main())
