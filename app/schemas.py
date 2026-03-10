from pydantic import BaseModel, Field

class ClienteInput(BaseModel):
    NetFractionRevolvingBurden:      float = Field(..., ge=0, le=100)
    ExternalRiskEstimate:            float = Field(..., ge=0, le=100)
    AverageMInFile:                  float = Field(..., ge=0)
    PercentTradesWBalance:           float = Field(..., ge=0, le=100)
    MSinceOldestTradeOpen:           float = Field(..., ge=0)
    NumSatisfactoryTrades:           float = Field(..., ge=0)
    PercentInstallTrades:            float = Field(..., ge=0, le=100)
    MSinceMostRecentInqexcl7days:    float = Field(..., ge=0)
    