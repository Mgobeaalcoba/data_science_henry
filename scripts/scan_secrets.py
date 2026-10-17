#!/usr/bin/env python3
"""Escanea el repo buscando patrones de credenciales. Sale con 1 si encuentra algo."""
import pathlib
import re
import sys

PATTERNS = [
    r"ghp_[A-Za-z0-9]{20,}",
    r"github_pat_[A-Za-z0-9_]{20,}",
    r"sk-[A-Za-z0-9]{20,}",
    r"AKIA[0-9A-Z]{16}",
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    r"xox[baprs]-[A-Za-z0-9-]{10,}",
    r"(?i)(password|passwd|secret|api[_-]?key|token)\s*[:=]\s*['\"][^'\"\s]{8,}['\"]",
    r"\b\d{2}\.\d{3}\.\d{3}\b.*(DNI|CUIL)",
    r"\b\d{22}\b",
]

SKIP_DIRS = {
    ".git", ".venv", "venv", "env", "node_modules", "__pycache__", "site-packages",
    ".next", "dist", "build", ".mypy_cache", ".pytest_cache", ".ruff_cache", ".tox",
}
SKIP_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".mp4", ".pptx", ".docx",
    ".xlsx", ".woff", ".woff2", ".ttf", ".ico",
}


def main() -> int:
    root = pathlib.Path(__file__).resolve().parent.parent
    bad = 0
    for path in root.rglob("*"):
        if not path.is_file() or path.name in {"scan_secrets.py", "install_hooks.sh"}:
            continue
        if path.suffix.lower() in SKIP_SUFFIXES:
            continue
        rel_dirs = path.relative_to(root).parts[:-1]
        if any(part in SKIP_DIRS or part.endswith(".egg-info") for part in rel_dirs):
            continue
        try:
            text = path.read_text(errors="ignore")
        except OSError:
            continue
        for pattern in PATTERNS:
            for match in re.finditer(pattern, text):
                print(f"[!] {path.relative_to(root)}: {match.group(0)[:40]}")
                bad += 1
    print("OK: sin secretos detectados" if not bad else f"{bad} hallazgo(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
