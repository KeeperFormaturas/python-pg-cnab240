from unicodedata import normalize


class Attribute:
    def __init__(self, name, type, length, start, end, default_value='', pad_content=0, pad_direction='left', required=False, datetime_format='', date_format='', time_format=''):
        self.name = name
        self.type = type
        self.length = length
        self.start = start
        self.end = end
        self.default_value = default_value
        self.pad_content = str(pad_content)
        self.pad_direction = pad_direction
        self.required = required
        self.value = None
    
    def is_required(self):
        return self.required
    
    def get_value(self):
        return self.value
    
    def set_value(self, new_value):
        if self.type == 'int':
            self.value = int(new_value)
        elif self.type == 'string':
            self.value = str(new_value)
        elif self.type == 'float':
            self.value = str(round(float(new_value), 2)).replace('.', '')
        elif self.type == 'whites':
            self.value = ' '
        
        self.value = str(self.value).upper

        self.clean_value()
        
        self.pad_value()
    
    def clean_value(self):
        # remove special chars
        special_chars = [',', '.', '-', '_', '*', '&', '´', '`', "'", '"', '!', '?', '/', ':', ';', '>', '<', '^', '~', ']', '}', '{', '[', 'ª', 'º', '#', '%', '¨', '(', ')', '+', '=', '§', '¬', '£', '¹', '²', '³', '°']
        for char in special_chars:
            self.value = self.value.replace(char, '')
        
        # remove accents
        self.value = normalize('NFKD', self.value).encode('ASCII', 'ignore').decode('ASCII')
    
    def pad_value(self):
        if len(self.value) < self.length:
            if self.pad_direction == 'left':
                self.value = self.value.rjust(self.length, self.pad_content)
            else:
                self.value = self.value.ljust(self.length, self.pad_content)
