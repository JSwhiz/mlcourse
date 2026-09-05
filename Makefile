.PHONY: install check notebooks setup-notes notes notes-dry pull

install:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements-ci.txt

check:
	python3 scripts/validate_repository.py

notebooks:
	@set -e; \
	mkdir -p /tmp/mlcourse-executed; \
	for notebook in $$(find . -type f -path './topic*/notebooks/*.ipynb' | sort); do \
		echo "Executing $$notebook"; \
		jupyter nbconvert --to notebook --execute "$$notebook" \
			--ExecutePreprocessor.timeout=300 \
			--ExecutePreprocessor.kernel_name=python3 \
			--output "$$(basename "$$notebook")" \
			--output-dir /tmp/mlcourse-executed >/dev/null; \
	done

setup-notes:
	@echo "Usage: python3 scripts/setup_obsidian.py --vault '/path/to/your/Vault'"

notes:
	python3 scripts/sync_obsidian.py

notes-dry:
	python3 scripts/sync_obsidian.py --dry-run

pull:
	python3 scripts/pull.py
