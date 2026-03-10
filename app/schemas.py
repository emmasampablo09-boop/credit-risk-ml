from pydantic import BaseModel, Field

class ClienteInput(BaseModel):
    ExternalRiskEstimate: float = Field(..., ge = 0, le=100)
    AverageMInFile: float = Field(..., ge = 0)
    MSinceOldestTradeOpen: float = Field(..., ge = 0)
    NumSatisfactoryTrades: float = Field(..., ge = 0)
    PercentTradesNeverDelq: float = Field(..., ge = 0, le=100)
    MSinceMostRecentInqexcl7days: float = Field(..., ge = 0)
    MaxDelq2PublicRecLast12M: float = Field(..., ge = 0)
    MaxDelqEver: float = Field(..., ge = 0)
    