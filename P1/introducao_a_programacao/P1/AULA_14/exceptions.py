from loguru import logger

try:
    print(10/0)

except ZeroDivisionError as e:
    logger.error(f'Erro de divisão por zero: {e}')
    logger.info('Digite um divisor válido!')


except Exception as error:
    logger.error(f'Error: {error}')
    
print('Programa Finalizado')