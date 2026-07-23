# mimi is a nice cat 

# github : https://github.com/MohssineX

# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>

def main():

    try :

        import sys
        import os 
        import speedtest
        import json

        # Enable ANSI escape codes on Windows (not needed on Linux/Mac)

        if sys.platform == "win32":
            os.system("")

        # color variables

        color_green = "\033[32m"
        color_yellow = "\033[33m"
        color_light_blue = "\033[94m"
        color_red = "\033[31m"
        color_reset = "\033[0m"

        print("loadspeed")
        print("")
        print("Checking...")


        try :
            
            # server func 

            def best_server() :

                speed_test = speedtest.Speedtest()
                speed_test.get_best_server()
                return speed_test


            # Ping func 

            def ping(speed_test) :

                ping = f"{speed_test.results.ping:.2f}"
                print(f"{color_yellow}Ping : {ping}{color_reset} ms")

                return ping

            
            # Download func 

            def download(speed_test) :

                download_speed = speed_test.download()

                download_speed_Mbps = f"{download_speed / 1000000:.2f}"

                print(f"{color_light_blue}Download : {download_speed_Mbps}{color_reset} Mbps")

                return download_speed_Mbps

            # upload func 

            def upload(speed_test) :

                upload_speed = speed_test.upload(pre_allocate=False)
                upload_speed_Mbps = f"{upload_speed / 1000000 :.2f}"

                print(f"{color_green}Upload : {upload_speed_Mbps}{color_reset} Mbps")

                return upload_speed_Mbps


            # Ping only

            if "-p" in sys.argv :

                print("")
                speed_test = best_server()  
                ping(speed_test)

            # Download only

            elif "-d" in sys.argv :

                print("")
                speed_test = best_server()  
                download(speed_test)

            # Upload only

            elif "-u" in sys.argv :

                print("")
                speed_test = best_server()  
                upload(speed_test)

            # Json

            elif "-j" in sys.argv :

                print("")
                speed_test = best_server()
                
                download_result = download(speed_test)
                upload_result = upload(speed_test)
                ping_result = ping(speed_test)

                data = {

                    
                    "Download" : download_result ,
                    "Upload" : upload_result ,
                    "ping" : ping_result 

                }

                with open("loadspeed.json", "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)

                full_path = os.path.abspath("loadspeed.json")   
                print("")
                print(f"{color_green}Results saved to: {full_path}{color_reset}")

            # all

            else :

                print("")
                speed_test = best_server()  
                download(speed_test)
                upload(speed_test)
                ping(speed_test)

            
            print("")
            print("Done!")
        
        except Exception  :

            print(f"{color_red}err : Connection failed :({color_reset}")


    except KeyboardInterrupt :

        print("")
        print(f"{color_yellow}Thank you for using loadspeed!{color_reset}")
        print(f"{color_yellow}Author : https://github.com/MohssineX{color_reset}")
        print()
        print(f"{color_yellow}goodbye{color_reset}")
        os._exit(0)

if __name__ == "__main__":
    main()
