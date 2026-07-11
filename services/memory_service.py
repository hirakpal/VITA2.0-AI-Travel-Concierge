"""
Memory Service

Acts as the persistence layer between the application
and any memory backend (MemorySaver, Redis, DB, etc.)

For MVP:
- Uses in-memory dictionary
- Can later be replaced by LangGraph MemorySaver
"""

from __future__ import annotations

from copy import deepcopy
from typing import Dict, Optional

from models.travel_dna import TravelDNA


class MemoryService:

    def __init__(self):

        self._travel_dna_store: Dict[str, TravelDNA] = {}

    # --------------------------------------------------
    # Travel DNA
    # --------------------------------------------------

    def load_travel_dna(
        self,
        session_id: str,
    ) -> Optional[TravelDNA]:

        dna = self._travel_dna_store.get(session_id)

        if dna is None:
            return None

        return deepcopy(dna)

    def save_travel_dna(
        self,
        session_id: str,
        dna: TravelDNA,
    ):

        self._travel_dna_store[session_id] = deepcopy(dna)

    def clear_travel_dna(
        self,
        session_id: str,
    ):

        if session_id in self._travel_dna_store:
            del self._travel_dna_store[session_id]

    # --------------------------------------------------
    # Generic Memory
    # --------------------------------------------------

    def exists(
        self,
        session_id: str,
    ) -> bool:

        return session_id in self._travel_dna_store

    def reset(self):

        self._travel_dna_store.clear()
