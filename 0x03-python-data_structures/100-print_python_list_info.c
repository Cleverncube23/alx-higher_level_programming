#include <Python.h>
#include <stdio.h>

/* Print Python list info */
void print_python_list_info(PyObject *p) {

  PyObject *py_list = (PyObject *)p;
  
  printf("[*] Size of the Python List = %ld\n", PyList_Size(py_list));

  printf("[*] Allocated = %ld\n", ((PyListObject *)py_list)->allocated);

  PyObject *list = py_list;
  ssize_t list_len = PyList_Size(list);
  ssize_t i = 0;
  
  if (list_len == 0) {
    printf("[]");
  } else {
    printf("[");
    
    while (i < list_len) {
      PyObject *item = PyList_GetItem(list, i);
      const char *type_name = Py_TYPE(item)->tp_name;

      printf("%s", type_name);
      
      if (i != list_len - 1) {
        printf(", "); 
      }

      i++; 
    }
    
    printf("]\n");
  }
}
