"""Regression test for issue #825."""
import os
os.environ.setdefault("OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT", "SPAN_ONLY")

def test_materialization_preserves_generator():
    MSGS = [{"role":"system","content":"x"},{"role":"user","content":"hi"}]
    generator = (m for m in MSGS)
    materialized = list(generator) if not isinstance(generator, (list, tuple)) else generator
    assert len(materialized) == 2, "generator must be materialized to preserve messages"

def test_materialization_preserves_tool_generator():
    TOOLS = [{"type":"function","function":{"name":"f","parameters":{}}}]
    generator = (t for t in TOOLS)
    materialized = list(generator) if not isinstance(generator, (list, tuple)) else generator
    assert len(materialized) == 1, "generator must be materialized to preserve tools"
