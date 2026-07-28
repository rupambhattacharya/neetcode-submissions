class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for current_word in strs:
            sorted_character_list = sorted(current_word)
            sorted_word_key = "".join(sorted_character_list)
            if sorted_word_key not in anagram_groups:
                anagram_groups[sorted_word_key] = []
            anagram_groups[sorted_word_key].append(current_word)
        return list(anagram_groups.values())
        