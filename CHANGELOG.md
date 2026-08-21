# Changelog

## 0.1.2 - 2026-08-22

### Changed

- Replaced the package-local CLI tree renderer with ChatStyle's registered Click tree runtime.
- Added the top-level `chatsmtp --tree-brief` contract alongside `--version` and `--tree`.
- Aligned runtime bounds to `chatstyle>=0.2.0,<0.3.0` and `chatenv>=0.2.10,<0.3.0`.
- Expanded tests, bilingual docs, and CI to verify editable and built-wheel CLI contracts.

## 0.1.1 - 2026-08-12

### Changed

- Added generated root-only `chatsmtp --tree` from the Click command surface.
- Updated README and MkDocs CLI tree pages to match the real command surface.
- Hardened CI, Preview Docs, Deploy Docs, and Publish Package workflow contracts.
- Removed the unused direct ChatStyle runtime dependency while preserving the ChatEnv provider entry point.

## 0.1.0 - 2026-07-27

### Added

- First formal ChatSMTP package release after the `0.0.1` PyPI placeholder.
- ChatArch CLI skeleton with `chatsmtp` entry point, ChatEnv provider wiring, tests, and MkDocs documentation scaffold.

### Changed

- Bounded documentation dependencies for stable strict MkDocs builds.

### Fixed
