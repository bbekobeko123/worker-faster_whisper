INPUT_VALIDATIONS = {
    'audio': {
        'type': str,
        'required': False,
        'default': None
    },
    'audio_base64': {
        'type': str,
        'required': False,
        'default': None
    },
    'model': {
        'type': str,
        'required': False,
        'default': 'base'
    },
    'transcription': {
        'type': str,
        'required': False,
        'default': 'plain_text'
    },
    'translate': {
        'type': bool,
        'required': False,
        'default': False
    },
    'translation': {
        'type': str,
        'required': False,
        'default': 'plain_text'
    },
    'language': {
        'type': str,
        'required': False,
        'default': None
    },
    'temperature': {
        'type': (float, list, tuple),
        'required': False,
        'default': [0.0, 0.2, 0.4]
    },
    'best_of': {
        'type': int,
        'required': False,
        'default': 5
    },
    'beam_size': {
        'type': int,
        'required': False,
        'default': 10
    },
    'patience': {
        'type': float,
        'required': False,
        'default': 2.0
    },
    'length_penalty': {
        'type': float,
        'required': False,
        'default': 0
    },
    'suppress_tokens': {
        'type': str,
        'required': False,
        'default': '-1'
    },
    'initial_prompt': {
        'type': str,
        'required': False,
        'default': None
    },
    'condition_on_previous_text': {
        'type': bool,
        'required': False,
        'default': False
    },
    'temperature_increment_on_fallback': {
        'type': float,
        'required': False,
        'default': 0.2
    },
    'compression_ratio_threshold': {
        'type': float,
        'required': False,
        'default': 2.4
    },
    'logprob_threshold': {
        'type': (float, type(None)),
        'required': False,
        'default': None
    },
    'no_speech_threshold': {
        'type': float,
        'required': False,
        'default': 1.0
    },
    'enable_vad': {
        'type': bool,
        'required': False,
        'default': False
    },
    'word_timestamps': {
        'type': bool,
        'required': False,
        'default': True
    },
    'chunk_length': {
        'type': float,
        'required': False,
        'default': 15.0
    },
}
