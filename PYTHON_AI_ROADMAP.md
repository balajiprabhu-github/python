# Python Roadmap for AI Engineers

For a mobile engineer (Kotlin, Android, Flutter) moving to AI engineering.
Scope: **Python only**: the language, its tooling, and the Python libraries used in AI work.
Not covered here: ML theory, Docker/Kubernetes, cloud, Git/Linux. Those belong in separate repos.

Pace: ~8–10 hrs/week, about 14 weeks.

## Kotlin/Dart → Python cheat sheet

| Concept | Kotlin / Dart | Python |
|---|---|---|
| Null safety | `?`, `?.`, `?:` | `None`, `x or default`, `is not None` |
| Data class | `data class` / freezed | `@dataclass`, `pydantic.BaseModel` |
| Coroutines | `suspend`, `Flow` | `async/await`, `asyncio`, generators |
| Collection ops | `map/filter/fold` | comprehensions, `itertools`, `functools` |
| Interfaces | `interface` | `Protocol`, `ABC` |
| Build/deps | Gradle / pub | `pyproject.toml`, `uv` / `pip` |
| Static typing | enforced | optional: `pyright` / `mypy` |

---

## Phase 1: Core language (Weeks 1–3)
- Syntax, dynamic typing, truthiness, f-strings, unpacking
- `list`, `dict`, `set`, `tuple`, comprehensions, slicing
- Functions: `*args/**kwargs`, closures, lambdas, default-arg pitfalls
- Errors: `try/except/finally`, custom exceptions
- Modules, packages, imports, `if __name__ == "__main__"`
- File I/O, `pathlib`, `json`, `csv`, `logging`
- Environment: `uv` / `venv`, `pyproject.toml`, Jupyter, VS Code

**Projects:** CLI file-organizer (`argparse` or `typer`); JSON/CSV report generator.

## Phase 2: Idiomatic and intermediate Python (Weeks 4–6)
- OOP: classes, dunder methods, `@property`, inheritance vs composition
- `@dataclass`, `enum`, `__slots__`
- Iterators, generators, `yield`
- Decorators and context managers (`with`, `contextlib`)
- `itertools`, `functools`, `collections`
- Type hints: `typing`, generics, `Protocol`, `TypedDict`
- Pydantic v2: models, validation, settings
- Regex, `datetime`, `argparse`

**Projects:** typed config loader with Pydantic; a decorator toolkit (retry, timing, cache).

## Phase 3: Quality, testing, packaging (Weeks 7–8)
- `pytest`: fixtures, parametrize, mocking (`unittest.mock`, `pytest-mock`)
- Linting and formatting: `ruff`
- Static checking: `pyright` / `mypy`
- Packaging a library, `src/` layout, `pyproject.toml`
- Debugging: `pdb`, logging, profiling (`cProfile`, `timeit`)

**Project:** package a small library with tests, type hints, and CI-ready config.

## Phase 4: Networking, async, concurrency (Weeks 9–10)
- HTTP with `httpx` / `requests`: retries, timeouts, rate limits, pagination
- `asyncio`: tasks, `gather`, semaphores, async context managers, async generators
- Threads vs processes vs async, and the GIL
- Streaming responses (SSE), WebSockets basics
- **FastAPI**: routes, dependency injection, Pydantic request/response models, background tasks

**Projects:** async API client with retries and rate limiting; small FastAPI service with streaming.

## Phase 5: Data stack (Weeks 11–12)
- **NumPy**: arrays, broadcasting, vectorization, shapes
- **Pandas**: DataFrame, groupby, merge, cleaning, time series
- **Matplotlib / Plotly**: quick EDA charts
- SQL from Python: `sqlite3`, SQLAlchemy
- Parquet/CSV/JSON pipelines

**Project:** clean and analyze a real dataset with reusable, tested functions.

## Phase 6: Python for AI work (Weeks 13–14)
Python-side skills that apply to AI engineering:
- LLM SDKs (OpenAI, Gemini, Anthropic): chat, streaming, tool calling
- Structured output with Pydantic
- Embeddings and similarity search with NumPy
- Text chunking and document loading (PDF, HTML, Markdown)
- Vector store clients (Chroma, FAISS)
- Basic agent loop written by hand: model call → tool call → result → repeat
- Tracing/logging model calls, token and cost counting
- Intro to Hugging Face `transformers` and PyTorch tensors (usage, not theory)

**Projects:** a RAG pipeline in plain Python (no framework); a hand-written tool-using agent loop.

---

## Suggested repo layout
```
Python/
├── 01-core/
├── 02-intermediate/
├── 03-quality-testing/
├── 04-async-http-fastapi/
├── 05-data/
├── 06-ai-python/
└── PYTHON_AI_ROADMAP.md
```
Each folder holds small exercises and one project, each with its own tests.

## Weekly rhythm
- 3 days learn, 2 days build, 1 day review and commit.

## Checkpoints
- Week 3: write scripts without looking up syntax
- Week 6: typed, Pydantic-validated code that passes `ruff` and `pyright`
- Week 8: a tested, packaged library
- Week 10: async API client and a FastAPI service
- Week 14: RAG pipeline and agent loop in plain Python

## Resources
| Topic | Resource |
|---|---|
| Language | Official Python tutorial, *Fluent Python*, Real Python, exercism.org |
| Typing/Pydantic | Pydantic docs, `typing` docs |
| Async/HTTP | `asyncio` docs, `httpx` docs, FastAPI docs |
| Data | *Python for Data Analysis*, Kaggle Learn |
| AI SDKs | Official OpenAI / Gemini / Anthropic Python docs |

## Skip for now
Django, GUI toolkits, advanced metaprogramming, and ML theory.
