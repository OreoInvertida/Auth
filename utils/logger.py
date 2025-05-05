# auth/utils/logger.py
import logging

# Configuración del logger
logger = logging.getLogger("auth_logger")
logger.setLevel(logging.INFO)

# Consola (puedes agregar FileHandler si quieres logs en archivo)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
