import collections


class Solution:
    def topKFrequent(self, nums, k):
        """
        USING THE SOLUTION FROM NEETCODE
        """
        # 1. Build a hashmap that stores the frequency of each element
        frequencies = collections.defaultdict(int)
        # Keep track of the max frequency. This way we know how big to allocate our array for step 2.
        curr_max = 0
        for num in nums:
            frequencies[num] += 1
            if frequencies[num] > curr_max:
                curr_max = frequencies[num]

        # 2. Create a list that stores a list of elements t at each possible frequency, represented by indices
        # We don't actually have to worry about the zero index, since we don't care about returning the actual frequencies.
        frequencies_to_element = [[] for _ in range(curr_max)]

        # Migrate the information from the dictionary to the list
        for num, count in frequencies.items():
            frequencies_to_element[count - 1].append(num)

        # 3. Iterate in reverse order (from high frequency to low) until we populate the top k into an output list
        output = []
        for index in range(curr_max - 1, -1, -1):
            elements_list = frequencies_to_element[index]
            for element in elements_list:
                output.append(element)
                # We can stop as soon as we have k elements, since we are addding from highest frequency to lowest
                if len(output) == k:
                    return output
        print("NEVER GOT HERE")
