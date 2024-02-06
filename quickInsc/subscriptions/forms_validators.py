from django.forms import ValidationError



### Validadores de ParticipantForm

def validate_age(value):
        if not value >= 18:
            raise ValidationError("A idade deve ser maior que 18 anos.")
        

def valida_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos
    if len(cpf) != 11:
        raise ValidationError('CPF deve conter 11 dígitos')

    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        raise ValidationError('CPF inválido')

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = 11 - (soma % 11)
    digito_verificador1 = str(resto if resto < 10 else 0)

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = 11 - (soma % 11)
    digito_verificador2 = str(resto if resto < 10 else 0)

    # Verifica se os dígitos verificadores estão corretos
    if cpf[-2:] != digito_verificador1 + digito_verificador2:
        raise ValidationError('CPF inválido')
        

### Validadores de EventForm