# Compatibility matrix
| Feature | Claude Code | Codex |
|---|---|---|
| Agent Skills SKILL.md | Supported where enabled | Supported where enabled |
| `/clear` | Supported according to Anthropic documentation | Not assumed |
| `/compact` | Supported according to Anthropic documentation | Use available session management; verify commands |
| `/context` | Version-dependent: verify locally | Not assumed |
| Plan Mode | If supported by client | If supported by interface/release |
| Model routing | Use currently available model selection | Use currently available model and reasoning selection |

Last source-check: 2026-10-13. Always revalidate client-specific details: https://code.claude.com/docs and https://developers.openai.com/codex/ .
