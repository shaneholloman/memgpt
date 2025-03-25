from typing import List, Literal, Optional

from pydantic import BaseModel, Field

from letta.schemas.message import Message


class LettaUsageStatistics(BaseModel):
    """
    Usage statistics for the agent interaction.

    Attributes:
        completion_tokens (int): The number of tokens generated by the agent.
        prompt_tokens (int): The number of tokens in the prompt.
        total_tokens (int): The total number of tokens processed by the agent.
        step_count (int): The number of steps taken by the agent.
    """

    message_type: Literal["usage_statistics"] = "usage_statistics"
    completion_tokens: int = Field(0, description="The number of tokens generated by the agent.")
    prompt_tokens: int = Field(0, description="The number of tokens in the prompt.")
    total_tokens: int = Field(0, description="The total number of tokens processed by the agent.")
    step_count: int = Field(0, description="The number of steps taken by the agent.")
    # TODO: Optional for now. This field makes everyone's lives easier
    steps_messages: Optional[List[List[Message]]] = Field(None, description="The messages generated per step")
