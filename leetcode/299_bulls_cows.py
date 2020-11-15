class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        smap = {}
        gmap = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] not in smap:
                    smap[secret[i]] = 1
                else:
                    smap[secret[i]] += 1
                
                if guess[i] not in gmap:
                    gmap[guess[i]] = 1
                else:
                    gmap[guess[i]] += 1
        cows = 0
        for n in smap:
            if n not in gmap:
                continue
            cows += min(smap[n], gmap[n])
        return str(bulls) + "A" + str(cows) + "B"