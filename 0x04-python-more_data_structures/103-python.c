#include <Python.h>

void print_python_list(PyObject *p)
{
    if (PyList_Check(p))
    {
        Py_ssize_t size = PyList_Size(p);
        Py_ssize_t allocated = ((PyListObject *)p)->allocated;
        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", allocated);

        for (Py_ssize_t i = 0; i < size; i++)
        {
            PyObject *element = PyList_GetItem(p, i);
            const char *typeName = Py_TYPE(element)->tp_name;
            printf("Element %ld: %s\n", i, typeName);
            if (strcmp(typeName, "bytes") == 0)
                print_python_bytes(element);
        }
    }
}

void print_python_bytes(PyObject *p)
{
    printf("[.] bytes object info\n");
    if (PyBytes_Check(p))
    {
        Py_ssize_t size = PyBytes_Size(p);
        const char *string = PyBytes_AsString(p);

        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", string);

        printf("  first %ld bytes: ", size + 1);
        for (Py_ssize_t i = 0; i <= size && i < 10; i++)
        {
            printf("%02x", (unsigned char)string[i]);
            if (i < size && i < 9)
                printf(" ");
        }
        printf("\n");
    }
    else
    {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}
