import ast
import sys


class SecurityScanner(ast.NodeVisitor):
    def __init__(self):
        self.findings = []

    def add_finding(self, line, severity, issue, recommendation):
        self.findings.append({
            "line": line,
            "severity": severity,
            "issue": issue,
            "recommendation": recommendation
        })

    def visit_Assign(self, node):
        # Detect possible hardcoded passwords, API keys, and secrets
        for target in node.targets:
            if isinstance(target, ast.Name):
                name = target.id.lower()

                if any(word in name for word in ["password", "passwd", "secret", "api_key", "apikey", "token"]):
                    if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                        self.add_finding(
                            node.lineno,
                            "HIGH",
                            f"Possible hardcoded secret: {target.id}",
                            "Store secrets in environment variables or a secure secret manager."
                        )

        self.generic_visit(node)

    def visit_Call(self, node):
        # Detect eval()
        if isinstance(node.func, ast.Name) and node.func.id == "eval":
            self.add_finding(
                node.lineno,
                "HIGH",
                "Use of eval() detected.",
                "Avoid eval(). Use safe parsing or a restricted calculation method."
            )

        # Detect os.system()
        if (
            isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "os"
            and node.func.attr == "system"
        ):
            self.add_finding(
                node.lineno,
                "HIGH",
                "Use of os.system() detected.",
                "Avoid shell execution with user input. Use safer APIs and validate input."
            )

        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        # Detect functions that accept user-controlled input
        for argument in node.args.args:
            if argument.arg.lower() in ["input", "data", "command", "expression"]:
                self.add_finding(
                    node.lineno,
                    "MEDIUM",
                    f"Function '{node.name}' accepts potentially unsafe input.",
                    "Validate, sanitize, and constrain user input before processing it."
                )

        self.generic_visit(node)


def scan_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            source = file.read()

        tree = ast.parse(source, filename)

        scanner = SecurityScanner()
        scanner.visit(tree)

        return scanner.findings

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    except SyntaxError as error:
        print(f"Syntax error in {filename}: {error}")
        sys.exit(1)


def display_report(filename, findings):
    print("=" * 70)
    print("              SECURE CODE REVIEW REPORT")
    print("=" * 70)
    print(f"File analyzed : {filename}")
    print(f"Total findings: {len(findings)}")
    print("=" * 70)

    if not findings:
        print("No security issues detected.")
        return

    for number, finding in enumerate(findings, start=1):
        print(f"\nFinding #{number}")
        print(f"Line          : {finding['line']}")
        print(f"Severity      : {finding['severity']}")
        print(f"Issue         : {finding['issue']}")
        print(f"Recommendation: {finding['recommendation']}")
        print("-" * 70)


if __name__ == "__main__":
    target_file = "vulnerable_app.py"

    findings = scan_file(target_file)
    display_report(target_file, findings)