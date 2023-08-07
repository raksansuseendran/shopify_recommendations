import streamlit as st
import urllib.request as urllib
import json
import time
import subprocess

st.title('Shopify Product Recommendations')

def get_recommendations(base_url, product_id):
   url = base_url+'recommendations/products.json?product_id='+product_id+'&intent=related'
   
   data = urllib.urlopen(url).read()
   products = json.loads(data)['products']
   
   for product in products:
        st.write('-------------------------------------')

        st.image('https:'+ product['featured_image'], width=200)
    
        st.write('Product ID: ', product['id'])
        st.write('Product Name: ', product['title'])
        st.write('Product Handle: ', base_url+'products/'+product['handle'])
        st.write('Product Description: ', product['description'])
        st.write('Product Price: ', product['price'])
        
        if product['available'] == True:
            st.write('Product Availability: Available')

        else:
            st.write('Product Availability: Not Available')
        
        time.sleep(5)

   return


base_url = st.text_input('Enter the base URL: ')
product_handle = st.text_input('Enter the product ID: ')


if st.button('Get Product Details'):
    url_b = base_url+'products/'+product_handle+'.js'
    data_b = urllib.urlopen(url_b).read()
    product = json.loads(data_b)


   
   # display the product image
    st.image('https:'+ product['images'][0], width=200)
    st.write('Product ID: ', product['id'])
    st.write('Product Name: ', product['title'])
    st.write('Product Handle: ', base_url+'products/'+product['handle'])
    st.write('Product Description: ', product['description'])
    st.write('Product Price: ', product['price'])
    
    if product['available'] == True:
        st.write('Product Availability: Available')

    else:
        st.write('Product Availability: Not Available')


if st.button('Get Recommendations'):
    url_b = base_url+'products/'+product_handle+'.js'
    data_b = urllib.urlopen(url_b).read()
    product = json.loads(data_b)

    product_id = str(product['id'])
    get_recommendations(base_url, product_id)

time.sleep(5)



