    @classmethod
    def from_gameFull_event(cls, gameFull_event: dict[str, Any]) -> 'Game_Information':
        assert gameFull_event['type'] == 'gameFull'

        raw_state = gameFull_event['state']
        if isinstance(raw_state, str):
            import json
            state = json.loads(raw_state)
        else:
            state = raw_state

        return cls(
            id_=gameFull_event['id'],
            white_title=gameFull_event['white'].get('title'),
            white_name=gameFull_event['white'].get('name', 'AI'),
            white_rating=gameFull_event['white'].get('rating'),
            white_ai_level=gameFull_event['white'].get('aiLevel'),
            white_provisional=gameFull_event['white'].get('provisional', False),
            black_title=gameFull_event['black'].get('title'),
            black_name=gameFull_event['black'].get('name', 'AI'),
            black_rating=gameFull_event['black'].get('rating'),
            black_ai_level=gameFull_event['black'].get('aiLevel'),
            black_provisional=gameFull_event['black'].get('provisional', False),
            initial_time_ms=gameFull_event['clock']['initial'],
            increment_ms=gameFull_event['clock']['increment'],
            speed=gameFull_event['speed'],
            rated=gameFull_event['rated'],
            variant=Variant(gameFull_event['variant']['key']),  # ✅ This is correct
            variant_name=gameFull_event['variant']['name'],
            initial_fen=gameFull_event.get('initialFen', ''),
            fen_str=gameFull_event.get('initialFen', ''),
            state=state
        )
