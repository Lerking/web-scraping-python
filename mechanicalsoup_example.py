import mechanicalsoup

def main():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://www.sas.dk/book/flights/?search=RT_CPH-NYC-20230521-20230528_a1c0i0y0&view=upsell&bookingFlow=points&sortBy=rec,rec&filterBy=all,all&out_class=BUSINESS&out_sub_class=SAS%20BUSINESS%20PRO&out_flight_number=SK1462,SK907")
    
    #offers = browser.page.find('td', class_='slide-plus up-grid-prods flight-products')
    #offers = browser.page.find_all('span', class_='fareprice-ubc')
    offers = browser.page.find_all('link')
    print(browser.get_url())
    print(browser.get_current_page().title.text)
    #print(browser.page)
    print(offers)

if __name__ == "__main__":
    main()
    '''
    <td flight-products="" tabindex="0" class="slide-plus up-grid-prods flight-products" aria-expanded="false"><div class="fareprice-parent fare-class-and-price-container"><span>Plus</span><!----><!----><!----><span aria-hidden="true" class="fareprice-ubc"><!----><p aria-hidden="true" class="discounted-point strike margin-auto mobilepoints max-digits">352 926 <span class="desktop-only">p</span></p></span><!----><!----><!----><!----><span role="presentation" class="sr-only"><!----><!----><span>PLUS Class fare: 352 926 <span class="points-units"> p</span><!----></span><!----><!----><!----><!----></span><!----><!----></div></td>
    '''