class SharedMemory:
    def __init__(self):
        self.memory = {
            "inputs": [],
            "extracted": {},
            "threads": {}
        }

    def store_metadata(self, fmt, intent):
        self.memory["inputs"].append({
            "source": "user",
            "type": fmt,
            "intent": intent,
            "timestamp": self._current_timestamp()
        })

    def store_extracted(self, agent_name, extracted_data):
        self.memory["extracted"][agent_name] = extracted_data

    def store_thread(self, thread_id, thread_data):
        self.memory["threads"][thread_id] = thread_data

    def get_memory(self):
        return self.memory

    def _current_timestamp(self):
        from datetime import datetime
        return datetime.utcnow().isoformat()


