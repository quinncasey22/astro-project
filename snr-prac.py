#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt


# In[2]:


hdu=fits.open('galSpecLine-dr9.fits')
hdu.info()


# In[3]:


hdu[1].header


# In[11]:


ha = hdu[1].data['H_ALPHA_FLUX']
hb = hdu[1].data['H_BETA_FLUX']
ha_err = hdu[1].data['H_ALPHA_FLUX_ERR']
hb_err = hdu[1].data['H_BETA_FLUX_ERR']


# In[12]:


ha = np.array(ha)
ha_err = np.array(ha_err)
print(ha, ha_err)


# In[13]:


hb = np.array(hb)
hb_err = np.array(hb_err)
print(hb, hb_err)


# In[14]:


ha_new=ha[ha/ha_err >3]


# In[ ]:




