import re

from django.db import models
from django.core.exceptions import ValidationError


class TxIDField(models.CharField):
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 64) 
        kwargs.setdefault('unique', True)  
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        
        # Bitcoin-like TXIDs (hexadecimal, 64 characters)
        if not re.fullmatch(r'^[a-fA-F0-9]{64}$', value):
            raise ValidationError("Invalid transaction ID format.")

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        return name, path, args, kwargs
