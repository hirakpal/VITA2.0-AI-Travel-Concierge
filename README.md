# VITA2.0-AI-Travel-Concierge
"""
# System Architecture Diagram

```mermaid
flowchart TD
    A[Streamlit Frontend (VITA UI)] --> B[Conversation Manager (LangGraph Entry)]
    B --> C[Shared Application State]

    C --> D[Intent Agent]
    C --> E[Profile Agent]
    C --> F[Memory Agent]

    D --> G[Planner Agent (ReAct)]
    E --> G
    F --> G

    G --> H[Weather Tool]
    G --> I[Maps Tool]
    G --> J[Places Tool]
    G --> K[Flight/Hotel Tool]

    H --> L[Recommendation Orchestrator]
    I --> L
    J --> L
    K --> L

    L --> M[Governance / Audit Agent]
    M --> N[Human Approval Gateway]
    N --> O[Itinerary Builder Agent]
    O --> P[Travel DNA Memory Update]
    P --> Q[END]

