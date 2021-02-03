#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[ ]:


a="hello world"

get_ipython().run_line_magic('pinfo', 'a')

print(a)

