class Solution:
    def encode(self, strs: List[str]) -> str:
        msg = ""
        for word in strs:
            length = len(word)
            msg += str(length)+'#'+word
        return msg
    def decode(self, s: str) -> List[str]:
        print(s)
        # init
        decoded_msg = []
        pos_idx = 0
        # loop

        while pos_idx < len(s)-1:
            delim_idx = s.find('#', pos_idx)
            print(f"delim_idx: {delim_idx}")
            length = int(s[pos_idx:delim_idx])
            print(f"pos_idx: {pos_idx}")
            print(f"length: {length}")
            word_start = delim_idx + 1
            word_end = delim_idx+length+1
            word = s[word_start:word_end]
            print(word) # 14
            decoded_msg.append(word)
            pos_idx = int(length)+delim_idx+1
            print(f"pos_idx: {pos_idx}")

        return decoded_msg