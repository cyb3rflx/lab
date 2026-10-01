# agent-chef

Ein kleiner KI-Koch im Terminal: Du gibst ein, welche Zutaten du zu Hause hast, und der Agent sucht im Web nach bis zu 3 Rezepten, die du **nur mit genau diesen Zutaten** kochen kannst.

Gebaut mit [LangChain](https://www.langchain.com/) (`create_agent`), einem OpenAI-Modell und der [Tavily](https://tavily.com/)-Websuche als Tool.

## Voraussetzungen

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)
- API-Keys für:
  - [OpenAI](https://platform.openai.com/api-keys)
  - [Tavily](https://app.tavily.com/)
  - optional [LangSmith](https://smith.langchain.com/) für Tracing

## Installation

```bash
uv sync
```

## Konfiguration

Kopiere die Beispieldatei und trage deine Keys ein:

```bash
cp .env.example .env
```

```env
OPENAI_API_KEY=your-openai-api-key
TAVILY_API_KEY=your-tavily-api-key
```

Die LangSmith-Variablen in `.env.example` sind optional. Entferne dort das `#`, wenn du Tracing nutzen willst.

> Die `.env` ist per `.gitignore` ausgeschlossen. Committe niemals deine echten Keys.

## Nutzung

```bash
uv run main.py
```

Beispiel:

```text
Hello from agent-chef!
Welche Zutaten hast du zur Verfügung?: Eier, Mehl, Milch, Butter, Salz
```

Der Agent sucht daraufhin passende Rezepte im Web und gibt dir maximal 3 Vorschläge aus.

## Anpassen

- **Modell:** In `main.py` bei `create_agent("openai:gpt-5", ...)` ein anderes Modell eintragen.
- **Verhalten:** Den `system_prompt` in `main.py` ändern, z. B. für vegetarische Rezepte oder mehr Vorschläge.
