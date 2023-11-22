import re

def clean_code(code):
    # Remove comments and strings
    code = re.sub(r'//.*', '', code)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    code = re.sub(r'".*?"', '', code)
    return code

def find_array_index_out_of_bound_operations_enhanced(code):
    # Regex pattern to capture function names and bodies
    function_pattern = r'int\s+(\w+)\s*\([^)]*\)\s*\{([^}]+)\}'

    # Enhanced regex pattern to find array accesses
    array_access_pattern = r'\b\w+\s*\[\s*([^]]+)\s*\]'

    functions = re.findall(function_pattern, code, flags=re.DOTALL)

    results = []

    for function_name, function_body in functions:
        # Find all array accesses within the function body
        matches = re.findall(array_access_pattern, function_body)

        # For each match, add the function name and the array access
        for match in matches:
            # Check for potential out-of-bound scenarios (basic check)
                results.append(f"Function '{function_name}' has potential out-of-bound array access: [{match}]")

    return results
c_code_array = """
#include <assert.h>
int array1(int i)
{
    int a[] = {0, 1, 9};
    return a[i];
}

int array2(int i)
{
    int a[] = {0, 1, 2};
    int b = 3, c = 4;
    if (i <= 2 && i >= 0)
    {
        return a[i] + (a[i + 1] + 1) * a[i + 2];
    }
    else
    {
        return 0;
    }
}

int array3(int i)
{
    int a[5], b, c;
    a[4] = 100;
    return a[i];
}

int array4(int i)
{
    assert(i > 0 && i < 4);
    int a[] = {1, 2, 3, 4};
    int b[] = {1, 2, 3, 4, 5};
    return a[i] + b[i + 1];
}

int array5(int x, int y)
{
    int a[] = {1, 2, 3, 4, 5, 6, 7};
    int index = 3;
    if (x > y)
    {
        index += y;
    }
    else
    {
        index += x;
    }
    return a[index];
}

int array6(int x, int y)
{
    assert(x < 7);
    int a[] = {1, 2, 3, 4, 5, 6, 7};
    int index = 3;
    if (x > y)
    {
        index += y;
    }
    else
    {
        index += x;
    }
    return a[index];
}
"""

# Clean the code
cleaned_code_array = clean_code(c_code_array)

# Find potential array index out-of-bound operations with enhanced detection
enhanced_results = find_array_index_out_of_bound_operations_enhanced(cleaned_code_array)

# Print the results
print("Enhanced results of potential array index out-of-bounds:", enhanced_results)
