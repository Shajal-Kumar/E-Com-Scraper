import streamlit as st

def print_details(name, image, cost, detail_name, detail_val, source = None, rate = None, about = None):
    details = {}
    st.header(name.strip())
    st.subheader(cost.strip())
    try:
        st.subheader(f':yellow[{rate.strip()}]')
    except:
        st.write("Ratings Not Found")
    st.write(image)
    st.image(image)
    for i in range(len(detail_name)):
        if source == 'shopclues':
            details[detail_name[i].text.strip()] = detail_val[i].text.strip().replace(':\xa0\xa0\xa0', '')
        else:
            details[detail_name[i].text.strip()] = detail_val[i].text.strip()
    # print(details)
    st.json(details)


def get_amazon(soup):
    p_name = soup.find('span', id='productTitle').text
    img_link = soup.find('img', id='landingImage')['src']
    #img class = a-dynamic-image a-stretch-horizontal
    price = soup.find('span', class_='a-offscreen').text
    # details = soup.find('table', class_= 'a-normal a-spacing-micro').text
    # details = details.replace('    ', '  ').split('  ')
    det_name = soup.find_all('td', class_='a-span3')
    det_val = soup.find_all('td', class_='a-span9')
    about = soup.find_all('li', class_='a-spacing-mini')

    print_details(p_name, img_link, price, det_name, det_val)
    st.divider()
    st.subheader(":yellow ABOUT THIS PRODUCT")
    st.divider()
    for i in about:
        point = i.text.strip()
        # st.write(f":orange[{point.replace(",Äî", "--")}]")
        st.write(f":orange[{point.replace(",Äî", "--")}]")
        st.divider()

def get_flipkart(soup):
    p_name = soup.find('span', class_='VU-ZEz').text
    img_link = soup.find('img', class_='DByuf4 IZexXJ jLEJ7H')['src']
    price = soup.find('div', class_='Nx9bqj CxhGGd').text
    rating = soup.find('div', class_='XQDdHH').text
    det_name = soup.find_all('td', class_='+fFi1w col col-3-12')
    det_val = soup.find_all('li', class_='HPETK2')

    print_details(p_name, img_link, price, det_name, det_val, rating)

def get_ebay(soup):
    p_name = soup.find('h1', class_='x-item-title__mainTitle').text
    img_link = soup.find('div', class_='ux-image-carousel zoom img-transition-medium').find('img')['src']
    price = soup.find('div', class_='x-price-primary').text
    det_name = soup.find_all('div', class_='ux-labels-values__labels-content')
    det_val = soup.find_all('div', class_='ux-labels-values__values-content')

    print_details(p_name, img_link, price, det_name, det_val)    

def get_shopclues(soup):
    
    p_name = soup.find('div', class_ = 'prd_mid_info').find('h1').text.strip()
    img_link = soup.find('div', class_='prd_mid_info').find('img')['src']
    # prices = [price.text for price in (soup.find_all('span', class_='textual-display bsig__price bsig__price--displayprice'))]
    price = soup.find('span', class_='f_price').text.strip()
    rating = soup.find('div', class_='star_rating_point').text.strip()
    det_name = soup.findAll('td', {'width' : '30%'})
    det_val = soup.find_all('span', class_='stext')

    print_details(p_name, img_link, price, det_name, det_val, source = 'shopclues', rate = rating)





#Flipkart
    # details = soup.find_all('div', class_='GNDEQ-')
    # details = {}
    # print(p_name.strip(), img_link['src'], price.strip(), rating.strip(), sep='\n')
    # for i in range(len(det_name)):
    #     # print(det_name[i].text.strip(),':', det_val[i].text.strip())
    #     details[det_name[i].text.strip()] = det_val[i].text.strip()
    # print(details)

#eBay
    # prices = [price.text for price in (soup.find_all('span', class_='textual-display bsig__price bsig__price--displayprice'))]
    # rating = soup.find('span', class_='ux-summary__start--rating').text
    # print(p_name.strip(), img_link['src'], price.strip(), sep='\n') #rating.strip(),
    # details = {}
    # for i in range(len(det_name)):
    #     # print(det_name[i].text.strip(),':', det_val[i].text.strip())
    #     details[det_name[i].text.strip()] = det_val[i].text.strip()
    # print(details)

#ShopcLues
# print(p_name, img_link, price, rating, sep='\n')
# details = {}
# for i in range(len(det_name)):
#     # print(det_name[i].text.strip(),':', det_val[i].text.strip().replace(':\xa0\xa0\xa0', ''))
#     details[det_name[i].text.strip()] = det_val[i].text.strip().replace(':\xa0\xa0\xa0', '')
# print(details)

# def get_jio(soup):
#     p_name = soup.find('div', class_='product-header-name jm-mb-xs jm-body-m-bold').text
#     img_link = soup.find('figure', class_='figure').find('img')['src']
#     # prices = [price.text for price in (soup.find_all('span', class_='textual-display bsig__price bsig__price--displayprice'))]
#     # price = soup.find('div', class_='product-price jm-mb-xxs').find('span', class_='jm-heading-xs jm-ml-xxs').text
#     # rating = soup.find('span', class_='average').text
#     about = soup.find('ul', class_='product-key-features-list').find_all('li')
#     det_name = soup.find_all('th', class_='product-specifications-table-item-header')
#     det_val = soup.find_all('td', class_='product-specifications-table-item-data')
#     price = None
#     print_details(p_name, img_link, price, det_name, det_val)
#     st.write(about)
