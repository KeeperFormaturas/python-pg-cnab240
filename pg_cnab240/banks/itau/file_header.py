from datetime import datetime
from pg_cnab240.file_section import FileSection


class FileHeader(FileSection):
    def __init__(self, data=None):
        super().__init__('FileHeader', data, {
            'bank_code': {
                'type': 'int',
                'length': 3,
                'default': 341,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 0,
                'end': 3,
                'value': None,
            },
            'lot_code': {
                'type': 'int',
                'length': 4,
                'default': 0000,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': False,
                'start': 3,
                'end': 7,
                'value': None,
            },
            'register_type': {
                'type': 'int',
                'length': 1,
                'default': 0,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': False,
                'start': 7,
                'end': 8,
                'value': None,
            },
            'register_type_whites': {
                'type': 'whites',
                'length': 6,
                'default': '',
                'pad_content': ' ',
                'pad_direction': 'left',
                'required': False,
                'start': 8,
                'end': 14,
                'value': None,
            },
            'file_layout': {
                'type': 'int',
                'length': 3,
                'default': '081',
                'pad_content': 0,
                'pad_direction': 'left',
                'required': False,
                'start': 14,
                'end': 17,
                'value': None,
            },
            'company_document_type': {
                'type': 'int',
                'length': 1,
                'default': 2, # 1 = CPF / 2 = CNPJ
                'pad_content': 0,
                'pad_direction': 'left',
                'required': False,
                'start': 17,
                'end': 18,
                'value': None,
            },
            'company_document_number': {
                'type': 'int',
                'length': 14,
                'default': '',
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 18,
                'end': 32,
                'value': None,
            },
            'inscription_number_whites': {
                'type': 'whites',
                'length': 20,
                'default': '',
                'pad_content': ' ',
                'pad_direction': 'left',
                'required': False,
                'start': 32,
                'end': 52,
                'value': None,
            },
            'agency': {
                'type': 'int',
                'length': 5,
                'default': '',
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 52,
                'end': 57,
                'value': None,
            },
            'agency_whites': {
                'type': 'whites',
                'length': 1,
                'default': '',
                'pad_content': ' ',
                'pad_direction': 'left',
                'required': False,
                'start': 57,
                'end': 58,
                'value': None,
            },
            'account': {
                'type': 'int',
                'length': 12,
                'default': '',
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 58,
                'end': 70,
                'value': None,
            },
            'account_whites': {
                'type': 'whites',
                'length': 1,
                'default': '',
                'pad_content': 0,
                'pad_direction': 'left',
                'required': False,
                'start': 70,
                'end': 71,
                'value': None,
            },
            'dac': { # bank account digit
                'type': 'int',
                'length': 1,
                'default': 0,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 71,
                'end': 72,
                'value': None,
            },
            'company_name': {
                'type': 'string',
                'length': 40,
                'default': '',
                'pad_content': ' ',
                'pad_direction': 'right',
                'required': True,
                'start': 72,
                'end': 102,
                'value': None,
            },
            'bank_name': {
                'type': 'string',
                'length': 30,
                'default': 'BANCO ITAU SA',
                'pad_content': ' ',
                'pad_direction': 'right',
                'required': False,
                'start': 102,
                'end': 132,
                'value': None,
            },
            'bank_name_whites': {
                'type': 'whites',
                'length': 10,
                'default': '',
                'pad_content': 0,
                'pad_direction': 'left',
                'required': False,
                'start': 132,
                'end': 142,
                'value': None,
            },
            'file_code': {
                'type': 'int',
                'length': 1,
                'default': 1, # 1 - Shipping / 2 - Return
                'pad_content': 0,
                'pad_direction': 'left',
                'required': True,
                'start': 142,
                'end': 143,
                'value': None,
            },
            'generation_date': {
                'type': 'date',
                'length': 6,
                'default': datetime.utcnow().strftime(self.default_date_format),
                'pad_content': '',
                'pad_direction': 'left',
                'required': False,
                'start': 143,
                'end': 151,
                'value': None,
            },
            'generation_hour': {
                'type': 'date',
                'length': 6,
                'default': datetime.utcnow().strftime(self.default_time_format),
                'pad_content': '',
                'pad_direction': 'left',
                'required': False,
                'start': 151,
                'end': 157,
                'value': None,
            },
            'generation_zeros': {
                'type': 'int',
                'length': 9,
                'default': 0,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': False,
                'start': 157,
                'end': 166,
                'value': None,
            },
            'density_unit': {
                'type': 'int',
                'length': 5,
                'default': 0,
                'pad_content': 0,
                'pad_direction': 'left',
                'required': False,
                'start': 166,
                'end': 171,
                'value': None,
            },
            'density_unit_whites': {
                'type': 'whites',
                'length': 69,
                'default': ' ',
                'pad_content': ' ',
                'pad_direction': 'left',
                'required': False,
                'start': 171,
                'end': 240,
                'value': None,
            },
        })
        
        self.bank = None
    
    def set_bank(self, bank):
        self.bank = bank
    
    def set_data(self, company):
        if not company:
            raise Exception('Company cannot be None')
        
        super().set_data(dict(
            bank_code = self.bank.code,
            company_document_type = self.bank.get_company_document_id(company.document_type),
            company_document_number = company.document,
            agency = company.agency,
            account = company.account,
            dac = company.account_digit,
            company_name = company.name,
        ))
