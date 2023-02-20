class Solution:
    def validIpv4(self, ip):
        splited_ip = ip.split(".")
        if len(splited_ip)!=4:
            return False
        for section in splited_ip:
            if len(section) == 0:
                return False
            if len(section) != 1 and section[0] == "0":
                return False
            for i in section:
                if not i.isnumeric():
                    return False
            if not(0<=int(section)<=255):
                return False
        return True

            

    def validIpv6(self, ip):
        splited_ip = ip.split(":")
        print(splited_ip)
        possible_char = {"a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"}
        if len(splited_ip)!=8:
            return False
        for section in splited_ip:
            if not(1<=len(section)<=4):
                return False
            for i in section:
                if (i not in possible_char) and (not i.isnumeric()):
                    return False
        return True

        
    def validIPAddress(self, queryIP: str) -> str:
        
        if "." in queryIP:
            return "IPv4" if self.validIpv4(queryIP) else "Neither"
        return "IPv6" if self.validIpv6(queryIP) else "Neither"