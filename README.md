# OpenHands MCP GitHub Agent - Comprehensive Guide

An autonomous AI agent demonstration project built using OpenHands SDK and MCP (Model Context Protocol), featuring progressive learning modules for Claude API integration.

## Project Overview

This project provides a structured learning path for developers to understand AI agent patterns, from basic API calls to advanced streaming and optimization techniques. The codebase is organized into three progressive modules that build upon each other.

---

## Architecture & Module Structure

### **Module 1: Foundations - API Basics & Conversation Management** 
*Basic to Intermediate Complexity | 6 Files | ~550 Lines of Code*

Core API patterns and conversation state management fundamentals.

#### Key Files:

1. **`first_call_single.py`** (80 LOC)
   - **Purpose**: Minimal example of Claude API integration
   - **Key Features**: Dataclass configuration, environment-based API key management
   - **Learning Focus**: Basic API setup and client initialization
   - **Pattern**: Configuration management using dataclasses
   ```python
   - Demonstrates how to set up Anthropic client
   - Uses environment variables for secure credential handling
   - Implements error handling for missing API keys
   ```

2. **`conversation_state.py`** (150 LOC)
   - **Purpose**: Educational comparison of stateless vs stateful conversation patterns
   - **Key Features**: Interactive model selection, custom system instructions
   - **Learning Focus**: Understanding conversation context preservation
   - **Patterns**:
     - **Stateless Model**: Each API call is independent (no memory)
     - **Stateful Model**: Maintains conversation history for contextual awareness
   ```python
   - Demonstrates how stateless calls fail to retain context
   - Shows how conversation_history list maintains state
   - Includes real-time history visualization
   ```

3. **`json_response_demo.py`** (100 LOC)
   - **Purpose**: Structured JSON output parsing and validation
   - **Key Features**: Schema-enforced responses, JSON error handling
   - **Learning Focus**: Output format enforcement and validation
   - **Pattern**: System instructions for forcing JSON format
   ```python
   - Uses system prompt to enforce JSON-only output
   - Includes JSON parsing with error handling
   - Demonstrates schema validation (title, category, priority, summary, steps)
   ```

4. **`conversation_loop.py`** (60 LOC)
   - **Purpose**: Simple turn-based conversation loop
   - **Key Features**: Loop control, input validation
   - **Production Ready**: Partial

5. **`pass_instructions_demo.py`** (50 LOC)
   - **Purpose**: System instruction customization
   - **Key Features**: User-defined instructions, dynamic prompt engineering
   - **Production Ready**: Yes

6. **`enfroce_outpt.py`** (120 LOC)
   - **Purpose**: Output format validation and enforcement
   - **Key Features**: JSON validation, structured response handling
   - **Production Ready**: Yes

---

### **Module 2: Intermediate Patterns - Context & Multi-Agent Systems**
*Intermediate to Advanced Complexity | 7 Files | ~800 Lines of Code*

Conversational agents with contextual awareness, data processing, and specialized use cases.

#### Key Files:

1. **`chatbot.py`** (100 LOC)
   - **Purpose**: Conversational chatbot with history management
   - **Key Features**:
     - Conversation history trimming (keeps last 10 messages)
     - Error handling for rate limits and API errors
     - Session management with /reset and /exit commands
   - **Pattern**: Memory-efficient conversation tracking
   ```python
   - Maintains full conversation context for coherence
   - Trims history to prevent token overflow
   - Graceful error handling for rate limiting
   ```

2. **`data_check_agent.py`** (130 LOC)
   - **Purpose**: Q&A agent for CSV data analysis
   - **Key Features**:
     - Multi-encoding CSV support (UTF-8, Latin1, CP1252)
     - Automated dataset summarization
     - Natural language queries on structured data
   - **Pattern**: Data extraction + LLM reasoning
   ```python
   - Loads CSV with fallback encoding strategies
   - Generates statistical summaries automatically
   - Answers user questions based on data context
   ```

3. **`contentReveiwAgent.py`** (110 LOC)
   - **Purpose**: PII detection and content review
   - **Key Features**: Safety checks, PII identification
   - **Production Ready**: Yes
   - **Pattern**: Content moderation through LLM analysis

4. **`context_aware_context.py`** (100 LOC)
   - **Purpose**: Context personalization and embedding
   - **Key Features**: JSON context injection, personalized responses
   - **Production Ready**: Yes
   - **Pattern**: Dynamic context enrichment

5. **`runtime_context_demo.py`** (90 LOC)
   - **Purpose**: Runtime context injection for request traceability
   - **Key Features**: Request tracking, context embedding
   - **Production Ready**: Yes
   - **Pattern**: Metadata propagation through conversation

6. **`taskPlanner.py`** (85 LOC)
   - **Purpose**: Multi-turn task planning agent
   - **Key Features**: Task decomposition, multi-turn dialogue
   - **Production Ready**: Yes

7. **`test_app.py`** (90 LOC)
   - **Purpose**: Text processing utility with instruction loops
   - **Production Ready**: Partial

---

### **Module 3: Advanced Patterns - Streaming, Resilience & Optimization**
*Advanced Complexity | 6 Files | ~800 Lines of Code*

Production-ready patterns for performance, reliability, and scalability.

#### Key Files:

1. **`streaming_chat.py`** (130 LOC)
   - **Purpose**: Real-time async streaming chat
   - **Key Features**:
     - Async/await pattern for concurrent operations
     - Token-by-token streaming for real-time response
     - Stream context management
   - **Production Ready**: Yes
   - **Pattern**: Non-blocking I/O for better UX
   ```python
   - Uses AsyncAnthropic client for async operations
   - Implements text_stream for progressive output
   - Handles graceful stream closure
   ```

2. **`token_optimization.py`** (110 LOC)
   - **Purpose**: Cost analysis and token optimization
   - **Key Features**: Prompt variant comparison, usage analytics
   - **Learning Focus**: Token efficiency and cost reduction
   - **Pattern**: A/B testing different prompt strategies
   ```python
   - Compares verbose vs concise prompts
   - Measures actual token usage (input + output)
   - Demonstrates token savings through optimization
   - Result Example: Naive (800→300 tokens), Optimized (300→200 tokens)
   ```

3. **`rate_limiting_timeout_demo.py`** (120 LOC)
   - **Purpose**: Exponential backoff retry mechanism
   - **Key Features**: Resilience pattern, rate limit handling
   - **Production Ready**: Yes
   - **Pattern**: Intelligent retry with exponential backoff
   ```python
   - Implements exponential backoff strategy
   - Handles rate limit errors gracefully
   - Configurable retry attempts and backoff multiplier
   ```

4. **`retry.demo.py`** (70 LOC)
   - **Purpose**: Simple fixed-delay retry mechanism
   - **Key Features**: Basic retry loop
   - **Production Ready**: Partial
   - **Pattern**: Simple failure recovery

5. **`app.py`** (110 LOC)
   - **Purpose**: Streamlit web interface for agents
   - **Key Features**: Streaming UI, interactive web interface
   - **Production Ready**: Yes
   - **Pattern**: Web UI for chatbot deployment

6. **`multi_step.py`** (140 LOC)
   - **Purpose**: Dynamic multi-step prompt generation
   - **Key Features**: Intent detection, step decomposition
   - **Production Ready**: Yes
   - **Pattern**: Complex task decomposition with intent routing

---

## Technologies & Stack

| Component | Technology | Version/Model |
|-----------|-----------|--------------|
| **AI Model** | Claude API | claude-sonnet-4.5, claude-v1 |
| **Language** | Python | 3.8+ |
| **Async Support** | asyncio | Built-in |
| **HTTP Client** | Anthropic SDK | Latest |
| **Environment** | python-dotenv | For API key management |
| **Data Processing** | pandas | CSV handling (Module 2) |
| **Web Framework** | Streamlit | Optional (Module 3) |

---

## Setup & Installation

### Prerequisites
- Python 3.8+
- Anthropic API key (from Claude dashboard)

### Install Dependencies

```bash
pip install -r requirements.txt
```

Expected dependencies:
```
anthropic>=0.7.0
python-dotenv>=0.19.0
pandas>=1.3.0
streamlit>=1.0.0  # Optional, for web UI
```

### Configuration

1. **Create `.env` file** in project root:
```env
ANTHROPIC_API_KEY=your_api_key_here
```

2. **Load environment**:
```python
from dotenv import load_dotenv
load_dotenv()
```

---

## Usage Examples

### Module 1: Basic API Call
```bash
cd module1
python first_call_single.py
```
**Output**: Simple Claude response to a test message

### Module 2: Data Analysis Agent
```bash
cd module2
python data_check_agent.py
# Then ask questions about your CSV data
```
**Input**: CSV file path  
**Output**: Natural language answers about your data

### Module 3: Streaming Chat
```bash
cd module3
python streaming_chat.py
```
**Output**: Real-time character-by-character streaming responses

---

## Key Concepts Demonstrated

### 1. **Conversation State Management**
- Stateless vs Stateful patterns
- History trimming strategies
- Context window optimization

### 2. **Structured Output Generation**
- JSON schema enforcement
- Error handling for malformed responses
- Schema validation patterns

### 3. **Multi-Agent Coordination**
- Task decomposition
- Intent detection
- Routing logic

### 4. **Performance Optimization**
- Token usage analysis
- Prompt optimization
- Streaming for UX improvement

### 5. **Reliability Patterns**
- Exponential backoff retry
- Rate limit handling
- Error recovery strategies

### 6. **Data Processing Integration**
- CSV parsing with encoding fallbacks
- Automated summarization
- Natural language querying on data

---

## Production Readiness Ratings

| Module | File | Status | Notes |
|--------|------|--------|-------|
| 1 | first_call_single.py | ✅ Yes | Basic but complete |
| 1 | conversation_state.py | ✅ Yes | Educational showcase |
| 1 | json_response_demo.py | ✅ Yes | Schema validation works |
| 2 | chatbot.py | ✅ Yes | Full history management |
| 2 | data_check_agent.py | ✅ Yes | Multi-encoding support |
| 2 | contentReveiwAgent.py | ✅ Yes | Safety features included |
| 3 | streaming_chat.py | ✅ Yes | Async patterns solid |
| 3 | token_optimization.py | ✅ Yes | Cost analysis accurate |
| 3 | rate_limiting_timeout_demo.py | ✅ Yes | Resilience patterns |

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│              Module 1: Foundations                      │
│  (Basic API, Conversation State, Output Formatting)     │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│          Module 2: Intermediate Patterns                │
│   (Chatbots, Agents, Context Awareness, Data Q&A)       │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│           Module 3: Advanced Patterns                   │
│  (Streaming, Resilience, Token Optimization, Web UI)    │
└─────────────────────────────────────────────────────────┘
```

---

## Common Patterns

### Pattern 1: Error Handling with Retry
```python
from anthropic import RateLimitError, APIError

try:
    response = client.messages.create(...)
except RateLimitError:
    # Exponential backoff
    time.sleep(2 ** attempt)
except APIError as e:
    # Handle API errors
    print(f"API error: {e}")
```

### Pattern 2: History Trimming
```python
def trim_history(history, max_length=10):
    if len(history) > max_length:
        return history[-max_length:]  # Keep last N messages
    return history
```

### Pattern 3: Streaming Responses
```python
async with client.messages.stream(
    model="claude-v1",
    messages=[{"role": "user", "content": prompt}],
) as stream:
    async for chunk in stream.text_stream:
        print(chunk, end="", flush=True)
```

### Pattern 4: JSON Schema Enforcement
```python
system_prompt = """
You are a JSON-only service. Output only valid JSON following this schema:
{title, category, priority, summary, steps}
Do not add extra fields or explanations.
"""
```

---

## Performance Metrics

### Token Usage Comparison (from Module 3)
- **Naive Prompt**: ~800 input tokens → 500+ output tokens
- **Optimized Prompt**: ~300 input tokens → 200 output tokens
- **Savings**: ~60% reduction in token usage

### Streaming Performance (from Module 3)
- **Traditional**: Full response wait time
- **Streaming**: Real-time character delivery (better perceived performance)

---

## Troubleshooting

### Common Issues

1. **"ANTHROPIC_API_KEY not found"**
   - Ensure `.env` file exists in project root
   - Verify `ANTHROPIC_API_KEY=...` format
   - Run `load_dotenv()` before accessing `os.getenv()`

2. **"RateLimitError"**
   - Use exponential backoff (see Module 3)
   - Implement retry logic with increasing delays
   - Check API rate limits in Anthropic dashboard

3. **JSON Parse Errors**
   - Use schema enforcement in system prompt
   - Add error handling with fallback parsing
   - Clean responses before JSON parsing

4. **CSV Encoding Issues**
   - Try multiple encodings (UTF-8, Latin1, CP1252)
   - Use pandas with encoding parameter
   - Validate data before processing

---

## Learning Path

**Recommended progression:**

1. **Day 1**: Module 1 → understand basic API usage
2. **Day 2-3**: Module 2 → build conversational agents
3. **Day 4-5**: Module 3 → optimize and scale
4. **Day 6+**: Combine patterns for production applications

---

## Contributing & Extensions

Possible extensions:

- [ ] Add webhook integration for event-driven agents
- [ ] Implement vector database for semantic search
- [ ] Add multi-modal support (images, documents)
- [ ] Build monitoring/observability dashboard
- [ ] Create agent orchestration framework
- [ ] Add memory persistence (SQLite/PostgreSQL)

---

## Resources

- [Anthropic Documentation](https://docs.anthropic.com)
- [Claude API Guide](https://docs.anthropic.com/claude-3/reference/intro)
- [Python Async Guide](https://docs.python.org/3/library/asyncio.html)
- [Streaming Best Practices](https://docs.anthropic.com/claude-3/reference/streaming)

---

## License

[Specify your license]

## Author

Satwik1Anand

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| **Total Modules** | 3 |
| **Total Files** | 19 |
| **Total Lines of Code** | ~2,300 |
| **Production-Ready Files** | 15/19 |
| **Complexity Range** | Basic → Advanced |
| **Languages** | Python 3.8+ |
| **Primary Framework** | Anthropic SDK |
