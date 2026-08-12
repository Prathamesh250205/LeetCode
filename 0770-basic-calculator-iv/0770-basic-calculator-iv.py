import re

class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        evalmap = dict(zip(evalvars, evalints))
        tokens = re.findall(r'\d+|[a-z]+|\S', expression)
        pos = [0]

        def poly_mul(a, b):
            result = {}
            for ka, va in a.items():
                for kb, vb in b.items():
                    key = tuple(sorted(ka + kb))
                    result[key] = result.get(key, 0) + va * vb
            return result

        def poly_add(a, b, sign):
            result = dict(a)
            for k, v in b.items():
                result[k] = result.get(k, 0) + sign * v
            return result

        def parseFactor():
            tok = tokens[pos[0]]
            if tok == '(':
                pos[0] += 1
                e = parseExpr()
                pos[0] += 1  # consume ')'
                return e
            pos[0] += 1
            if tok.isdigit():
                return {(): int(tok)}
            if tok in evalmap:
                return {(): evalmap[tok]}
            return {(tok,): 1}

        def parseTerm():
            result = parseFactor()
            while pos[0] < len(tokens) and tokens[pos[0]] == '*':
                pos[0] += 1
                result = poly_mul(result, parseFactor())
            return result

        def parseExpr():
            result = parseTerm()
            while pos[0] < len(tokens) and tokens[pos[0]] in ('+', '-'):
                op = tokens[pos[0]]
                pos[0] += 1
                result = poly_add(result, parseTerm(), 1 if op == '+' else -1)
            return result

        poly = parseExpr()
        poly = {k: v for k, v in poly.items() if v != 0}

        items = sorted(poly.items(), key=lambda item: (-len(item[0]), item[0]))

        output = []
        for variables, coeff in items:
            if not variables:
                output.append(str(coeff))
            else:
                output.append(str(coeff) + '*' + '*'.join(variables))

        return output