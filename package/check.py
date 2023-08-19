def check_prod(file):
  prefixo = "ProdutividadePolicial-"
  extensao = ".csv"
  return prefixo in file and file.endswith(extensao)

def is_xslx(filename):
  with open(filename, 'rb') as f:
    first_four_bytes = f.read()[:4]
    return first_four_bytes == b'PK\x03\x04'


def detect_encoding(file_path):
    with open(file_path, "rb") as file:
        first_bytes = file.read(4)
    hex_representation = " ".join([f"{byte:02X}" for byte in first_bytes])
    print("Primeiros 4 bytes em hexadecimal:", hex_representation)