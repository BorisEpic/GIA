"""Prepara solicitudes de generación y empaqueta bancos revisados."""

import argparse
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_STORED, ZipFile

ROOT = Path(__file__).resolve().parent


def comprimir(documento, contenidos):
    banco = ROOT / "Generadas" / documento.stem
    esperadas = {
        Path(f"Contenido {contenido}", destinatario,
             f"actividades_{inicio:02}-{inicio + 4:02}.png")
        for contenido in contenidos
        for destinatario in ("Alumno", "Profesor")
        for inicio in range(1, 61, 5)
    }
    presentes = {ruta.relative_to(banco) for ruta in banco.rglob("*") if ruta.is_file()}
    diferencias = [
        f"{estado}: {ruta}"
        for estado, rutas in (("Falta", esperadas - presentes),
                              ("Archivo adicional", presentes - esperadas))
        for ruta in sorted(rutas)
    ]
    if diferencias:
        raise ValueError("\n".join(diferencias))

    destino = ROOT / "Comprimidos" / f"{banco.name}.zip"
    destino.parent.mkdir(exist_ok=True)
    with NamedTemporaryFile(dir=destino.parent, delete=False) as archivo:
        temporal = Path(archivo.name)
    try:
        with ZipFile(temporal, "w", compression=ZIP_STORED) as zip_final:
            for ruta in sorted(esperadas):
                zip_final.write(banco / ruta, Path(banco.name, ruta))
        with ZipFile(temporal) as zip_final:
            if archivo_danado := zip_final.testzip():
                raise ValueError(f"Archivo dañado en el ZIP: {archivo_danado}")
        temporal.replace(destino)
    finally:
        temporal.unlink(missing_ok=True)
    print(destino.relative_to(ROOT))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    comandos = parser.add_subparsers(dest="comando", required=True)
    prompt = comandos.add_parser("prompt", help="Imprime el prompt para el asistente")
    zip_final = comandos.add_parser("comprimir", help="Crea el ZIP de un banco revisado")
    for comando in (prompt, zip_final):
        comando.add_argument("documento", type=Path, help="Ruta al DOCX dentro de Data")
    zip_final.add_argument("--contenidos", type=int, nargs="+", required=True)
    args = parser.parse_args()
    documento = (ROOT / args.documento).resolve()
    if (documento.parent != (ROOT / "Data").resolve()
            or documento.suffix.lower() != ".docx" or not documento.is_file()):
        parser.error("Indica un archivo .docx existente directamente dentro de Data.")

    if args.comando == "prompt":
        print(f'Procesa `{documento.relative_to(ROOT)}` según `GUIA_DE_GENERACION.md`. '
              'Genera y verifica todas las parejas alumno–profesor. '
              'Entrega el ZIP final en `Comprimidos`.')
    else:
        try:
            comprimir(documento, args.contenidos)
        except (OSError, ValueError) as error:
            parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
