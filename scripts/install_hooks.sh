#!/bin/sh
# Instala el hook pre-commit que corre scan_secrets.py (local, no versionado).
cd "$(git rev-parse --show-toplevel)" || exit 1
printf '#!/bin/sh\npython3 scripts/scan_secrets.py || exit 1\n' > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit scripts/scan_secrets.py
echo "Hook pre-commit instalado"
