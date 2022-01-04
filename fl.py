
import time
import scrapy
import json
import logging
class FlipkartAppPromo(scrapy.Spider):

    name = "flipkart-promo-app"
    merchant_name = "flipkart"
    start_urls = [
        "https://2.rome.api.flipkart.net/4/page/fetch"
    ]

    headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; sdk_gphone64_arm64 Build/SPB5.210812.003) FKUA/Retail/1290008/Android/Mobile (Google/sdk_gphone64_arm64/5ff3af5cbb9ea6c7d10aad6e36753b87)',
    'secureCookie': 'd1t14Dj8/P1h7Pz9wPzpEDT8/P9LiVdXJasoanxwBZDVAIC/cHZkCHIWSE4IxhwDZcmK/BPZ0jLCRq+rxoQdDhcun8g==',
    'sn': 'VIFCE5C2176A0F4C8F967D119DE14D1A9E.TOK2488949AB771418D83B26D019AE3EEDC.1641191921.LO',
    'Content-Type': 'application/json',
    'Cookie': 'Cookie_1=value'
    }



    payload1 = lambda y,x : f"{{\"locationContext\":null,\"pageUri\":\"{x}\",\"requestContext\":null}}"

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parseHome,method='POST',headers=self.headers,body=self.payload1("/"),dont_filter=True)
        return super().start_requests()

    def parseHome(self, response):
        
        response1 = response.json()
        bannerImageLinks = []
        bannerImages = []
        slots = response1['RESPONSE']['slots']


        ################## CENTER_CYCLIC_DOTS_ON_CONTENT View slot##############
        
        centerCyclicrederableComponents = []
        try:
            centerCyclicrederableComponents = [slot["widget"]["data"]["renderableComponents"] for slot in slots if slot.get("widget").get("viewType") == 'CENTER_CYCLIC_DOTS_ON_CONTENT']
        except Exception as e:
            logging.error(e)
        
        for centerCyclicrederableComponent in centerCyclicrederableComponents:
            for centerCyclicrederableComponent1 in centerCyclicrederableComponent:
                try:
                    bannerImages.append(centerCyclicrederableComponent1["value"]["primaryImage"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                except:
                    try:
                        bannerImages.append(centerCyclicrederableComponent1["value"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                    except:
                        try:
                            bannerImages.append(centerCyclicrederableComponent1["value"]["image"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                        except:
                            pass
                try:
                    bannerImageLinks.append(centerCyclicrederableComponent1["action"]["url"])
                except:
                    pass
        ##########################################################



        ################## LEFT_ALIGN_VIEW get slot id and iterate through every slot##############
        
        leftAlignrederableComponents = []

        try:
            leftAlignrederableComponents = [slot["widget"]["data"]["renderableComponents"] for slot in slots if slot.get("widget").get("viewType") == 'LEFT_ALIGN_VIEW']
        except Exception as e:
            logging.error(e)
        
        
        for leftAlignrederableComponent in leftAlignrederableComponents:
            for leftAlignrederableComponent1 in leftAlignrederableComponent:
                bannerImageLinks.append(leftAlignrederableComponent1["action"]["url"])
                try:
                    bannerImages.append(leftAlignrederableComponent1["value"]["primaryImage"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                except:
                    try:
                        bannerImages.append(leftAlignrederableComponent1["value"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                    except:
                        try:
                            bannerImages.append(leftAlignrederableComponent1["value"]["image"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                        except:
                            pass
                try:
                    bannerImageLinks.append(leftAlignrederableComponent1["action"]["url"])
                except:
                    pass
        ##########################################################


        ################## SOLO_VIEW slot##############
        
        
        soloViewrederableComponents = []

        try:
            soloViewrederableComponents = [slot["widget"]["data"]["renderableComponents"] for slot in slots if slot.get("widget").get("viewType") == 'SOLO_VIEW']
        except Exception as e:
            logging.error(e)
        
        for soloViewrederableComponent in soloViewrederableComponents:
            for soloViewrederableComponent1 in soloViewrederableComponent:
                try:
                    bannerImages.append(soloViewrederableComponent1["value"]["primaryImage"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                except:
                    try:
                        bannerImages.append(soloViewrederableComponent1["value"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                    except:
                        pass
                try:
                    bannerImageLinks.append(soloViewrederableComponent1["action"]["url"])
                except:
                    pass
        ##########################################################

        ################## THREE_HORIZONTAL_VIEW  View slot##############
        
        threeHorizontalrederableComponents = []

        try:
            threeHorizontalrederableComponents = [slot["widget"]["data"]["renderableComponents"] for slot in slots if slot.get("widget").get("viewType") == 'THREE_HORIZONTAL_VIEW']
        except Exception as e:
            logging.error(e)
        
        for threeHorizontalrederableComponent in threeHorizontalrederableComponents:
            for threeHorizontalrederableComponent1 in threeHorizontalrederableComponent:
                try:
                    bannerImages.append(threeHorizontalrederableComponent1["value"]["primaryImage"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                except:
                    try:
                        bannerImages.append(threeHorizontalrederableComponent1["value"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                    except:
                        try:
                            bannerImages.append(threeHorizontalrederableComponent1["value"]["image"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                        except:
                            pass
                try:
                    bannerImageLinks.append(threeHorizontalrederableComponent1["action"]["url"])
                except:
                    pass
        ##########################################################

        print(bcolors.OKBLUE + json.dumps(bannerImages,indent=3) + bcolors.ENDC)
        print(bcolors.OKBLUE + json.dumps(bannerImageLinks,indent=3) + bcolors.ENDC)

        # for link in bannerImageLinks:
        #     yield scrapy.Request(self.start_urls[0], callback=self.parseHome,method='POST',headers=self.headers,body=self.payload1(link),dont_filter=True)
        #     time.sleep(20)
        grooming_essential_care_url = "/grooming-essentials-store"
        mobile_phone_store_url_l1 = "/mobile-phones-store"
        grocery_url_l1 = "/grocery-supermart-store"
        fashion_url_l1 = "/fashion-aw21-nu-store"
        electronics_url_l1 = "/flipkart-electronics-new-store"
        home_furnishing_url_l1 = "/home-handfclp-july2021-store"
        beauty_and_grooming_url_l1 = "/beauty-and-grooming-essentials-store"
        skin_care = "/best-of-skin-care-store"
        sports_url_l1 = "/the-sports-hub-store"


        # yield scrapy.Request(self.start_urls[0], callback=self.parse_catogery,method='POST',headers=self.headers,body=self.payload1(sports_url_l1),dont_filter=True)
        # yield scrapy.Request(self.start_urls[0], callback=self.parse_grocery,method='POST',headers=self.headers,body=self.payload1("/grocery-supermart-store?marketplace=GROCERY"),dont_filter=True)
        

    
    def parse_catogery(self,response):
            response1 = response.json()
            catogery_banner_links = []
            catogery_banner_images = []   
            slots = response1['RESPONSE']['slots']


            ################## CENTER_CYCLIC_DOTS_ON_CONTENT View slot##############
            
            centerCyclicSlots = []
            centerCyclicrederableComponents = []

            for idx,slot in enumerate(slots):
                try:
                    if slot["widget"]["viewType"] == "CENTER_CYCLIC_DOTS_ON_CONTENT":
                        centerCyclicSlots.append(idx)
                        print(bcolors.OKGREEN +"CENTER_CYCLIC_DOTS_ON_CONTENT"+ str(centerCyclicSlots) + bcolors.ENDC)

                except KeyError:
                    pass
        
            for idx in centerCyclicSlots:
                centerCyclicrederableComponents.append(slots[idx]["widget"]["data"]["renderableComponents"])
        
            for centerCyclicrederableComponent in centerCyclicrederableComponents:
                for centerCyclicrederableComponent1 in centerCyclicrederableComponent:
                    try:
                        catogery_banner_images.append(centerCyclicrederableComponent1["value"]["primaryImage"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                    except:
                        try:
                            catogery_banner_images.append(centerCyclicrederableComponent1["value"]["image"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                        except:  
                            try:
                                catogery_banner_images.append(centerCyclicrederableComponent1["value"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                            except:
                                pass
                    try:
                        catogery_banner_links.append(centerCyclicrederableComponent1["action"]["url"])
                    except:
                        catogery_banner_links.append("No link")
            ##########################################################

            ################################# LEFT_ALIGN_VIEWt##############
            
            leftAlignSlots = []
            leftAlignrederableComponents = []

            for idx,slot in enumerate(slots):
                try:
                    if slot["widget"]["viewType"] == "LEFT_ALIGN_VIEW":
                        leftAlignSlots.append(idx)
                        print(bcolors.OKGREEN +"LEFT_ALIGN_VIEW"+ str(leftAlignSlots) + bcolors.ENDC)
                except KeyError:
                    pass
            
            for idx in leftAlignSlots:
                leftAlignrederableComponents.append(slots[idx]["widget"]["data"]["renderableComponents"])
            
            for leftAlignrederableComponent in leftAlignrederableComponents:
                for leftAlignrederableComponent1 in leftAlignrederableComponent:
                    try:
                        catogery_banner_images.append(leftAlignrederableComponent1["value"]["primaryImage"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                    except:
                        try:
                            catogery_banner_images.append(leftAlignrederableComponent1["value"]["image"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                        except:  
                            try:
                                catogery_banner_images.append(leftAlignrederableComponent1["value"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                            except:
                                pass
                    try:
                        catogery_banner_links.append(leftAlignrederableComponent1["action"]["url"])
                    except:
                        catogery_banner_links.append("No link")
            # ##############################################################################################################################
            
            ################## SOLO_VIEW slot##############
            
            soloViewSlots = []
            soloViewrederableComponents = []

            for idx,slot in enumerate(slots):
                try:
                    if slot["widget"]["viewType"] == "SOLO_VIEW":
                        soloViewSlots.append(idx)
                        print(bcolors.OKGREEN +"SOLO_VIEW"+ str(soloViewSlots) + bcolors.ENDC)
                except KeyError:
                    pass
            
            for idx in soloViewSlots:
                soloViewrederableComponents.append(slots[idx]["widget"]["data"]["renderableComponents"])
            
            for soloViewrederableComponent in soloViewrederableComponents:
                for soloViewrederableComponent1 in soloViewrederableComponent:
                    try:
                        catogery_banner_images.append(soloViewrederableComponent1["value"]["primaryImage"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                    except:
                        try:
                            catogery_banner_images.append(soloViewrederableComponent1["value"]["image"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                        except:
                            try:
                                catogery_banner_images.append(soloViewrederableComponent1["value"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                            except:
                                pass
                    try:
                        catogery_banner_links.append(soloViewrederableComponent1["action"]["url"])
                    except:
                        catogery_banner_links.append("No link")

            ##########################################################

            ################## MAPP_HORIZONTAL##############
            mapHorizontalSlots = []
            mapHorizontalrederableComponents = []

            for idx,slot in enumerate(slots):
                try:
                    if slot["widget"]["viewType"] == "MAPP_HORIZONTAL":
                        mapHorizontalSlots.append(idx)
                        print(bcolors.OKGREEN +"MAPP_HORIZONTAL"+ str(mapHorizontalSlots) + bcolors.ENDC)
                except KeyError:
                    pass
            
            for idx in mapHorizontalSlots:
                mapHorizontalrederableComponents.append(slots[idx]["widget"]["data"]["renderableComponents"])
            
            for mapHorizontalrederableComponent in mapHorizontalrederableComponents:
                for mapHorizontalrederableComponent1 in mapHorizontalrederableComponent:
                    try:
                        catogery_banner_images.append(mapHorizontalrederableComponent1["value"]["primaryImage"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                    except:
                        try:
                            catogery_banner_images.append(mapHorizontalrederableComponent1["value"]["image"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                        except:
                            try:
                                catogery_banner_images.append(mapHorizontalrederableComponent1["value"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                            except:
                                pass
                    try:
                        catogery_banner_links.append(mapHorizontalrederableComponent1["action"]["url"])
                    except:
                        catogery_banner_links.append("No link")
            ##########################################################

            ################## THREE_HORIZONTAL_VIEW ##############
            threeHorizontalSlots = []
            threeHorizontalrederableComponents = []

            for idx,slot in enumerate(slots):
                try:
                    if slot["widget"]["viewType"] == "THREE_HORIZONTAL_VIEW":
                        threeHorizontalSlots.append(idx)
                        print(bcolors.OKGREEN +"THREE_HORIZONTAL"+ str(threeHorizontalSlots) + bcolors.ENDC)
                except KeyError:
                    pass
            
            for idx in threeHorizontalSlots:
                threeHorizontalrederableComponents.append(slots[idx]["widget"]["data"]["renderableComponents"])

            for threeHorizontalrederableComponent in threeHorizontalrederableComponents:
                for threeHorizontalrederableComponent1 in threeHorizontalrederableComponent:
                    try:
                        catogery_banner_images.append(threeHorizontalrederableComponent1["value"]["primaryImage"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                    except:
                        try:
                            catogery_banner_images.append(threeHorizontalrederableComponent1["value"]["image"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                        except:
                            try:
                                catogery_banner_images.append(threeHorizontalrederableComponent1["value"]["dynamicImageUrl"].replace("{@width}","500").replace("{@height}","500").replace("{@quality}","90"))
                            except:
                                pass
                    try:
                        catogery_banner_links.append(threeHorizontalrederableComponent1["action"]["url"])
                    except:
                        catogery_banner_links.append("No link")

            print(bcolors.OKGREEN + json.dumps(catogery_banner_images,indent=3) + bcolors.ENDC)
            print(bcolors.OKGREEN + json.dumps(catogery_banner_links,indent=3) + bcolors.ENDC)



       
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
        
