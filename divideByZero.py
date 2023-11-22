import re

def clean_code(code):
    # Remove comments and strings
    code = re.sub(r'//.*', '', code)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    code = re.sub(r'".*?"', '', code)
    return code

def find_divide_by_zero_operations_with_function_names(code):
    # Regex pattern to capture function names and bodies
    function_pattern = r'int\s+(\w+)\s*\([^)]*\)\s*\{([^}]+)\}'

    # Regex pattern to find division operations
    division_pattern = r'[^/]+/\s*([^;]+);'

    functions = re.findall(function_pattern, code, flags=re.DOTALL)

    results = []

    for function_name, function_body in functions:
        # Find all division operations within the function body
        matches = re.findall(division_pattern, function_body)

        # Check each match for potential divide by zero
        for match in matches:
            # Simplistic check for a '0' in the denominator
            if '0' in match:
                results.append(f"Function '{function_name}' has potential divide by zero.")

    return results

c_code_div = """
#include <assert.h>

int div0(int a)
{
    int b = 0;
    return a / b;
}

int divtest(int a)
{
    return a / 0;
}

int div_a_b1(int a, int b)
{
    return a / b;
}

int div_a_b2(int a, int b)
{
    assert(b != 0);
    return a / b;
}

int div_a_b3(int a, int b)
{
    int c = 9;
    c = a / c;
    if (c > b)
    {
        return c / b;
    }
    else
    {
        return a / b;
    }
}

int div_a_b4(int a, int b)
{
    int c = 9;
    while (a > b && c < 15)
    {
        a = b / c;
        c += 1;
    }
    return a;
}

int div_a_b5(int a, int b)
{
    int c = 9;
    a = c * b / (a + 3 - c * b);
    b = a * b + c;
    if (a > b)
    {
        return b + c / a;
    }
    return a;
}
"""

# Clean the code
cleaned_code_div = clean_code(c_code_div)

results_with_function_names = find_divide_by_zero_operations_with_function_names(cleaned_code_div)

print("Potential divide by zero cases in functions:", results_with_function_names)
