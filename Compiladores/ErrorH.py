import re

def analyze_java_code(code):
    # Expresiones regulares para buscar errores comunes en el código Java
    regex_errors = {
        "missing_semicolon": r";(?![^(){}]*\))",
        "missing_closing_brace": r"{(?![^{}]*\})",
        "missing_opening_brace": r"(?<![{}])}",
        "unterminated_string": r"\".*?(?<!\\)\"",
        "unterminated_comment": r"\/\*.*",
        "unused_import": r"import .*?;",
        "unreachable_code": r"throw new RuntimeException\(\"Unreachable code\"\);"
    }
    
    # Analizar el código en busca de errores
    errors = {}
    for error_type, regex_pattern in regex_errors.items():
        matches = re.findall(regex_pattern, code)
        if matches:
            errors[error_type] = matches
    
    return errors

# Código Java de ejemplo
java_code = """
public class Test {
    public static void main(String[] args) {
        int x = 10;
        int y = 20;
        System.out.println("Sum: " + (x + y));
    }
}
"""

# Analizar el código Java
error_report = analyze_java_code(java_code)

# Mostrar los errores encontrados
if error_report:
    print("Errores encontrados:")
    for error_type, error_lines in error_report.items():
        print(f"- {error_type}:")
        for line in error_lines:
            print(f"  Línea {line}")
else:
    print("No se encontraron errores.")