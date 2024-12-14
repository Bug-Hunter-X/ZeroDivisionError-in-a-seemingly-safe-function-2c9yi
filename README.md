# Uncommon Python Error: ZeroDivisionError in seemingly safe function

This repository demonstrates a subtle case of a `ZeroDivisionError` in a Python function where the error might not be immediately obvious.

The function `function_with_uncommon_error` attempts to handle the case where either `a` or `b` is zero; however, it has a flaw in its logic.