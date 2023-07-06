# Исключения (Exception) Run-Time
# общая схема

try:  # попытка совершения операции с потенциальным исключением
    pass
except Exception as exp:  # обязательный (или finally)
    pass
else:  # если исключение не возникало
    pass
finally:  # выполнится в любом случае
    pass
