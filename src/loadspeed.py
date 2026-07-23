# mimi is a nice cat 

# github : https://github.com/MohssineX

# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>

def main():

    try :

        

        import os 
        import speedtest
        import sys

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
        print("")

        try :

            speed_test = speedtest.Speedtest()

            speed_test.get_best_server()

            # Ping only
            if "-p" in sys.argv :
                
                # Ping

                ping = speed_test.results.ping
                print(f"{color_yellow}Ping : {ping:.2f}{color_reset} ms")

            # Download only
            elif "-d" in sys.argv :

                # Download

                download_speed = speed_test.download()

                download_speed_Mbps = download_speed / 1000000

                print(f"{color_light_blue}Download : {download_speed_Mbps:.2f}{color_reset} Mbps")

            # Upload only
            elif "-u" in sys.argv :

                # Upload

                upload_speed = speed_test.upload(pre_allocate=False)
                upload_speed_Mbps = upload_speed / 1000000

                print(f"{color_green}Upload : {upload_speed_Mbps:.2f}{color_reset} Mbps")

            # all
            else :
            
                # Download

                download_speed = speed_test.download()

                download_speed_Mbps = download_speed / 1000000

                print("")
                print(f"{color_light_blue}Download : {download_speed_Mbps:.2f}{color_reset} Mbps")

                # Upload

                upload_speed = speed_test.upload(pre_allocate=False)
                upload_speed_Mbps = upload_speed / 1000000

                print(f"{color_green}Upload : {upload_speed_Mbps:.2f}{color_reset} Mbps")

                # ping

                ping = speed_test.results.ping
                print(f"{color_yellow}Ping : {ping:.2f}{color_reset} ms")

            print("")
            print("Done!")
        
        except Exception  :

            print("")
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
    
