.PHONY: setup-notes notes notes-dry pull

setup-notes:
	@echo "Usage: python3 scripts/setup_obsidian.py --vault '/path/to/your/Vault'"

notes:
	python3 scripts/sync_obsidian.py

notes-dry:
	python3 scripts/sync_obsidian.py --dry-run

pull:
	python3 scripts/pull.py
