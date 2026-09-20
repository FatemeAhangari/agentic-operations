from typing import Any, Protocol

from llm_adapter import Interpretation, interpret_case


class LLMProvider(Protocol):
    def interpret(self, case: dict[str, Any]) -> Interpretation:
        ...


class LocalProvider:
    """Safe offline baseline used for the portfolio prototype."""

    def interpret(self, case: dict[str, Any]) -> Interpretation:
        return interpret_case(case)


class OpenAICompatibleProvider:
    """Optional provider interface.

    The repository deliberately does not contain credentials or make network
    calls. A production implementation can map this interface to an
    approved LLM gateway.
    """

    def __init__(self, client: Any):
        self.client = client

    def interpret(self, case: dict[str, Any]) -> Interpretation:
        raise NotImplementedError(
            "Connect this adapter to an approved LLM gateway."
        )
